-- MySQL dump 10.13  Distrib 5.5.57, for debian-linux-gnu (x86_64)
--
-- Host: 0.0.0.0    Database: cric
-- ------------------------------------------------------
-- Server version	5.5.57-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `batting`
--
DROP DATABASE IF EXISTS cric;
create database cric;
use cric;
DROP TABLE IF EXISTS `batting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `batting` (
  `plid` int(11) NOT NULL,
  `mat` int(11) DEFAULT NULL,
  `inns` int(11) DEFAULT NULL,
  `notout` int(11) DEFAULT NULL,
  `runs` int(11) DEFAULT NULL,
  `hs` int(11) DEFAULT NULL,
  `ave` float DEFAULT NULL,
  `bf` int(11) DEFAULT NULL,
  `sr` float DEFAULT NULL,
  `hnds` int(11) DEFAULT NULL,
  `fiftys` int(11) DEFAULT NULL,
  `fours` int(11) DEFAULT NULL,
  `sixs` int(11) DEFAULT NULL,
  `ct` int(11) DEFAULT NULL,
  `st` int(11) DEFAULT NULL,
  PRIMARY KEY (`plid`),
  CONSTRAINT `batting_ibfk_1` FOREIGN KEY (`plid`) REFERENCES `player` (`plid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `batting`
--

