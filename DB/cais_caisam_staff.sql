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
-- Table structure for table `caisam_staff`
--

DROP TABLE IF EXISTS `caisam_staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `caisam_staff` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `card_number` varchar(60) DEFAULT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `contact` varchar(60) DEFAULT NULL,
  `position` varchar(200) NOT NULL,
  `status` varchar(100) DEFAULT NULL,
  `profile_pic` varchar(100) DEFAULT NULL,
  `date_added` datetime(6) NOT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `card_number` (`card_number`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `caisam_staff_user_id_1eeef70e_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `caisam_staff`
--

LOCK TABLES `caisam_staff` WRITE;
/*!40000 ALTER TABLE `caisam_staff` DISABLE KEYS */;
INSERT INTO `caisam_staff` VALUES (1,'T21301','Sopheaktra','Sieng','Male','+855 89 59 67 81','Homeroom Teacher','Active','sopheaktra_sieng_VpKJqWS.png','2023-05-13 12:23:20.192335',2),(2,'21302','Sophia','Phan','Female','+855 89 48 78 86','Homeroom Teacher','Active','sofia_phan_6GfkGq8.png','2023-05-13 12:24:11.705325',3),(3,'T21303','Sopheak','Meas','Male','+855 89 48 68 78','Homeroom Teacher','Active','meas_sopheak_grKYCAs.png','2023-05-13 12:24:42.963605',4),(4,'T21311','Sadam','Ka','Male','+855 88 78 98 56','Homeroom Teacher','Active','ka_sadam_KWKbK8p.png','2023-05-13 12:25:15.640776',12),(5,'T21312','Vannak','Leng','Female','+855 25 65 78 97','Homeroom Teacher','Active','Vannak_Leng_vVPULvK.png','2023-05-13 12:25:40.333707',13),(7,'registrar_01','Bopha','Chin','Female','+855 54 87 98 56','Registrar','Active','bopha_chin_xT7iHO5.jpg','2023-05-13 12:27:00.271725',43),(8,'S21310','Kaneetha','Sophal','Female','+855 48 87 987 78','Accountant','Active','Kaneetha_Sophal_40eeHaC.png','2023-05-13 12:27:47.472318',11),(9,'S21308','July','Thach','Male','+855 48 68 48 59','Vice-Principal','Active','July_Thach_xfjzKoa.png','2023-05-13 12:28:23.245560',9),(10,'T21321','Silim','Sip','Female','092 638 881/011 336 149','Homeroom Teacher','Active','thim_buntheourn_8XIooUH.png','2023-05-13 23:36:36.587350',22),(11,'T21320','Chhaiya','Sou','Male','012 304 897/012 615 349/012 829 410','Homeroom Teacher','Active','DSC_1961.JPG','2023-05-13 23:38:30.669847',21),(12,'T21318','Sodalin','Sorn','Female','023 214 319','Homeroom Teacher','Active','Socheat_Sieng.png','2023-05-13 23:39:41.161511',19),(13,'T21315','Seiha','Chan','Female','+855 23 6312 402','Homeroom Teacher','Active','seiha_chan_bP46b2K.png','2023-05-13 23:40:20.221626',16);
/*!40000 ALTER TABLE `caisam_staff` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-14 11:31:51
