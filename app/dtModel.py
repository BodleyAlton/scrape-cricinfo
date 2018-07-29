def model_dt(t):
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

    for p in t:
        if p[1]!= None:
            ptype=p[1]
        else:
            ptype=[]
        if p[3][0] != None:
            bowstl=p[3][0]
        else:
            bowstl=[]
        if p[3][1]!=None:
            batstl=p[3][1]
        else:
            batstl=[]
        for i in ptype:
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
        for i in batstl:
            if set(((i.lower()).split(" "))).intersection(set(bat_rh)):
                cbat_rh+=1
            if set(((i.lower()).split(" "))).intersection(set(bat_lh)):
                cbat_lh+=1
        for i in bowstl:
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
    info=[clspin,crspin,cfast,cmedium,cslow,cgoogly,cbat_rh,cbat_lh,cop_bm,cmo_bm,cto_bm,cbowl,cbat,callr,cbow_all,cbat_all,cwk]#,['win_lose','lspin','rspin','fast','medium','slow','googly','bat_rh','bat_lh','op_bm','mo_bm','to_bm','bowl','bats','allr','bow_all','bat_all','wk'])
    entTModel(crspin,cslow,cmo_bm,cbat)
    
def entTModel(crspin,cslow,cmo_bm,cbat):
    if cmo_bm<=1:
        if cbat<=4:
            if crspin <= 3:
                # Lose
                return 0
            else:
                # Win
                return 1
        else:
            if crspin <=3:
                if cslow<=1:
                    # WIN
                    return 1
                else:
                    # LOSE
                    return 0
            else:
                # LOSE
                return 0
    else:
        # WIN
        return 1
