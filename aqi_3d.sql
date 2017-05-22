-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: localhost    Database: aqidata
-- ------------------------------------------------------
-- Server version	5.7.16-log

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
-- Table structure for table `aqi_3d`
--

DROP TABLE IF EXISTS `aqi_3d`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `aqi_3d` (
  `district_id` int(11) NOT NULL,
  `district_name` varchar(45) NOT NULL,
  `stair` int(11) NOT NULL,
  `aqi_value` int(11) NOT NULL,
  PRIMARY KEY (`district_id`,`district_name`,`stair`,`aqi_value`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aqi_3d`
--

LOCK TABLES `aqi_3d` WRITE;
/*!40000 ALTER TABLE `aqi_3d` DISABLE KEYS */;
INSERT INTO `aqi_3d` VALUES (0,'百讲',1,20),(0,'百讲',2,40),(0,'百讲',3,60),(0,'百讲',4,80),(0,'百讲',5,100),(1,'二教',1,120),(1,'二教',2,100),(1,'二教',3,80),(1,'二教',4,60),(1,'二教',5,40),(2,'南门',1,80),(2,'南门',2,100),(2,'南门',3,120),(2,'南门',4,140),(2,'南门',5,110),(3,'西门',1,70),(3,'西门',2,50),(3,'西门',3,20),(3,'西门',4,80),(3,'西门',5,50),(4,'图书馆',1,100),(4,'图书馆',2,150),(4,'图书馆',3,200),(4,'图书馆',4,150),(4,'图书馆',5,100),(5,'邱德拔',1,130),(5,'邱德拔',2,160),(5,'邱德拔',3,130),(5,'邱德拔',4,160),(5,'邱德拔',5,130),(6,'未名湖',1,100),(6,'未名湖',2,20),(6,'未名湖',3,200),(6,'未名湖',4,250),(6,'未名湖',5,150);
/*!40000 ALTER TABLE `aqi_3d` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `aqi_average`
--

DROP TABLE IF EXISTS `aqi_average`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `aqi_average` (
  `district_id` int(11) NOT NULL,
  `district_name` varchar(45) NOT NULL,
  `CO` int(11) NOT NULL,
  `NO` int(11) NOT NULL,
  `SO2` int(11) NOT NULL,
  `O3` int(11) NOT NULL,
  `PM1` int(11) NOT NULL,
  `PM2` int(11) NOT NULL,
  `PM10` int(11) NOT NULL,
  PRIMARY KEY (`district_id`,`district_name`,`CO`,`NO`,`SO2`,`O3`,`PM1`,`PM2`,`PM10`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aqi_average`
--

LOCK TABLES `aqi_average` WRITE;
/*!40000 ALTER TABLE `aqi_average` DISABLE KEYS */;
INSERT INTO `aqi_average` VALUES (0,'百讲',12,12,32,312,2,31,1),(1,'二教',4,3,34,4,32,5,23),(2,'南门',3,4,1,2,3,4,3),(3,'西门',5,45,34,567,3,12,21),(4,'图书馆',6,6,4,76,6,6,5),(5,'邱德拔',2,3,4,6,4,6,0),(6,'未名湖',5,4,3,2,1,9,0);
/*!40000 ALTER TABLE `aqi_average` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `aqi_now`
--

DROP TABLE IF EXISTS `aqi_now`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `aqi_now` (
  `district_id` int(11) NOT NULL,
  `district_name` varchar(45) NOT NULL,
  `CO` int(11) NOT NULL,
  `NO` int(11) NOT NULL,
  `SO2` int(11) NOT NULL,
  `O3` int(11) NOT NULL,
  `PM1` int(11) NOT NULL,
  `PM2` int(11) NOT NULL,
  `PM10` int(11) NOT NULL,
  PRIMARY KEY (`district_id`,`district_name`,`CO`,`NO`,`SO2`,`O3`,`PM1`,`PM2`,`PM10`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aqi_now`
--

LOCK TABLES `aqi_now` WRITE;
/*!40000 ALTER TABLE `aqi_now` DISABLE KEYS */;
INSERT INTO `aqi_now` VALUES (0,'百讲',0,0,0,0,0,0,0),(1,'二教',1,1,1,1,1,1,1),(2,'南门',2,2,2,2,2,2,2),(3,'西门',3,3,3,3,3,3,3),(4,'图书馆',4,4,4,4,4,4,4),(5,'邱德拔',5,5,5,5,5,5,5),(6,'未名湖',6,6,6,6,6,6,6);
/*!40000 ALTER TABLE `aqi_now` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `repository`
--

DROP TABLE IF EXISTS `repository`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `repository` (
  `district_id` int(11) NOT NULL,
  `district_name` varchar(45) NOT NULL,
  PRIMARY KEY (`district_id`,`district_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `repository`
--

LOCK TABLES `repository` WRITE;
/*!40000 ALTER TABLE `repository` DISABLE KEYS */;
INSERT INTO `repository` VALUES (0,'百讲'),(1,'二教'),(2,'南门'),(3,'西门'),(4,'图书馆'),(5,'邱德拔'),(6,'未名湖');
/*!40000 ALTER TABLE `repository` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-05-22 15:14:44
