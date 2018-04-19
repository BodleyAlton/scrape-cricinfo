from . import db,app

class Player(db.Model):
    # id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    plid = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    born = db.Column(db.String(50), unique=True)
    team = db.Column(db.String(20))
    ptype=db.Column(db.String(20))
    batStyle=db.Column(db.String(40))
    bowStyle=db.Column(db.String(40))
    
    
    def __init__(self,plid,name,born,team,ptype,batStyle,bowStyle):
        # self.id=id
        self.plid=plid
        self.name=name
        self.born=born
        self.team=team
        self.ptype=ptype
        self.batStyle=batStyle
        self.bowStyle=bowStyle

class Batting(db.Model):
    plid = db.Column(db.Integer,db.ForeignKey('player.plid'),primary_key=True)
    mat = db.Column(db.Integer)
    inns = db.Column(db.Integer)
    notout = db.Column(db.Integer)
    runs = db.Column(db.Integer)
    hs = db.Column(db.Integer)
    ave = db.Column(db.Float)
    bf = db.Column(db.Integer)
    sr = db.Column(db.Float)
    hnds = db.Column(db.Integer)
    fiftys = db.Column(db.Integer)
    fours = db.Column(db.Integer)
    sixs = db.Column(db.Integer)
    ct = db.Column(db.Integer)
    st = db.Column(db.Integer)
    
    def __init__(self,plid,mat,inns,notout,runs,hs,ave,bf,sr,hnds,fiftys,fours,sixs,ct,st):
        self.plid=plid
        self.mat=mat
        self.inns=inns
        self.notout=notout
        self.runs=runs
        self.hs=hs
        self.ave=ave
        self.bf=bf
        self.sr=sr
        self.hnds=hnds
        self.fiftys=fiftys
        self.fours=fours
        self.sixs=sixs
        self.ct=ct
        self.st=st

class Bowling(db.Model):
    plid = db.Column(db.Integer,db.ForeignKey('player.plid'),primary_key=True) 
    mat = db.Column(db.Integer)
    inns = db.Column(db.Integer)
    balls = db.Column(db.Integer)
    runs = db.Column(db.Integer)
    wkts = db.Column(db.Integer)
    bbi = db.Column(db.Float)
    bbm = db.Column(db.Float)
    ave = db.Column(db.Float)
    econ = db.Column(db.Float)
    sr = db.Column(db.Float)
    fourw = db.Column(db.Integer)
    fivew = db.Column(db.Integer)
    tens = db.Column(db.Integer)

    def __init__(self,plid,mat,inns,balls,runs,wkts,bbi,bbm,ave,econ,sr,fourw,fivew,tens):
        self.plid = plid 
        self.mat  = mat
        self.inns  = inns
        self.balls  = balls
        self.runs = runs 
        self.wkts = wkts
        self.bbi = bbi 
        self.bbm = bbm 
        self.ave = ave 
        self.econ = econ 
        self.sr = sr 
        self.fourw = fourw 
        self.fivew = fivew 
        self.tens =tens
