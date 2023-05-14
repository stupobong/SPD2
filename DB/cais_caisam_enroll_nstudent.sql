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
-- Table structure for table `caisam_enroll_nstudent`
--

DROP TABLE IF EXISTS `caisam_enroll_nstudent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `caisam_enroll_nstudent` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date_added` date NOT NULL,
  `academic_year_id` bigint NOT NULL,
  `examid_card_id` bigint NOT NULL,
  `into_class_id` bigint NOT NULL,
  `student_user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `student_user_id` (`student_user_id`),
  KEY `caisam_enroll_nstude_academic_year_id_9cafb4f7_fk_caisam_ac` (`academic_year_id`),
  KEY `caisam_enroll_nstude_examid_card_id_5f87e7d2_fk_caisam_ex` (`examid_card_id`),
  KEY `caisam_enroll_nstude_into_class_id_5381ab9d_fk_caisam_cl` (`into_class_id`),
  CONSTRAINT `caisam_enroll_nstude_academic_year_id_9cafb4f7_fk_caisam_ac` FOREIGN KEY (`academic_year_id`) REFERENCES `caisam_academic_year` (`id`),
  CONSTRAINT `caisam_enroll_nstude_examid_card_id_5f87e7d2_fk_caisam_ex` FOREIGN KEY (`examid_card_id`) REFERENCES `caisam_exam_stats` (`id`),
  CONSTRAINT `caisam_enroll_nstude_into_class_id_5381ab9d_fk_caisam_cl` FOREIGN KEY (`into_class_id`) REFERENCES `caisam_classroom` (`id`),
  CONSTRAINT `caisam_enroll_nstudent_student_user_id_75f6b89d_fk_auth_user_id` FOREIGN KEY (`student_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `caisam_enroll_nstudent`
--

LOCK TABLES `caisam_enroll_nstudent` WRITE;
/*!40000 ALTER TABLE `caisam_enroll_nstudent` DISABLE KEYS */;
INSERT INTO `caisam_enroll_nstudent` VALUES (1,'2023-05-14',1,1,1,23),(2,'2023-05-14',1,2,4,33),(3,'2023-05-14',1,3,6,38),(4,'2023-05-14',1,4,1,27),(5,'2023-05-14',1,5,1,26);
/*!40000 ALTER TABLE `caisam_enroll_nstudent` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-14 11:31:53
