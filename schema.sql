DROP DATABASE IF EXISTS cric;
create database cric;
use cric;
create table player(
plid int not null,
name varchar(50),
born varchar(50),
team varchar(20),
ptype varchar(20),
batStyle varchar(40),
bowStyle varchar(40),
primary key(plid)
);
create table batting(
plid int not null,
mat int,
inns int,
notout int,
runs int,
hs int,
ave float,
bf int,
sr float,
hnds int,
fiftys int,
fours int,
sixs int,
ct int,
st int,
primary key (plid)
foreign key(plid) references player(plid) on delete cascade on update cascade
);
create table bowling(
plid int not null,
mat int,
inns int,
balls int,
runs int,
wkts int,
bbi float,
bbm float,
ave float,
econ float,
sr float,
fourw int,
fivew int,
tens int,
primary key (plid)
foreign key(plid) references player(plid) on delete cascade on update cascade
);