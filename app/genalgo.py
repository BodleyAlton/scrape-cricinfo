import random
from app.dtModel import model_dt
#--------Calculat fitness of player----
def plfitness(p):
    fitness=0
#calculate fitnes of player and append to player.
    ptype=p[1] # player Type
    print("ptype"+str(ptype))
    stats=p[2] # Player Statistics(based on player type)
    bowStl=p[3][0]
    batStyl=p[3][1]
    # Calculate fitness for batsman
    if "batsman" in ptype:
        fitness+=0.4
        batave=stats[0]
        if batave < 20:
            fitness+=0.2
        elif batave>=20 and batave <=25:
            fitness+=0.5
        elif batave>=26 and batave <=30:
            fitness+=0.7
        elif batave>=31 and batave <=40:
            fitness+=0.9
        elif batave > 40:
            fitness+=1
    # Calculate fitness for wicketkeeper
    if "wicketkeeper" in ptype:
        wkts=stats[-1]
        if wkts < 5:
            fitness+=0.1
        elif 5<= wkts<=10:
            fitness+=0.2
        elif 11<= wkts<=20:
            fitness+=0.5
        elif 21<= wkts<=40:
            fitness+=0.6
        elif 41<= wkts<=55:
            fitness+=0.7
        elif 56<= wkts<=70:
            fitness+=0.8
        elif 71<= wkts<=100:
            fitness+=0.9
        elif 101<= wkts<=110:
            fitness+=1
        elif 111<= wkts<=120:
            fitness+=1.2
        elif 121<= wkts<=130:
            fitness+=1.5
        elif 131<= wkts<=145:
            fitness+=1.7
        elif 146<= wkts<=160:
            fitness+=1.8
        elif wkts<160:
            fitness+=2
    # Calculate fitness for bowlerr
    if "bowler" in ptype:
        wkts=stats[-1]
        bave=stats[0]
        if wkts < 5 or bave<15:
            fitness+=0.1
        elif 5<= wkts<=10 or 15<bave<=20:
            fitness+=0.2
        elif 11<= wkts<=20 or 21<=bave<=25:
            fitness+=0.5
        elif 21<= wkts<=40 or 26<=bave<=28:
            fitness+=0.6
        elif 41<= wkts<=55 or 29<=bave<=31:
            fitness+=0.7
        elif 56<= wkts<=70 or 32<=bave<=35:
            fitness+=0.8
        elif 71<= wkts<=100 or 36<=bave<=38:
            fitness+=0.9
        elif 101<= wkts<=110 or 39<=bave<=40:
            fitness+=1
        elif 111<= wkts<=120 or 41<=bave<=43:
            fitness+=1.2
        elif 121<= wkts<=130 or 44<=bave<=46:
            fitness+=1.5
        elif 131<= wkts<=145 or 47<=bave<=49:
            fitness+=1.7
        elif 146<= wkts<=160 or 50<=bave<=52:
            fitness+=1.8
        elif wkts<160 or bave<53:
            fitness+=2
    # Calculate fitness for an allrounder
    if "allrounder" in ptype:
        fitness+=0.4
        batave=stats[0]
        wkts=stats[-1]
        bave=stats[1]
        if batave < 20:
            fitness+=0.2
        elif batave>=20 and batave <=25:
            fitness+=0.5
        elif batave>=26 and batave <=30:
            fitness+=0.7
        elif batave>=31 and batave <=40:
            fitness+=0.9
        elif batave > 40:
            fitness+=1
        if wkts < 5 or bave<15:
            fitness+=0.1
        elif 5<= wkts<=10 or 15<bave<=20:
            fitness+=0.2
        elif 11<= wkts<=20 or 21<=bave<=25:
            fitness+=0.5
        elif 21<= wkts<=40 or 26<=bave<=28:
            fitness+=0.6
        elif 41<= wkts<=55 or 29<=bave<=31:
            fitness+=0.7
        elif 56<= wkts<=70 or 32<=bave<=35:
            fitness+=0.8
        elif 71<= wkts<=100 or 36<=bave<=38:
            fitness+=0.9
        elif 101<= wkts<=110 or 39<=bave<=40:
            fitness+=1
        elif 111<= wkts<=120 or 41<=bave<=43:
            fitness+=1.2
        elif 121<= wkts<=130 or 44<=bave<=46:
            fitness+=1.5
        elif 131<= wkts<=145 or 47<=bave<=49:
            fitness+=1.7
        elif 146<= wkts<=160 or 50<=bave<=52:
            fitness+=1.8
        elif wkts<160 or bave<53:
            fitness+=2
    p.append(fitness)

#------Calculate team fitness (sum of each players fitness)-----
def tmfitness(t):
    tot=0 #running total of fitness of each player
    #Add each players fitness to tot
    for p in t:
        tot+=p[4]
    # call DT model implementation; function shhould return a value which should be added to tot
    tot+= model_dt(t) #add points for composition
    # Apply penalty for constitution
    t.append(tot) #append team fitness to team

#-----Crossover----
# @ Input: 2 Teams
# @Output: 1 Team....Crossover of teams(T1 X T2)
def crossover(T1,T2):
    cpt=random.randint(1,10) #Selects a random cutpoint in range(1,10)
    #Splice list at cpt
    T1R=T1[cpt:]
    T1L=T1[:cpt]
    T2R=T2[cpt:]
    T2L=T2[cpt:]
    # Perform cross over f it will not introduce a duplicate player
    for i in T2R:
        if dups(T1L,i):
            return True
        else:
            T1L.append(i)
    return T1L # Crossover product

#-----Mutator----
#@Input: 1 Team
#@Output: 1 team with random change (change a player in the team)
def mutate(Team,plyr):
    pt=random.randint(0,10) #Select random player in team to be replaced
    if plyr in Team: #Assert Player to be added is not already on team
        return True
    del Team[pt] #remove randomly selected player
    Team.append(plyr) # Add new player to team

#----Determine whether a player is already on a team
def dups(T,pl):
    for p in T:
        if pl[0] in p:
            return True
    return False
