import os
from difflib import SequenceMatcher
import collections



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
    print ("LS",matches[0][0][13])
    for m in matches:
        team=[]
        for t in m:
            for y in t:
                y[13].translate(None,'\n')

            p=t[0].split(",")
            team.append(p)
        match.append(team)
        c=collections.Counter(match)
        print ("Count:",c)
    print ("match:",match)

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
    print ("MATCH:",sim[10])
    del sim[0]
    print ("Max:",max(sim))
    return winners[10]

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

mb=2# medium bowler
mmb=0
fs=3#fast
ffs=0
of=1#offbreak
oof=0
bm=3#batsman
bbm=0
wk=1#wicket keeper
wwk=0
al=1#allrounder
aal=0
def i_comp(team,player):
    mb=2# medium bowler
    mmb=0
    fs=3#fast
    ffs=0
    of=1#offbreak
    oof=0
    bm=3#batsman
    bbm=0
    wk=1#wicket keeper
    wwk=0
    al=1#allrounder
    aal=0
    ptypes=[]
    print (team)
    print (player)
    for p in team:
        if p[1][-1]=='bowler':
            if 'medium-fast' in p[3] or p[3]=='Right-arm medium':
                mmb+=1
            elif 'fast-medium' in p[3]:
                ffs+=1
        if 'wicketkeeper' in p[1][-1]:
            wwk+=1
        if 'batsman' in p[1][-1]:
            bbm+=1
            if p[3]!=None:
                if 'offbreak' in p[3]:
                    oof+=1
        if p[1][-1]=='allrounder':
            aal+=1
        print ("mmb",mmb)
        print ("ffs",ffs)
        print ("wwk",wwk)
        print ("bbm",bbm)
        print ("oof",oof)
        print ("aal",aal)
    if mmb<mb+1 and wwk<wk+1 and ffs<fs+1 and bbm<bm+1 and oof<of+1 and aal<al+1:
        return True
    else:
        return False
    #     ptypes.append(p[3])
    # count=collections.Counter(ptypes)
    # print "COUNT:",count
    return True
