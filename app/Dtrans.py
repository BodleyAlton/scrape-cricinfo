import csv,math
import pandas as pd
import numpy as np

def getData():
    data= pd.read_csv("..//R//Data//match_players.csv")
    data.index=data.index+1
    uptype=data.ptype.unique()
    uptype=uptype[uptype!='NoData']
    uBowS=data.bowStyle.unique()
    uBowS=uBowS[uBowS!='NoData']
    uBatS= data.batStyle.unique()
    uBatS=uBatS[uBatS!='NoData']
    # print(data.head(n=5))
    # print(uptype)
    # print(uBowS)
    # print(uBatS)
    cols=np.concatenate((uptype,uBowS,uBatS),axis=0)
    # print(cols)
    # mod_data=pd.DataFrame(columns=cols)
    # print (mod_data.info())
    return trans_data(data)

def trans_data(data):
    cols=['win_lose','lspin','rspin','fast','medium','slow','googly','bat_rh','bat_lh','op_bm','mo_bm','to_bm','bowl','bats','allr','bow_all','bat_all','wk']
    mod_data=pd.DataFrame(columns=cols)
    # print(data.head(n=5))
    # print(mod_data.info())
    lspin=['left-arm orthodox','legbreak']
    rspin=['left-arm chinaman','offbreak']
    fast=['fast','fast-medium']
    medium=['medium','medium-fast']
    slow=['slow']
    googly=['googly']
    op_bm=['opening']
    mo_bm=['middle-order']
    to_bm=['top-order']
    bowl=['bowler']
    bats=['batsman']
    allr=['allrounder']
    bow_all=['bowling allrounder']
    bat_all=['batting allrounder']
    wk=['wicketkeeper']
    bat_rh=['right-hand']
    bat_lh=['left-hand']
    # print(data[0:11])
    s=0
    r=0
    while s < len(data.index):
        win=0
        clspin=0
        crspin=0
        cfast=0
        cmedium=0
        cslow=0
        cgoogly=0
        cop_bm=0
        cmo_bm=0
        cto_bm=0
        cbow_all=0
        cbat_all=0
        cbowl=0
        cbat=0
        callr=0
        cwk=0
        cbat_rh=0
        cbat_lh=0
        # print("COUNT")
        # print(len(data.index))
        # df=data[int(math.ceil((r*(1.61803398875**5)))):((r*11)+11)
        e=s+11
        print("S: "+str(s))
        print("E: "+str(e))
        df=data[s:e]
        print(df)
        if df['win_lose'][s+1]!='lose':
            win=1
        # print (type(df['ptype']))
        # print(df['ptype'])
        for i in df['ptype']:
            # if any(s in i.lower() for s in wk):
            if set(((i.lower()).split(" "))).intersection(set(wk)):
                cwk+=1
            if set(((i.lower()).split(" "))).intersection(set(bat_all)) or i.lower() in bat_all:
                cbat_all+=1
                cbat+=1
                cbowl+=1
            if set(((i.lower()).split(" "))).intersection(set(bats)):
                cbat+=1
            if set(((i.lower()).split(" "))).intersection(set(bowl)):
                cbowl+=1
            if set(((i.lower()).split(" "))).intersection(set(bow_all)) or i.lower() in bow_all:
                cbow_all+=1
                cbat+=1
                cbowl+=1
            if set(((i.lower()).split(" "))).intersection(set(allr)):
                callr+=1
            if set(((i.lower()).split(" "))).intersection(set(to_bm)):
                cto_bm+=1
            if set(((i.lower()).split(" "))).intersection(set(mo_bm)):
                cmo_bm+=1
            if set(((i.lower()).split(" "))).intersection(set(op_bm)):
                cop_bm+=1
        for i in df['batStyle']:
            if set(((i.lower()).split(" "))).intersection(set(bat_rh)):
                cbat_rh+=1
            if set(((i.lower()).split(" "))).intersection(set(bat_lh)):
                cbat_lh+=1
        for i in df['bowStyle']:
            if set(((i.lower()).split(" "))).intersection(set(lspin)):
                clspin+=1
            if set(((i.lower()).split(" "))).intersection(set(rspin)):
                crspin+=1
            if set(((i.lower()).split(" "))).intersection(set(fast)):
                cfast+=1
            if set(((i.lower()).split(" "))).intersection(set(medium)):
                cmedium+=1
            if set(((i.lower()).split(" "))).intersection(set(slow)):
                cslow+=1
            if set(((i.lower()).split(" "))).intersection(set(googly)):
                cgoogly+=1
        info=[win,clspin,crspin,cfast,cmedium,cslow,cgoogly,cbat_rh,cbat_lh,cop_bm,cmo_bm,cto_bm,cbowl,cbat,callr,cbow_all,cbat_all,cwk]#,['win_lose','lspin','rspin','fast','medium','slow','googly','bat_rh','bat_lh','op_bm','mo_bm','to_bm','bowl','bats','allr','bow_all','bat_all','wk'])
        mod_data.loc[r]=info
        s+=11
        r+=1
    print("MOD_DATA")
    print(mod_data)
    # print(mod_data.info())
    mod_data.to_csv("mod_data.csv",sep=',',header=True,index=False)
    return "ok"
