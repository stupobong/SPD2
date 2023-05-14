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
-- Table structure for table `caisam_class_academic`
--

DROP TABLE IF EXISTS `caisam_class_academic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `caisam_class_academic` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date_added` date NOT NULL,
  `class_academic_id` bigint NOT NULL,
  `student_class_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `caisam_class_academi_student_class_id_5c6af24a_fk_caisam_st` (`student_class_id`),
  KEY `caisam_class_academi_class_academic_id_1c7dee18_fk_caisam_cl` (`class_academic_id`),
  CONSTRAINT `caisam_class_academi_class_academic_id_1c7dee18_fk_caisam_cl` FOREIGN KEY (`class_academic_id`) REFERENCES `caisam_classroom` (`id`),
  CONSTRAINT `caisam_class_academi_student_class_id_5c6af24a_fk_caisam_st` FOREIGN KEY (`student_class_id`) REFERENCES `caisam_student` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `caisam_class_academic`
--

LOCK TABLES `caisam_class_academic` WRITE;
/*!40000 ALTER TABLE `caisam_class_academic` DISABLE KEYS */;
INSERT INTO `caisam_class_academic` VALUES (9,'2023-05-14',1,1),(11,'2023-05-14',1,2);
/*!40000 ALTER TABLE `caisam_class_academic` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-14 11:31:32
