#Entrophy tree
if mo_bm<=1:
    if bats<=4:
        if rspin <= 3:
            Lose
    else:
        if rspin <=3:
            if slow<=1:
                WIN
            else:
                LOSE
        else:
            LOSE
else:
    WIN

Rule1. If greater than 1 mo_bm THEN Win
Rule2. If up to 1 mo_bm and up to 4 bats and up to 3 rspin THEN Lose
Rule3. If up to 1 mo_bm and up to 4 bats and greater than 3 rspin THEN Win
Rule4. If up to 1 mo_bm and greater than 4 bats and greater than 3 rspin THEN LOSE
Rule5. If up to 1 mo_bm and greater than 4 bats and up to 3 rspin and up to 1 slow THEN Win
Rule6. If up to 1 mo_bm and greater than 4 bats and up to 3 rspin and greater than 1 slow THEN Lose

#Gini Tree
if cmo_bm <=1:
    if cgoogly <=0:
        if cbow_all <= 0:
            if cbat<=4:
                if crspin<=2:
                    LOSE
                elif allr <=3:
                    WIN
                else:
                    Win
            elif cbat_rh <=7:
                if slow <=1:
                    LOSE
                else:
                    LOSE
            else:
                LOSE
