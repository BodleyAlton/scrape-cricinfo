from app import app
from flask import request,jsonify,json
from lxml import html
import requests,random,os
from model import *
from genalgo import *
# Consider creating a text file with player ID's and creating a function which would 
# read the ID's from the file and call scarpe(plid) with each ID

@app.route("/plids",methods=["GET"])
def get_plid():
    with open(os.getcwd()+'/playerIds.txt', 'r') as plids:
        for plid in plids:
            print int(plid)
            scrape(int(plid))
            
    return "done"

#--------------Scrape player data from cric info and update database--------------
#@app.route("/scrape/<plid>",methods=["GET"])
def scrape(plid):
    datav=[]
    page= requests.get("http://www.espncricinfo.com/westindies/content/player/%s.html"%(plid))
    tree = html.fromstring(page.content)
    name= tree.xpath("//div[@class='pnl490M']/div[2]/div/p[1]/span/text()")
    born= tree.xpath("//div[@class='pnl490M']/div[2]/div/p[b='Born']/span/text()")
    teams= tree.xpath("//div[@class='pnl490M']/div[2]/div/p[b='Major teams']/span/text()")
    batStyle=tree.xpath("//div[@class='pnl490M']/div[2]/div/p[b='Batting style']/span/text()")
    bowStyle=tree.xpath("//div[@class='pnl490M']/div[2]/div/p[b='Bowling style']/span/text()")
    playerType=tree.xpath("//div[@class='pnl490M']/div[2]/div/p[b='Playing role']/span/text()")
    data=tree.xpath("//div[@class='pnl490M']/table/tbody/tr[td[@title='Insights on odi']]/td[@nowrap='nowrap']/text()")
    for i in data:
        i=i.translate(None, '\t\n ')
        if i != "":
            if i== '-':
                datav.append('0')
            else:
                datav.append(i)
    player={"Note":"Dataset updated"},{"info":{"name":name[0],"YOB":born[0][1:],"Team":teams[0], "data":datav,"Batting Style":batStyle, "Bowling Style":bowStyle,"Player Type":playerType[0]}}
    updDataset(plid,name,born,teams,playerType,batStyle,bowStyle,datav) # Add player to DB
    jsn= jsonify(player)
    return jsn
#--------------Update Database---------
def updDataset(plid,name,born,teams,playerType,batStyle,bowStyle,datav):
    if datav[19]!='0':
        bbi= float(datav[19].split('/')[0]) / float(datav[19].split('/')[1])
    else:
        bbi=0
    if datav[20]!='0':
        bbm= float(datav[20].split('/')[0]) / float(datav[20].split('/')[1])
    else:
        bbm=0
    yob= born[0][1:]
    playerType=playerType[0]
    if batStyle != []:
        batStyle=batStyle[0]
    else:
        batStyle= None
    if bowStyle != []:
        bowStyle=bowStyle[0]
    else:
        bowStyle=None
    playerinf=Player(plid,name[0],yob,teams[0],playerType,batStyle,bowStyle)
    batting= Batting(plid,datav[0],datav[1],datav[2],datav[3],datav[4],datav[5],datav[6],datav[7],datav[8],datav[9],datav[10],datav[11],datav[12],datav[13])
    bowling= Bowling(plid,datav[14],datav[15],datav[16],datav[17],datav[18],bbi,bbm,datav[21],datav[22],datav[23],datav[24],datav[25],datav[26])
    db.session.add(playerinf)
    db.session.commit()
    db.session.add_all([batting,bowling])
    db.session.commit()
#----------Creates Random Player [plid,[ptype],[stats(bat ave,bow ave, wkts)]]---------------
def getRandPlayer():
    randPlyr=[] # Random player
    typ=[] #Player Type
    plrstats=[] #Player Stats
    rp=randPlid() #plid of randomly selected player
    #
    for i in db.session.query(Player.plid,Player.ptype).filter_by(plid=rp).all():
        randPlyr.append(i.plid)
        if "Batsman" in i.ptype or "batsman" in i.ptype:
            typ.append("batsman")
            for p in db.session.query(Batting.ave).filter_by(plid=rp).all():
                plrstats.append(p.ave)
        if "Bowler" in i.ptype or "Bowling" in i.ptype:
            typ.append("bowler")
            for p in db.session.query(Bowling.wkts,Bowling.ave).filter_by(plid=rp).all():
                plrstats.append(p.ave)
                plrstats.append(p.wkts)
        if "Wicketkeeper" in i.ptype or "wicketkeeper" in i.ptype:
            typ.append("wicketkeeper")
            for p in db.session.query(Bowling.wkts).filter_by(plid=rp).all():
                plrstats.append(p.wkts)
        if "Allrounder" in i.ptype:
            typ.append("allrounder")
            for p in db.session.query(Batting.ave).filter_by(plid=rp).all():
                batav=p.ave
                plrstats.append(batav)
            for p in db.session.query(Bowling.wkts,Bowling.ave).filter_by(plid=rp).all():
                bowave=p.ave
                plrstats.append(bowave)
                plrstats.append(p.wkts)
    randPlyr.append(typ)
    randPlyr.append(plrstats)
    # print randPlyr
    return randPlyr