LOCK TABLES `batting` WRITE;
/*!40000 ALTER TABLE `batting` DISABLE KEYS */;
INSERT INTO `batting` VALUES (51248,47,30,7,182,31,7.91,240,75.83,0,0,19,3,9,0),(51862,25,25,0,354,54,14.16,549,64.48,0,2,42,7,5,3),(51880,281,276,17,9585,215,37,11169,85.81,23,48,1063,267,119,0),(52917,139,110,22,2200,169,25,2738,80.35,2,8,165,31,181,7),(52983,199,188,26,5472,133,33.77,7248,75.49,10,30,510,116,50,0),(53191,90,42,9,278,43,8.42,323,86.06,0,0,31,5,20,0),(230549,26,22,1,529,91,25.19,761,69.51,0,4,44,10,3,0),(230558,65,45,12,363,36,11,441,82.31,0,0,36,12,14,0),(230559,101,95,6,2289,119,25.71,2464,92.89,3,9,145,110,53,0),(252932,39,37,0,897,83,24.24,1144,78.4,0,8,102,12,10,0),(274921,7,4,1,19,10,6.33,26,73.07,0,0,1,0,1,0),(277472,94,91,10,2595,124,32.03,3714,69.87,3,17,222,55,30,0),(314615,28,25,2,524,54,22.78,764,68.58,0,3,43,9,7,0),(315586,9,8,0,53,19,6.62,86,61.62,0,0,7,0,9,1),(315594,33,26,10,298,44,18.62,323,92.26,0,0,28,6,13,0),(333066,48,48,0,1283,130,26.72,1531,83.8,2,4,140,35,21,1),(341593,28,17,5,90,16,7.5,158,56.96,0,0,10,0,4,0),(348024,10,10,0,278,78,27.8,483,57.55,0,1,15,0,3,0),(348054,1,1,1,38,38,0,27,140.74,0,0,4,0,0,0),(391485,77,62,16,1229,99,26.71,1281,95.94,0,6,90,41,31,0),(391832,8,6,1,68,33,13.6,106,64.15,0,0,4,0,4,0),(431901,32,29,1,968,176,34.57,1147,84.39,2,3,101,22,11,0),(443150,7,6,0,138,46,23,192,71.87,0,0,20,0,1,0),(446101,18,13,7,21,12,3.5,53,39.62,0,0,1,0,1,0),(450075,8,5,4,19,16,19,27,70.37,0,0,1,0,0,0),(457249,28,26,2,323,33,13.45,391,82.6,0,0,20,12,9,0),(556749,11,3,1,10,5,5,27,37.03,0,0,1,0,1,0),(581379,33,30,3,1020,101,37.77,1533,66.53,1,5,65,18,32,4),(670031,14,6,3,74,27,24.66,95,77.89,0,0,4,2,5,0),(820351,23,20,2,475,101,26.38,556,85.43,1,1,25,25,11,0);
/*!40000 ALTER TABLE `batting` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bowling`
--

DROP TABLE IF EXISTS `bowling`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bowling` (
  `plid` int(11) NOT NULL,
  `mat` int(11) DEFAULT NULL,
  `inns` int(11) DEFAULT NULL,
  `balls` int(11) DEFAULT NULL,
  `runs` int(11) DEFAULT NULL,
  `wkts` int(11) DEFAULT NULL,
  `bbi` float DEFAULT NULL,
  `bbm` float DEFAULT NULL,
  `ave` float DEFAULT NULL,
  `econ` float DEFAULT NULL,
  `sr` float DEFAULT NULL,
  `fourw` int(11) DEFAULT NULL,
  `fivew` int(11) DEFAULT NULL,
  `tens` int(11) DEFAULT NULL,
  PRIMARY KEY (`plid`),
  CONSTRAINT `bowling_ibfk_1` FOREIGN KEY (`plid`) REFERENCES `player` (`plid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bowling`
--

LOCK TABLES `bowling` WRITE;
/*!40000 ALTER TABLE `bowling` DISABLE KEYS */;
INSERT INTO `bowling` VALUES (51248,47,46,2387,1913,39,0.222222,0.222222,49.05,4.8,61.2,3,0,0),(51862,25,3,28,26,0,0,0,0,5.57,0,0,0,0),(51880,281,192,7268,5791,165,0.108696,0.108696,35.09,4.78,44,3,1,0),(52917,139,0,0,0,0,0,0,0,0,0,0,0,0),(52983,199,130,5009,4040,85,0.12,0.12,47.52,4.83,58.9,0,0,0),(53191,90,88,4341,3780,128,0.104167,0.104167,29.53,5.22,33.9,3,1,0),(230549,26,7,134,116,0,0,0,0,5.19,0,0,0,0),(230558,65,65,3540,2435,92,0.222222,0.222222,26.46,4.12,38.4,4,2,0),(230559,101,70,2044,1956,50,0.111111,0.111111,39.12,5.74,40.8,0,0,0),(252932,39,0,0,0,0,0,0,0,0,0,0,0,0),(274921,7,7,331,271,8,0.075,0.075,33.87,4.91,41.3,0,0,0),(277472,94,0,0,0,0,0,0,0,0,0,0,0,0),(314615,28,11,124,141,3,0.142857,0.142857,47,6.82,41.3,0,0,0),(315586,9,0,0,0,0,0,0,0,0,0,0,0,0),(315594,33,31,1540,1293,33,0.0645161,0.0645161,39.18,5.03,46.6,1,0,0),(333066,48,1,5,12,0,0,0,0,14.4,0,0,0,0),(341593,28,28,1416,1124,31,0.1,0.1,36.25,4.76,45.6,0,0,0),(348024,10,5,152,140,1,0.0178571,0.0178571,140,5.52,152,0,0,0),(348054,1,0,0,0,0,0,0,0,0,0,0,0,0),(391485,77,76,3686,3316,106,0.185185,0.185185,31.28,5.39,34.7,4,2,0),(391832,8,4,41,48,1,0.0666667,0.0666667,48,7.02,41,0,0,0),(431901,32,0,0,0,0,0,0,0,0,0,0,0,0),(443150,7,0,0,0,0,0,0,0,0,0,0,0,0),(446101,18,18,839,782,23,0.176471,0.176471,34,5.59,36.4,0,0,0),(450075,8,7,330,293,9,0.0930233,0.0930233,32.55,5.32,36.6,1,0,0),(457249,28,27,1284,1163,26,0.185185,0.185185,44.73,5.43,49.3,1,1,0),(556749,11,9,450,474,9,0.0365854,0.0365854,52.66,6.32,50,0,0,0),(581379,33,0,0,0,0,0,0,0,0,0,0,0,0),(670031,14,13,661,706,23,0.0892857,0.0892857,30.69,6.4,28.7,1,1,0),(820351,23,9,152,151,1,0.0263158,0.0263158,151,5.96,152,0,0,0);
/*!40000 ALTER TABLE `bowling` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `player`
--

DROP TABLE IF EXISTS `player`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `player` (
  `plid` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `born` varchar(50) DEFAULT NULL,
  `team` varchar(20) DEFAULT NULL,
  `ptype` varchar(20) DEFAULT NULL,
  `batStyle` varchar(40) DEFAULT NULL,
  `bowStyle` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`plid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player`
--

LOCK TABLES `player` WRITE;
/*!40000 ALTER TABLE `player` DISABLE KEYS */;
INSERT INTO `player` VALUES (51248,'Sulieman Jamaal Benn','July 22, 1981, Haynesville, St James, Barbados ','West Indies,','Bowler','Left-hand bat','Slow left-arm orthodox'),(51862,'Andre David Stephon Fletcher','November 28, 1987, La Tante, Grenada ','West Indies,','Wicketkeeper batsman','Right-hand bat','Right-arm medium-fast, Legbreak'),(51880,'Christopher Henry Gayle','September 21, 1979, Kingston, Jamaica ','West Indies,','Allrounder','Left-hand bat','Right-arm offbreak'),(52917,'Denesh Ramdin','March 13, 1985, Couva, Trinidad ','West Indies,','Wicketkeeper batsman','Right-hand bat',NULL),(52983,'Marlon Nathaniel Samuels','February 5, 1981, Kingston, Jamaica ','West Indies,','Top-order batsman','Right-hand bat','Right-arm offbreak'),(53191,'Jerome Everton Taylor','June 22, 1984, St Elizabeth, Jamaica ','West Indies,','Bowler','Right-hand bat','Right-arm fast'),(230549,'Jason Nazimuddin Mohammed','September 23, 1986, Trinidad ','Guyana Amazon Warrio','Batsman','Right-hand bat','Right-arm offbreak'),(230558,'Sunil Philip Narine','May 26, 1988, Arima, Trinidad & Tobago ','West Indies,','Bowler','Left-hand bat','Right-arm offbreak'),(230559,'Kieron Adrian Pollard','May 12, 1987, Tacarigua, Trinidad ','West Indies,','Allrounder','Right-hand bat','Right-arm medium-fast'),(252932,'Kieran Omar Akeem Powell','March 6, 1990, Nevis ','West Indies,','Opening batsman','Left-hand bat','Right-arm medium, Right-arm offbreak'),(274921,'Veerasammy Permaul','August 11, 1989, Guyana ','West Indies,','Bowler','Right-hand bat','Slow left-arm orthodox'),(277472,'Darren Michael Bravo','February 6, 1989, Trinidad ','West Indies,','Top-order batsman','Left-hand bat','Right-arm medium-fast'),(314615,'Jonathan Lyndon Carter','November 16, 1987, Barbados ','Barbados,','Allrounder','Left-hand bat','Right-arm medium'),(315586,'Chadwick Antonio Kirkpatrick Walton','July 3, 1985, Jamaica ','West Indies,','Wicketkeeper batsman','Right-hand bat',NULL),(315594,'Ashley Renaldo Nurse','December 22, 1988, Gibbons, Christ Church, Barbado','West Indies,','Bowler','Right-hand bat','Right-arm offbreak'),(333066,'Johnson Charles','January 14, 1989, St Lucia ','West Indies,','Wicketkeeper batsman','Right-hand bat',NULL),(341593,'Devendra Bishoo','November 6, 1985, New Amsterdam, Berbice, Guyana ','West Indies,','Bowler','Left-hand bat','Legbreak'),(348024,'Kraigg Clairmonte Brathwaite','December 1, 1992, Black Rock, St Michael, Barbados','West Indies,','Opening batsman','Right-hand bat','Right-arm offbreak'),(348054,'Sunil Walford Ambris','March 23, 1993, St Vincent, Windward Islands ','West Indies,','Opening batsman','Right-hand bat',NULL),(391485,'Jason Omar Holder','November 5, 1991, Barbados ','West Indies,','Bowling allrounder','Right-hand bat','Right-arm medium-fast'),(391832,'Roston Lamar Chase','March 22, 1992, Barbados ','West Indies,','Allrounder','Right-hand bat','Right-arm offbreak'),(431901,'Evin Lewis','December 27, 1991, Port of Spain, Trinidad ','Barisal Bulls,','Opening batsman','Left-hand bat',NULL),(443150,'Kyle Antonio Hope','November 20, 1988, Barbados ','West Indies,','Middle-order batsman','Right-hand bat','Right-arm offbreak'),(446101,'Shannon Terry Gabriel','April 28, 1988, Trinidad ','West Indies,','Bowler','Right-hand bat','Right-arm fast-medium'),(450075,'Kesrick Omari Kenal Williams','January 17, 1990, Spring Village, St. Vincent and ','West Indies,','Bowler','Right-hand bat','Right-arm fast-medium'),(457249,'Carlos Ricardo Brathwaite','July 18, 1988, Barbados ','West Indies,','Allrounder','Right-hand bat','Right-arm fast-medium'),(556749,'Miguel Lamar Cummins','September 5, 1990, St. Michael, Barbados ','West Indies,','Bowler','Left-hand bat','Right-arm fast-medium'),(581379,'Shai Diego Hope','November 10, 1993, Barbados ','West Indies,','Wicketkeeper batsman','Right-hand bat',NULL),(670031,'Alzarri Shaheim Joseph','November 20, 1996, Antigua ','West Indians,','Bowler','Right-hand bat','Right-arm fast-medium'),(820351,'Rovman Powell','July 23, 1993, Jamaica ','West Indies,','Batsman','Right-hand bat','Right-arm medium-fast');
/*!40000 ALTER TABLE `player` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-09 16:19:42
