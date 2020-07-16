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
  `adder` varchar(20) DEFAULT NULL,
  KEY `playlisttitle` (`playlisttitle`,`playlistowner`),
  KEY `songtitle` (`songtitle`,`albumtitle`,`artist`),
  KEY `adder` (`adder`),
  CONSTRAINT `addsong_ibfk_1` FOREIGN KEY (`playlisttitle`, `playlistowner`) REFERENCES `playlist` (`title`, `username`) ON DELETE CASCADE,
  CONSTRAINT `addsong_ibfk_2` FOREIGN KEY (`songtitle`, `albumtitle`, `artist`) REFERENCES `song` (`title`, `albumtitle`, `artist`) ON DELETE CASCADE,
  CONSTRAINT `addsong_ibfk_3` FOREIGN KEY (`adder`) REFERENCES `user` (`username`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `addsong`
--

LOCK TABLES `addsong` WRITE;
/*!40000 ALTER TABLE `addsong` DISABLE KEYS */;
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
  CONSTRAINT `adduser_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`) ON DELETE CASCADE,
  CONSTRAINT `adduser_ibfk_2` FOREIGN KEY (`playlisttitle`, `playlistowner`) REFERENCES `playlist` (`title`, `username`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adduser`
--

LOCK TABLES `adduser` WRITE;
/*!40000 ALTER TABLE `adduser` DISABLE KEYS */;
INSERT INTO `adduser` VALUES ('ali','myplaylist4','behrooz');
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
  CONSTRAINT `album_ibfk_1` FOREIGN KEY (`artist`) REFERENCES `artist` (`username`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `album`
--

LOCK TABLES `album` WRITE;
/*!40000 ALTER TABLE `album` DISABLE KEYS */;
INSERT INTO `album` VALUES ('toxicity','ali','alternative metal','2020-07-16');
/*!40000 ALTER TABLE `album` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `artist`
--

DROP TABLE IF EXISTS `artist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artist` (
  `username` varchar(20) NOT NULL,
  `artisticname` varchar(10) DEFAULT NULL,
  `debutyear` int(11) DEFAULT NULL,
  `isapproved` int(11) DEFAULT NULL,
  PRIMARY KEY (`username`),
  KEY `username` (`username`),
  CONSTRAINT `artist_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artist`
--

LOCK TABLES `artist` WRITE;
/*!40000 ALTER TABLE `artist` DISABLE KEYS */;
INSERT INTO `artist` VALUES ('ali','alijfri',2020,1);
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
  CONSTRAINT `creditcard_ibfk_1` FOREIGN KEY (`username`) REFERENCES `listener` (`username`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `creditcard`
--

LOCK TABLES `creditcard` WRITE;
/*!40000 ALTER TABLE `creditcard` DISABLE KEYS */;
INSERT INTO `creditcard` VALUES (1234,'2020-07-17','behrooz');
/*!40000 ALTER TABLE `creditcard` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `follow`
--

DROP TABLE IF EXISTS `follow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `follow` (
  `follower` varchar(20) NOT NULL,
  `following` varchar(20) NOT NULL,
  PRIMARY KEY (`follower`,`following`),
  KEY `follower` (`follower`),
  KEY `following` (`following`),
  CONSTRAINT `follow_ibfk_1` FOREIGN KEY (`follower`) REFERENCES `user` (`username`) ON DELETE CASCADE,
  CONSTRAINT `follow_ibfk_2` FOREIGN KEY (`following`) REFERENCES `user` (`username`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `follow`
--

LOCK TABLES `follow` WRITE;
/*!40000 ALTER TABLE `follow` DISABLE KEYS */;
INSERT INTO `follow` VALUES ('ali','behrooz'),('behrooz','ali');
/*!40000 ALTER TABLE `follow` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `likeplaylist`
--

DROP TABLE IF EXISTS `likeplaylist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `likeplaylist` (
  `username` varchar(20) NOT NULL,
  `playlisttitle` varchar(20) NOT NULL,
  `playlistowner` varchar(20) NOT NULL,
  PRIMARY KEY (`username`,`playlisttitle`,`playlistowner`),
  KEY `username` (`username`),
  KEY `playlisttitle` (`playlisttitle`,`playlistowner`),
  CONSTRAINT `likeplaylist_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`) ON DELETE CASCADE,
  CONSTRAINT `likeplaylist_ibfk_2` FOREIGN KEY (`playlisttitle`, `playlistowner`) REFERENCES `playlist` (`title`, `username`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `likeplaylist`
--

LOCK TABLES `likeplaylist` WRITE;
/*!40000 ALTER TABLE `likeplaylist` DISABLE KEYS */;
INSERT INTO `likeplaylist` VALUES ('ali','myplaylist','behrooz');
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
  CONSTRAINT `likesong_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`) ON DELETE CASCADE,
  CONSTRAINT `likesong_ibfk_2` FOREIGN KEY (`songtitle`, `albumtitle`, `artist`) REFERENCES `song` (`title`, `albumtitle`, `artist`) ON DELETE CASCADE
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
  `username` varchar(20) NOT NULL,
  `firstname` varchar(15) DEFAULT NULL,
  `lastname` varchar(15) DEFAULT NULL,
  `yearofbirth` int(11) DEFAULT NULL,
  PRIMARY KEY (`username`),
  KEY `username` (`username`),
  CONSTRAINT `listener_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `listener`
--

LOCK TABLES `listener` WRITE;
/*!40000 ALTER TABLE `listener` DISABLE KEYS */;
INSERT INTO `listener` VALUES ('behrooz','behrooz','ghamkhar',1999);
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
  `dateplayed` datetime DEFAULT NULL,
  `songtitle` varchar(20) DEFAULT NULL,
  `albumtitle` varchar(20) DEFAULT NULL,
  `artist` varchar(20) DEFAULT NULL,
  KEY `username` (`username`),
  KEY `songtitle` (`songtitle`,`albumtitle`,`artist`),
  CONSTRAINT `play_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`) ON DELETE CASCADE,
  CONSTRAINT `play_ibfk_2` FOREIGN KEY (`songtitle`, `albumtitle`, `artist`) REFERENCES `song` (`title`, `albumtitle`, `artist`) ON DELETE CASCADE
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
  CONSTRAINT `playlist_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `playlist`
--

LOCK TABLES `playlist` WRITE;
/*!40000 ALTER TABLE `playlist` DISABLE KEYS */;
INSERT INTO `playlist` VALUES ('myplaylist','behrooz'),('myplaylist2','behrooz'),('myplaylist3','behrooz'),('myplaylist4','behrooz'),('premiumplaylist','behrooz');
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
  KEY `username` (`username`),
  CONSTRAINT `premium_ibfk_1` FOREIGN KEY (`username`) REFERENCES `listener` (`username`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `premium`
--

LOCK TABLES `premium` WRITE;
/*!40000 ALTER TABLE `premium` DISABLE KEYS */;
INSERT INTO `premium` VALUES (26,'behrooz','2020-07-16');
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
  CONSTRAINT `report_ibfk_1` FOREIGN KEY (`songtitle`, `albumtitle`, `artist`) REFERENCES `song` (`title`, `albumtitle`, `artist`) ON DELETE CASCADE,
  CONSTRAINT `report_ibfk_2` FOREIGN KEY (`username`) REFERENCES `user` (`username`) ON DELETE SET NULL
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
  CONSTRAINT `song_ibfk_1` FOREIGN KEY (`albumtitle`, `artist`) REFERENCES `album` (`title`, `artist`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `song`
--

LOCK TABLES `song` WRITE;
/*!40000 ALTER TABLE `song` DISABLE KEYS */;
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
  `email` varchar(40) DEFAULT NULL,
  `nationality` varchar(20) DEFAULT NULL,
  `password` varchar(35) DEFAULT NULL,
  `personalquestion` varchar(50) DEFAULT NULL,
  `personalanswer` varchar(35) DEFAULT NULL,
  `signupdate` date DEFAULT NULL,
  `salt` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('admin','fumdbprojectadmin@gmail.com','iran','b3ce39987096dade3a1d227b563accc3','What is your favorite color?','c974ac9be4f3113f95ae45ff42a5ebd0','2020-07-16','Y*cIb'),('ali','alijfri99@gmail.com','iran','208feeb4101d53ccdef6544ba5fa8d29','What is your favorite color?','b60434f45f57c75a184477afc9153753','2020-07-16','}q9Xl'),('behrooz','behroozghamkhar@gmail.com','iran','4bea6e34cf6a5dd73b245a997cc0ffa5','What is your favorite color?','117170283903f39c056232d90884a2be','2020-07-16','TD/>C');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'database_project'
--
/*!50106 SET @save_time_zone= @@TIME_ZONE */ ;
/*!50106 DROP EVENT IF EXISTS `checkpremium` */;
DELIMITER ;;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;;
/*!50003 SET character_set_client  = cp850 */ ;;
/*!50003 SET character_set_results = cp850 */ ;;
/*!50003 SET collation_connection  = cp850_general_ci */ ;;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;;
/*!50003 SET @saved_time_zone      = @@time_zone */ ;;
/*!50003 SET time_zone             = 'SYSTEM' */ ;;
/*!50106 CREATE*/ /*!50117 DEFINER=`root`@`localhost`*/ /*!50106 EVENT `checkpremium` ON SCHEDULE EVERY 20 SECOND STARTS '2020-07-16 00:00:00' ON COMPLETION NOT PRESERVE ENABLE DO begin
update premium set duration = duration - 1;
delete from premium where duration = 0;
end */ ;;
/*!50003 SET time_zone             = @saved_time_zone */ ;;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;;
/*!50003 SET character_set_client  = @saved_cs_client */ ;;
/*!50003 SET character_set_results = @saved_cs_results */ ;;
/*!50003 SET collation_connection  = @saved_col_connection */ ;;
DELIMITER ;
/*!50106 SET TIME_ZONE= @save_time_zone */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-07-16 20:52:47
