import os
from difflib import SequenceMatcher
import collections

mb=2# medium bowler
fs=4#fast
bm=3#batsman
wk=1#wicket keeper
al=1#allrounder
    
def naive_comp():
    matchlst=[]
    for file in os.listdir(os.getcwd()+"/app/data"):
        with open(os.getcwd()+"/app/data/"+file, 'r') as matches:
            next(matches)
            team=[]
            for match in matches:
                team.append([match])
            matchlst.append(team)    
    return matchlst
    
def convert(matches):
    match=[]
    print "LS",matches[0][0][13]
    for m in matches:
        team=[]
        for t in m:
            for y in t:
                y[13].translate(None,'\n')
                
            p=t[0].split(",")
            team.append(p)
        match.append(team)
        c=collections.Counter(match)
        print "Count:",c
    print "match:",match

def n_comp(matches):
    sim=[]
    winners=[]
    for m in matches:
        for t in m:
            if t[0][0]=="1":
                t[0].translate(None,"\n")
                winners.append(t[0])
    # c=collections.Counter(winners)
    # print "count:",c
    # print "C",len(winners)
    # print type(winners)
    # print winners
    for m in winners:
        sim.append(similar(winners[0],m))
    print "MATCH:",sim[10]
    del sim[0]
    print "Max:",max(sim)
    return winners[10]

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def i_comp(player):
    global mb
    global fs
    global bm
    global wk
    global al
    ptype=player[1][0]
    b_style=player[3]
    if ptype=="bowler":
        if ("medium" in b_style) & (mb>0):
            mb-=1
            print "mb:",mb
            return True
        elif ("fast" in b_style) & (fs>0):
            fs-=1
            print "fs:",fs
            return True
    elif (ptype=="batsman")&(bm>0):
        bm-=1
        print "bm:",bm
        return True
    elif ("wicketkeeper" in ptype)&(wk>0):
        wk-=1
        print "wk:",wk
        return True
    elif (ptype=="allrounder")&(al>0):
        al-=1
        print "al:",al
        return True
    else:
        return False
    # print "PLAYER:",player
    # return True
    