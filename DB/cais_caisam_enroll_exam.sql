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
-- Table structure for table `caisam_enroll_exam`
--

DROP TABLE IF EXISTS `caisam_enroll_exam`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `caisam_enroll_exam` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(60) DEFAULT NULL,
  `date_added` date NOT NULL,
  `classroom_id` bigint NOT NULL,
  `prospect_name_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `caisam_enroll_exam_classroom_id_23eecbeb_fk_caisam_en` (`classroom_id`),
  KEY `caisam_enroll_exam_prospect_name_id_6696a3f0_fk_caisam_pr` (`prospect_name_id`),
  CONSTRAINT `caisam_enroll_exam_classroom_id_23eecbeb_fk_caisam_en` FOREIGN KEY (`classroom_id`) REFERENCES `caisam_entrance_exam` (`id`),
  CONSTRAINT `caisam_enroll_exam_prospect_name_id_6696a3f0_fk_caisam_pr` FOREIGN KEY (`prospect_name_id`) REFERENCES `caisam_prospect` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `caisam_enroll_exam`
--

LOCK TABLES `caisam_enroll_exam` WRITE;
/*!40000 ALTER TABLE `caisam_enroll_exam` DISABLE KEYS */;
INSERT INTO `caisam_enroll_exam` VALUES (1,'Malyta_202303001','2023-05-14',3,1),(2,'Pisalsak_202102001','2023-05-14',5,2),(3,'Angech_202101001','2023-05-14',1,3),(4,'Mony_202103005','2023-05-14',6,4),(5,'Zamana-202103004','2023-05-14',6,5);
/*!40000 ALTER TABLE `caisam_enroll_exam` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-14 11:31:25
