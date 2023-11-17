-- MySQL dump 10.13  Distrib 8.0.35, for Linux (x86_64)
--
-- Host: localhost    Database: metalprod
-- ------------------------------------------------------
-- Server version	8.0.35-0ubuntu0.22.04.1

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
-- Table structure for table `entry_parameter`
--

DROP TABLE IF EXISTS `entry_parameter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `entry_parameter` (
  `id_entry_parameter` int NOT NULL AUTO_INCREMENT,
  `id_equipment` int NOT NULL,
  `id_parameter` int NOT NULL,
  `date_entry` datetime NOT NULL,
  `value` text NOT NULL,
  PRIMARY KEY (`id_entry_parameter`),
  KEY `id_equipment` (`id_equipment`),
  KEY `id_parameter` (`id_parameter`),
  CONSTRAINT `entry_parameter_ibfk_1` FOREIGN KEY (`id_equipment`) REFERENCES `equipment` (`id_equipment`),
  CONSTRAINT `entry_parameter_ibfk_2` FOREIGN KEY (`id_parameter`) REFERENCES `parameter` (`id_parameter`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `entry_parameter`
--

LOCK TABLES `entry_parameter` WRITE;
/*!40000 ALTER TABLE `entry_parameter` DISABLE KEYS */;
INSERT INTO `entry_parameter` VALUES (1,1,1,'2023-12-21 00:00:00','3002'),(2,3,1,'2023-04-07 00:00:00','4243'),(3,2,2,'2023-11-13 00:00:00','324'),(4,2,1,'2023-08-24 00:00:00','3042'),(5,3,2,'2023-10-14 13:22:20','255'),(6,3,2,'2023-10-14 13:22:28','255');
/*!40000 ALTER TABLE `entry_parameter` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-17 20:33:41
