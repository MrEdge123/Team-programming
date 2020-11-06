-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: oj
-- ------------------------------------------------------
-- Server version	8.0.22

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
-- Table structure for table `problemContent`
--

DROP TABLE IF EXISTS `problemContent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `problemContent` (
  `problemId` int DEFAULT NULL,
  `problemTitle` varchar(20) DEFAULT NULL,
  `memoryLimit` int DEFAULT NULL,
  `timeLimit` int DEFAULT NULL,
  `problemDescription` text,
  `inputDescription` text,
  `outputDescription` text,
  UNIQUE KEY `problemId` (`problemId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `problemContent`
--

LOCK TABLES `problemContent` WRITE;
/*!40000 ALTER TABLE `problemContent` DISABLE KEYS */;
INSERT INTO `problemContent` VALUES (0,'计算a+b',65536,1000,'计算a+b的结果\n','输入一个整数a\n','输入一个整数b\n');
/*!40000 ALTER TABLE `problemContent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `problemTestData`
--

DROP TABLE IF EXISTS `problemTestData`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `problemTestData` (
  `problemId` int DEFAULT NULL,
  `number` int DEFAULT NULL,
  `inputData` longtext,
  `outputData` longtext,
  `isExample` tinyint DEFAULT NULL,
  `explanation` text,
  KEY `problemId` (`problemId`),
  CONSTRAINT `problemTestData_ibfk_1` FOREIGN KEY (`problemId`) REFERENCES `problemContent` (`problemId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `problemTestData`
--

LOCK TABLES `problemTestData` WRITE;
/*!40000 ALTER TABLE `problemTestData` DISABLE KEYS */;
INSERT INTO `problemTestData` VALUES (0,0,'1 2\n','3\n',1,'1+2=3'),(0,0,'3 4\n','7\n',1,'3+4=5'),(0,0,'-1 2\n','1\n',0,NULL);
/*!40000 ALTER TABLE `problemTestData` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `submitStatus`
--

DROP TABLE IF EXISTS `submitStatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `submitStatus` (
  `submitTime` datetime DEFAULT NULL,
  `userName` varchar(20) DEFAULT NULL,
  `problemId` int DEFAULT NULL,
  `judgeResult` varchar(20) DEFAULT NULL,
  `usedMemory` int DEFAULT NULL,
  `usedTime` int DEFAULT NULL,
  `language` varchar(10) DEFAULT NULL,
  `code` text,
  KEY `userName` (`userName`),
  KEY `problemId` (`problemId`),
  CONSTRAINT `submitStatus_ibfk_1` FOREIGN KEY (`userName`) REFERENCES `user` (`userName`),
  CONSTRAINT `submitStatus_ibfk_2` FOREIGN KEY (`problemId`) REFERENCES `problemContent` (`problemId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `submitStatus`
--

LOCK TABLES `submitStatus` WRITE;
/*!40000 ALTER TABLE `submitStatus` DISABLE KEYS */;
/*!40000 ALTER TABLE `submitStatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `userId` int DEFAULT NULL,
  `userName` varchar(20) DEFAULT NULL,
  `userNickName` varchar(20) DEFAULT NULL,
  `userPassWord` varchar(20) DEFAULT NULL,
  `userEmail` varchar(50) DEFAULT NULL,
  `isAdmin` tinyint DEFAULT NULL,
  UNIQUE KEY `userId` (`userId`),
  UNIQUE KEY `userName` (`userName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (0,'mredge',NULL,'123456','mredge@163.com',1);
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

-- Dump completed on 2020-11-06 22:19:22
