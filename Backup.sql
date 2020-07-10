-- MySQL dump 10.13  Distrib 8.0.17, for Win64 (x86_64)
--
-- Host: localhost    Database: database_project
-- ------------------------------------------------------
-- Server version	8.0.17

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `addsong`
--

DROP TABLE IF EXISTS `addsong`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `addsong` (
  `dateadded` date DEFAULT NULL,
  `playlisttitle` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `playlistowner` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `songtitle` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `albumtitle` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `artist` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  KEY `playlisttitle` (`playlisttitle`,`playlistowner`),
  KEY `songtitle` (`songtitle`,`albumtitle`,`artist`),
  CONSTRAINT `addsong_ibfk_1` FOREIGN KEY (`playlisttitle`, `playlistowner`) REFERENCES `playlist` (`title`, `username`),
  CONSTRAINT `addsong_ibfk_2` FOREIGN KEY (`songtitle`, `albumtitle`, `artist`) REFERENCES `song` (`title`, `albumtitle`, `artist`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `addsong`
--

LOCK TABLES `addsong` WRITE;
/*!40000 ALTER TABLE `addsong` DISABLE KEYS */;
INSERT INTO `addsong` VALUES ('2001-05-02','myplaylist','behrouz','bliever','evolve','ali'),('2001-05-02','myplaylist','behrouz','gun','evolve','ali');
/*!40000 ALTER TABLE `addsong` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `adduser`
--

DROP TABLE IF EXISTS `adduser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `adduser` (
  `username` varchar(20) DEFAULT NULL,
  `playlisttitle` varchar(20) DEFAULT NULL,
  `playlistowner` varchar(20) DEFAULT NULL,
  KEY `username` (`username`),
  KEY `playlisttitle` (`playlisttitle`,`playlistowner`),
  CONSTRAINT `adduser_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`),
  CONSTRAINT `adduser_ibfk_2` FOREIGN KEY (`playlisttitle`, `playlistowner`) REFERENCES `playlist` (`title`, `username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adduser`
--

LOCK TABLES `adduser` WRITE;
/*!40000 ALTER TABLE `adduser` DISABLE KEYS */;
/*!40000 ALTER TABLE `adduser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `album`
--

DROP TABLE IF EXISTS `album`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `album` (
  `title` varchar(20) NOT NULL,
  `artist` varchar(20) NOT NULL,
  `genre` varchar(20) DEFAULT NULL,
  `releasedate` date DEFAULT NULL,
  PRIMARY KEY (`title`,`artist`),
  KEY `artist` (`artist`),
  CONSTRAINT `album_ibfk_1` FOREIGN KEY (`artist`) REFERENCES `artist` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `album`
--

LOCK TABLES `album` WRITE;
/*!40000 ALTER TABLE `album` DISABLE KEYS */;
INSERT INTO `album` VALUES ('evolve','ali','pop-rock','2001-05-02');
/*!40000 ALTER TABLE `album` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `artist`
--

DROP TABLE IF EXISTS `artist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artist` (
  `username` varchar(20) DEFAULT NULL,
  `artisticname` varchar(10) DEFAULT NULL,
  `debutyear` int(11) DEFAULT NULL,
  `isapproved` int(11) DEFAULT NULL,
  KEY `username` (`username`),
  CONSTRAINT `artist_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artist`
--

LOCK TABLES `artist` WRITE;
/*!40000 ALTER TABLE `artist` DISABLE KEYS */;
INSERT INTO `artist` VALUES ('behrouz','yegane',1996,1),('ali','dragons',1900,1);
/*!40000 ALTER TABLE `artist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `creditcard`
--

DROP TABLE IF EXISTS `creditcard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `creditcard` (
  `number` int(11) NOT NULL,
  `expdate` date DEFAULT NULL,
  `username` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`number`),
  KEY `username` (`username`),
  CONSTRAINT `creditcard_ibfk_1` FOREIGN KEY (`username`) REFERENCES `listener` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `creditcard`
--

LOCK TABLES `creditcard` WRITE;
/*!40000 ALTER TABLE `creditcard` DISABLE KEYS */;
/*!40000 ALTER TABLE `creditcard` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `follow`
--

DROP TABLE IF EXISTS `follow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `follow` (
  `follower` varchar(20) DEFAULT NULL,
  `following` varchar(20) DEFAULT NULL,
  KEY `follower` (`follower`),
  KEY `following` (`following`),
  CONSTRAINT `follow_ibfk_1` FOREIGN KEY (`follower`) REFERENCES `user` (`username`),
  CONSTRAINT `follow_ibfk_2` FOREIGN KEY (`following`) REFERENCES `user` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `follow`
--

LOCK TABLES `follow` WRITE;
/*!40000 ALTER TABLE `follow` DISABLE KEYS */;
INSERT INTO `follow` VALUES ('ali','reza'),('ali','behrouz'),('reza','behrouz'),('reza','ali'),('behrouz','ali'),('behrouz','reza'),('ali','ahmad'),('reza','ahmad');
/*!40000 ALTER TABLE `follow` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `likeplaylist`
--

DROP TABLE IF EXISTS `likeplaylist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `likeplaylist` (
  `username` varchar(20) DEFAULT NULL,
  `playlisttitle` varchar(20) DEFAULT NULL,
  `playlistowner` varchar(20) DEFAULT NULL,
  KEY `username` (`username`),
  KEY `playlisttitle` (`playlisttitle`,`playlistowner`),
  CONSTRAINT `likeplaylist_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`),
  CONSTRAINT `likeplaylist_ibfk_2` FOREIGN KEY (`playlisttitle`, `playlistowner`) REFERENCES `playlist` (`title`, `username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `likeplaylist`
--

LOCK TABLES `likeplaylist` WRITE;
/*!40000 ALTER TABLE `likeplaylist` DISABLE KEYS */;
/*!40000 ALTER TABLE `likeplaylist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `likesong`
--

DROP TABLE IF EXISTS `likesong`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `likesong` (
  `username` varchar(20) DEFAULT NULL,
  `songtitle` varchar(20) DEFAULT NULL,
  `albumtitle` varchar(20) DEFAULT NULL,
  `artist` varchar(20) DEFAULT NULL,
  KEY `username` (`username`),
  KEY `songtitle` (`songtitle`,`albumtitle`,`artist`),
  CONSTRAINT `likesong_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`),
  CONSTRAINT `likesong_ibfk_2` FOREIGN KEY (`songtitle`, `albumtitle`, `artist`) REFERENCES `song` (`title`, `albumtitle`, `artist`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `likesong`
--

LOCK TABLES `likesong` WRITE;
/*!40000 ALTER TABLE `likesong` DISABLE KEYS */;
/*!40000 ALTER TABLE `likesong` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `listener`
--

DROP TABLE IF EXISTS `listener`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `listener` (
  `username` varchar(20) DEFAULT NULL,
  `firstname` varchar(15) DEFAULT NULL,
  `lastname` varchar(15) DEFAULT NULL,
  `yearofbirth` int(11) DEFAULT NULL,
  KEY `username` (`username`),
  CONSTRAINT `listener_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `listener`
--

LOCK TABLES `listener` WRITE;
/*!40000 ALTER TABLE `listener` DISABLE KEYS */;
/*!40000 ALTER TABLE `listener` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `play`
--

DROP TABLE IF EXISTS `play`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `play` (
  `username` varchar(20) DEFAULT NULL,
  `dateplayed` date DEFAULT NULL,
  `songtitle` varchar(20) DEFAULT NULL,
  `albumtitle` varchar(20) DEFAULT NULL,
  `artist` varchar(20) DEFAULT NULL,
  KEY `username` (`username`),
  KEY `songtitle` (`songtitle`,`albumtitle`,`artist`),
  CONSTRAINT `play_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`),
  CONSTRAINT `play_ibfk_2` FOREIGN KEY (`songtitle`, `albumtitle`, `artist`) REFERENCES `song` (`title`, `albumtitle`, `artist`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `play`
--

LOCK TABLES `play` WRITE;
/*!40000 ALTER TABLE `play` DISABLE KEYS */;
/*!40000 ALTER TABLE `play` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `playlist`
--

DROP TABLE IF EXISTS `playlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `playlist` (
  `title` varchar(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  PRIMARY KEY (`title`,`username`),
  KEY `username` (`username`),
  CONSTRAINT `playlist_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `playlist`
--

LOCK TABLES `playlist` WRITE;
/*!40000 ALTER TABLE `playlist` DISABLE KEYS */;
INSERT INTO `playlist` VALUES ('myplaylist','behrouz');
/*!40000 ALTER TABLE `playlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `premium`
--

DROP TABLE IF EXISTS `premium`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `premium` (
  `duration` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `subdate` date DEFAULT NULL,
  PRIMARY KEY (`duration`,`username`),
  KEY `username` (`username`),
  CONSTRAINT `premium_ibfk_1` FOREIGN KEY (`username`) REFERENCES `listener` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `premium`
--

LOCK TABLES `premium` WRITE;
/*!40000 ALTER TABLE `premium` DISABLE KEYS */;
/*!40000 ALTER TABLE `premium` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `report`
--

DROP TABLE IF EXISTS `report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `report` (
  `songtitle` varchar(20) DEFAULT NULL,
  `albumtitle` varchar(20) DEFAULT NULL,
  `artist` varchar(20) DEFAULT NULL,
  `username` varchar(20) DEFAULT NULL,
  KEY `songtitle` (`songtitle`,`albumtitle`,`artist`),
  KEY `username` (`username`),
  CONSTRAINT `report_ibfk_1` FOREIGN KEY (`songtitle`, `albumtitle`, `artist`) REFERENCES `song` (`title`, `albumtitle`, `artist`),
  CONSTRAINT `report_ibfk_2` FOREIGN KEY (`username`) REFERENCES `user` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `report`
--

LOCK TABLES `report` WRITE;
/*!40000 ALTER TABLE `report` DISABLE KEYS */;
/*!40000 ALTER TABLE `report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `song`
--

DROP TABLE IF EXISTS `song`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `song` (
  `title` varchar(20) NOT NULL,
  `albumtitle` varchar(20) NOT NULL,
  `artist` varchar(20) NOT NULL,
  `length` int(11) DEFAULT NULL,
  PRIMARY KEY (`title`,`albumtitle`,`artist`),
  KEY `albumtitle` (`albumtitle`,`artist`),
  CONSTRAINT `song_ibfk_1` FOREIGN KEY (`albumtitle`, `artist`) REFERENCES `album` (`title`, `artist`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `song`
--

LOCK TABLES `song` WRITE;
/*!40000 ALTER TABLE `song` DISABLE KEYS */;
INSERT INTO `song` VALUES ('bliever','evolve','ali',204),('gun','evolve','ali',204),('guns','evolve','ali',224);
/*!40000 ALTER TABLE `song` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `username` varchar(20) NOT NULL,
  `email` varchar(20) DEFAULT NULL,
  `nationality` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `personalquestion` varchar(20) DEFAULT NULL,
  `personalanswer` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('ahmad','2@gma','usa','21','www','qqq'),('ali','a@gmail.com','iran','123','que','ans'),('behrouz','behrooz@gmail.com','iran','pss','ques','answ'),('reza','r@gmail','zimbabwe','12','qw','ssw');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-07-11  3:57:18
