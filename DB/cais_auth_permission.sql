-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: cais
-- ------------------------------------------------------
-- Server version	8.0.33

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
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add academic_ year',7,'add_academic_year'),(26,'Can change academic_ year',7,'change_academic_year'),(27,'Can delete academic_ year',7,'delete_academic_year'),(28,'Can view academic_ year',7,'view_academic_year'),(29,'Can add city',8,'add_city'),(30,'Can change city',8,'change_city'),(31,'Can delete city',8,'delete_city'),(32,'Can view city',8,'view_city'),(33,'Can add class_ academic',9,'add_class_academic'),(34,'Can change class_ academic',9,'change_class_academic'),(35,'Can delete class_ academic',9,'delete_class_academic'),(36,'Can view class_ academic',9,'view_class_academic'),(37,'Can add classroom',10,'add_classroom'),(38,'Can change classroom',10,'change_classroom'),(39,'Can delete classroom',10,'delete_classroom'),(40,'Can view classroom',10,'view_classroom'),(41,'Can add country',11,'add_country'),(42,'Can change country',11,'change_country'),(43,'Can delete country',11,'delete_country'),(44,'Can view country',11,'view_country'),(45,'Can add enroll_ exam',12,'add_enroll_exam'),(46,'Can change enroll_ exam',12,'change_enroll_exam'),(47,'Can delete enroll_ exam',12,'delete_enroll_exam'),(48,'Can view enroll_ exam',12,'view_enroll_exam'),(49,'Can add entrance_ exam',13,'add_entrance_exam'),(50,'Can change entrance_ exam',13,'change_entrance_exam'),(51,'Can delete entrance_ exam',13,'delete_entrance_exam'),(52,'Can view entrance_ exam',13,'view_entrance_exam'),(53,'Can add prospect',14,'add_prospect'),(54,'Can change prospect',14,'change_prospect'),(55,'Can delete prospect',14,'delete_prospect'),(56,'Can view prospect',14,'view_prospect'),(57,'Can add registree',15,'add_registree'),(58,'Can change registree',15,'change_registree'),(59,'Can delete registree',15,'delete_registree'),(60,'Can view registree',15,'view_registree'),(61,'Can add staff',16,'add_staff'),(62,'Can change staff',16,'change_staff'),(63,'Can delete staff',16,'delete_staff'),(64,'Can view staff',16,'view_staff'),(65,'Can add subject',17,'add_subject'),(66,'Can change subject',17,'change_subject'),(67,'Can delete subject',17,'delete_subject'),(68,'Can view subject',17,'view_subject'),(69,'Can add teacher',18,'add_teacher'),(70,'Can change teacher',18,'change_teacher'),(71,'Can delete teacher',18,'delete_teacher'),(72,'Can view teacher',18,'view_teacher'),(73,'Can add student',19,'add_student'),(74,'Can change student',19,'change_student'),(75,'Can delete student',19,'delete_student'),(76,'Can view student',19,'view_student'),(77,'Can add street',20,'add_street'),(78,'Can change street',20,'change_street'),(79,'Can delete street',20,'delete_street'),(80,'Can view street',20,'view_street'),(81,'Can add state',21,'add_state'),(82,'Can change state',21,'change_state'),(83,'Can delete state',21,'delete_state'),(84,'Can view state',21,'view_state'),(85,'Can add staff_ user',22,'add_staff_user'),(86,'Can change staff_ user',22,'change_staff_user'),(87,'Can delete staff_ user',22,'delete_staff_user'),(88,'Can view staff_ user',22,'view_staff_user'),(89,'Can add exam_ stats',23,'add_exam_stats'),(90,'Can change exam_ stats',23,'change_exam_stats'),(91,'Can delete exam_ stats',23,'delete_exam_stats'),(92,'Can view exam_ stats',23,'view_exam_stats'),(93,'Can add enroll_n student',24,'add_enroll_nstudent'),(94,'Can change enroll_n student',24,'change_enroll_nstudent'),(95,'Can delete enroll_n student',24,'delete_enroll_nstudent'),(96,'Can view enroll_n student',24,'view_enroll_nstudent'),(97,'Can add address',25,'add_address'),(98,'Can change address',25,'change_address'),(99,'Can delete address',25,'delete_address'),(100,'Can view address',25,'view_address');
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

-- Dump completed on 2023-05-14 11:31:58
