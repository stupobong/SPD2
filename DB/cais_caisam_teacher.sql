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
-- Table structure for table `caisam_teacher`
--

DROP TABLE IF EXISTS `caisam_teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `caisam_teacher` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `first_name` varchar(60) DEFAULT NULL,
  `last_name` varchar(60) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `DoB` date DEFAULT NULL,
  `nationality` varchar(100) DEFAULT NULL,
  `religion` varchar(100) DEFAULT NULL,
  `profile_pic` varchar(100) DEFAULT NULL,
  `bachelor_degree` varchar(100) DEFAULT NULL,
  `email` varchar(60) DEFAULT NULL,
  `phone_num` varchar(60) DEFAULT NULL,
  `address` varchar(60) DEFAULT NULL,
  `city` varchar(60) DEFAULT NULL,
  `country` varchar(100) DEFAULT NULL,
  `date_joined` date DEFAULT NULL,
  `staff_user_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `staff_user_id` (`staff_user_id`),
  CONSTRAINT `caisam_teacher_staff_user_id_bb8f5da5_fk_caisam_staff_id` FOREIGN KEY (`staff_user_id`) REFERENCES `caisam_staff` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `caisam_teacher`
--

LOCK TABLES `caisam_teacher` WRITE;
/*!40000 ALTER TABLE `caisam_teacher` DISABLE KEYS */;
INSERT INTO `caisam_teacher` VALUES (1,'Sopheaktra','Sieng','Male','1995-05-09','Cambodian','SDA Christian','sopheaktra_sieng_TZsmKwg.png','BS of Science','siengsopheaktra@caisedu.com','+855 89 59 87 68','St. Rada 321, 3E0 Krang Tnung','Phnom Penh','Cambodia','2023-05-13',1),(2,'Sophia','Phan','Female','1997-05-14','Cambodian','SDA Christian','sofia_phan_EYMoSLx.png','BA of TESOL','phansophia@caisedu.com','+855 89 59 89 65','#49Eo, St.156 S/K Phsaar Deepou Muoy, Khan Tuol Kouk','Phnom Penh','Cambodia','2023-05-14',2),(3,'Sopheak','Meas','Male','1979-05-14','Cambodian','SDA Christian','meas_sopheak_nfmsIsF.png','MBA of Administration','meassopheak@caisedu.com','+855 16 98 65 79','#792, National Road 5 S/K Ruessei Kaev, Khan Ruessei Kaev','Phnom Penh','Cambodia','2023-05-14',3),(4,'Sadam','Ka','Male','1989-05-14','Cambodian','SDA Christian','ka_sadam_bYkI0xu.png','MBA of Education','kasadam@caisedu.com','+855 89 78 48 96','#49Eo, St.156 S/K Phsaar Deepou Muoy, Khan Tuol Kouk','Phnom Penh','Cambodia','2023-05-14',4),(5,'Silim','Sip','Female','1985-05-14','Cambodian','SDA Christian','DSC_1646.JPG','BA of Education','sipsilim@caisedu.com','+855 53 6330 331','#160Eo, St.217 (Monireth) S/K Toul Svay Prey I, Khan Chamkar','Phnom Penh','Cambodia','2023-05-14',10),(6,'Chhaiya','Sou','Male','1985-05-14','Cambodian','SDA Christian','DSC_1961_qL2Acny.JPG','BA of Education','souchhaiya@caisedu.com','+855 12 304 897/012 615 349/012 829 410','#150Eo, St.156 S/K Phsaar Deepou Muoy, Khan Tuol Kouk','Phnom Penh','Cambodia','2023-05-14',11),(7,'Vannak','Leng','Female','1987-05-16','Cambodian','SDA Christian','Vannak_Leng_1UCwnZx.png','MBA of Education','t21312@caisedu.com','+855 59 15 48 68','#48Eo, St.156 S/K Phsaar Deepou Muoy, Khan Tuol Kouk','Phnom Penh','Cambodia','2023-05-14',5);
/*!40000 ALTER TABLE `caisam_teacher` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-14 11:31:46