#-------Selects a random plid-------
def randPlid():
    plids=[] # player ID's
    # Query all player ID's (pid) from Player table in database
    for pid in db.session.query(Player.plid): 
        plids.append(pid)
    rplidPos=random.randint(0,len(plids)-1) # Random index in plids
    rplid= plids[rplidPos][0] # Retreve plid at randomly selected index
    return rplid
    
#--------Create random team of 11 players-------------
def randTeam():
    rndtm=[] # Randomly Selected team of 11 players
    pl=0 #Counter keeping track of the number of unique players added to the team
    while pl < 11:
        player= getRandPlayer() #Random Player
        if dups(rndtm,player)== False: #Asserts that the player is unique to the team
            pl+=1
            rndtm.append(player) # Append unique player to the team
    return  rndtm
    
 #-------Generate Random Population of 20 Teams------------
def getRndPop():
#pop --> [ [team] ] ,[ [ [player] ] ], [ [ [plid,[ptype],[stats] ] ] ]
#pop[] -> Team
#pop[][] -> Player
#pop[][][0] -> plid
#pop[][][1] -> ptype[x,y]
#pop[][][2] -> stats[x,y,z]
  #Stats based on player type
    # if ptype =
    # batsman -> [bat ave]
    # bowler -> [bow ave,wkts]
    # wicketkeeper -> [bat ave, wkts]
    # allrounder -> [bat ave, bow ave, wkts]
    pop=[] # population 
    #Generate initiales population of 20 teams
    for i in range(0,20):
        pop.append(randTeam())
    return pop
    
#--------Determine the fitness of each player and of each team n population--------
def fitness(pop):
    for t in pop:
        for p in t:
            plfitness(p) #Fitness of each player in team
    for t in pop:
        tmfitness(t) # FItness of each team in population
        
#------Returns sort key--------
def getKey(p):
    return p[-1]

#------Selects a random index in a list------
def randInd(lst):
    ind=random.randint(0,len(lst)-1)
    return ind

#------Removes fitness values from teams and players------
def dropFitness(pop):
    for t in pop:
        if type(t[-1])==float:
            del t[-1]
        for p in t:
            if len(p)==4:
                del p[-1]

#-------Executes GA-------
def ga():
    pop=getRndPop() #Initialise population
    # dropFitness(pop) 
    fitness(pop) #Evaluate fitness of each player and team in population
    pop.sort(reverse=True,key=getKey) #Sorts population in decending order of fitness values
    dropFitness(pop) # Remove fitness value from players and teams
    #Execute crossover function with probability at 60% of pop size
    for i in range(1,int(0.6*len(pop))):
        ind1=randInd(pop) #random index in pop
        ind2=randInd(pop) #random index in pop
        offspring= crossover(pop[ind1],pop[ind2]) #Create crossover product of 2 randomly selected teams
        if offspring != True: #offspring is not a duplicate
            del pop[-i] #Remove least fit team from population
            pop.append(offspring) #Append crossover product to pop
    fitness(pop) 
    pop.sort(reverse=True,key=getKey)
    dropFitness(pop)
    #Execute mutation function with probability at 5% of pop size
    for i in range(0,int(0.05*len(pop))):
        t= randInd(pop) #Select index of team randomly
        mutate(pop[t],getRandPlayer()) # mutate player in team 
    fitness(pop)
    pop.sort(reverse=True,key=getKey)
    fitest=pop[0] #Select fittest team in population
    # Add respective players name 
    for p in fitest[:-1]:
        for n in db.session.query(Player.name).filter_by(plid=p[0]).first():
            p.insert(0,n)
    return fitest

@app.route('/rp',methods=["GET"])  
#-----Main Function
def main():
    ft=[] #Fittest teams
    # Terminal Condition (Bounded iterations)
    for i in range(0,5):
        ft.append(ga()) #Execute GA
    ft.sort(reverse=True,key=getKey)
    return jsonify(ft)
