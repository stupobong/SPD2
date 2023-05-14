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
-- Table structure for table `caisam_staff_user`
--

DROP TABLE IF EXISTS `caisam_staff_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `caisam_staff_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `profile_pic` varchar(100) DEFAULT NULL,
  `date_added` datetime(6) NOT NULL,
  `card_number_id` bigint NOT NULL,
  `username_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username_id` (`username_id`),
  KEY `caisam_staff_user_card_number_id_69d7c52b_fk_caisam_staff_id` (`card_number_id`),
  CONSTRAINT `caisam_staff_user_card_number_id_69d7c52b_fk_caisam_staff_id` FOREIGN KEY (`card_number_id`) REFERENCES `caisam_staff` (`id`),
  CONSTRAINT `caisam_staff_user_username_id_1fcb061e_fk_auth_user_id` FOREIGN KEY (`username_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `caisam_staff_user`
--

LOCK TABLES `caisam_staff_user` WRITE;
/*!40000 ALTER TABLE `caisam_staff_user` DISABLE KEYS */;
INSERT INTO `caisam_staff_user` VALUES (1,'sopheaktra_sieng_Ppk13xy.png','2023-05-13 18:51:02.696745',1,2),(2,'sofia_phan_VOm2mh4.png','2023-05-13 18:51:23.502891',2,3),(3,'','2023-05-13 18:51:33.313457',3,4),(4,'','2023-05-13 18:52:05.337248',4,12),(5,'Vannak_Leng_NGM0Jyk.png','2023-05-13 23:30:47.722326',5,13),(6,'DSC_1384.JPG','2023-05-13 23:41:07.352763',10,22),(7,'July_Thach_Gz7HLuF.png','2023-05-13 23:42:04.640669',9,9),(8,'DSC_1961_5paZQQ4.JPG','2023-05-13 23:42:32.855515',11,21),(9,'DSC_1487.JPG','2023-05-13 23:42:56.757687',12,19),(10,'seiha_chan_VYwBDxn.png','2023-05-13 23:43:21.040173',13,16);
/*!40000 ALTER TABLE `caisam_staff_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-14 11:32:11
