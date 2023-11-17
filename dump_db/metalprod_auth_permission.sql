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
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=109 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add client',7,'add_client'),(26,'Can change client',7,'change_client'),(27,'Can delete client',7,'delete_client'),(28,'Can view client',7,'view_client'),(29,'Can add aaaa',8,'add_aaaa'),(30,'Can change aaaa',8,'change_aaaa'),(31,'Can delete aaaa',8,'delete_aaaa'),(32,'Can view aaaa',8,'view_aaaa'),(33,'Can add post',9,'add_post'),(34,'Can change post',9,'change_post'),(35,'Can delete post',9,'delete_post'),(36,'Can view post',9,'view_post'),(37,'Can add state contract',10,'add_statecontract'),(38,'Can change state contract',10,'change_statecontract'),(39,'Can delete state contract',10,'delete_statecontract'),(40,'Can view state contract',10,'view_statecontract'),(41,'Can add employee',11,'add_employee'),(42,'Can change employee',11,'change_employee'),(43,'Can delete employee',11,'delete_employee'),(44,'Can view employee',11,'view_employee'),(45,'Can add contract',12,'add_contract'),(46,'Can change contract',12,'change_contract'),(47,'Can delete contract',12,'delete_contract'),(48,'Can view contract',12,'view_contract'),(49,'Can add warehouse',13,'add_warehouse'),(50,'Can change warehouse',13,'change_warehouse'),(51,'Can delete warehouse',13,'delete_warehouse'),(52,'Can view warehouse',13,'view_warehouse'),(53,'Can add product',14,'add_product'),(54,'Can change product',14,'change_product'),(55,'Can delete product',14,'delete_product'),(56,'Can view product',14,'view_product'),(57,'Can add employee warehouseman',15,'add_employeewarehouseman'),(58,'Can change employee warehouseman',15,'change_employeewarehouseman'),(59,'Can delete employee warehouseman',15,'delete_employeewarehouseman'),(60,'Can view employee warehouseman',15,'view_employeewarehouseman'),(61,'Can add factory',16,'add_factory'),(62,'Can change factory',16,'change_factory'),(63,'Can delete factory',16,'delete_factory'),(64,'Can view factory',16,'view_factory'),(65,'Can add parameter',17,'add_parameter'),(66,'Can change parameter',17,'change_parameter'),(67,'Can delete parameter',17,'delete_parameter'),(68,'Can view parameter',17,'view_parameter'),(69,'Can add specialization',18,'add_specialization'),(70,'Can change specialization',18,'change_specialization'),(71,'Can delete specialization',18,'delete_specialization'),(72,'Can view specialization',18,'view_specialization'),(73,'Can add type equipment',19,'add_typeequipment'),(74,'Can change type equipment',19,'change_typeequipment'),(75,'Can delete type equipment',19,'delete_typeequipment'),(76,'Can view type equipment',19,'view_typeequipment'),(77,'Can add type workshop',20,'add_typeworkshop'),(78,'Can change type workshop',20,'change_typeworkshop'),(79,'Can delete type workshop',20,'delete_typeworkshop'),(80,'Can view type workshop',20,'view_typeworkshop'),(81,'Can add employee driver',21,'add_employeedriver'),(82,'Can change employee driver',21,'change_employeedriver'),(83,'Can delete employee driver',21,'delete_employeedriver'),(84,'Can view employee driver',21,'view_employeedriver'),(85,'Can add workshop',22,'add_workshop'),(86,'Can change workshop',22,'change_workshop'),(87,'Can delete workshop',22,'delete_workshop'),(88,'Can view workshop',22,'view_workshop'),(89,'Can add material',23,'add_material'),(90,'Can change material',23,'change_material'),(91,'Can delete material',23,'delete_material'),(92,'Can view material',23,'view_material'),(93,'Can add equipment',24,'add_equipment'),(94,'Can change equipment',24,'change_equipment'),(95,'Can delete equipment',24,'delete_equipment'),(96,'Can view equipment',24,'view_equipment'),(97,'Can add entry parameter',25,'add_entryparameter'),(98,'Can change entry parameter',25,'change_entryparameter'),(99,'Can delete entry parameter',25,'delete_entryparameter'),(100,'Can view entry parameter',25,'view_entryparameter'),(101,'Can add transportation',26,'add_transportation'),(102,'Can change transportation',26,'change_transportation'),(103,'Can delete transportation',26,'delete_transportation'),(104,'Can view transportation',26,'view_transportation'),(105,'Can add employee metallurgist',27,'add_employeemetallurgist'),(106,'Can change employee metallurgist',27,'change_employeemetallurgist'),(107,'Can delete employee metallurgist',27,'delete_employeemetallurgist'),(108,'Can view employee metallurgist',27,'view_employeemetallurgist');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
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
