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
-- Table structure for table `caisam_student`
--

DROP TABLE IF EXISTS `caisam_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `caisam_student` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `grade_level` varchar(100) DEFAULT NULL,
  `student_status` varchar(100) DEFAULT NULL,
  `age` varchar(100) NOT NULL,
  `DoB` date DEFAULT NULL,
  `nationality` varchar(100) DEFAULT NULL,
  `religion` varchar(100) DEFAULT NULL,
  `student_idcard` varchar(60) NOT NULL,
  `email` varchar(60) DEFAULT NULL,
  `profile_pic` varchar(100) DEFAULT NULL,
  `father_status` varchar(100) DEFAULT NULL,
  `father_firstname` varchar(60) DEFAULT NULL,
  `father_lastname` varchar(60) DEFAULT NULL,
  `father_occupation` varchar(60) DEFAULT NULL,
  `mother_status` varchar(100) DEFAULT NULL,
  `mother_firstname` varchar(60) DEFAULT NULL,
  `mother_lastname` varchar(60) DEFAULT NULL,
  `mother_occupation` varchar(60) DEFAULT NULL,
  `parent_email` varchar(60) DEFAULT NULL,
  `parent_contact1` varchar(60) DEFAULT NULL,
  `parent_contact2` varchar(60) DEFAULT NULL,
  `address` varchar(60) DEFAULT NULL,
  `city` varchar(60) DEFAULT NULL,
  `country` varchar(100) DEFAULT NULL,
  `date_joined` date DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `caisam_student_user_id_db25ce4e_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `caisam_student`
--

LOCK TABLES `caisam_student` WRITE;
/*!40000 ALTER TABLE `caisam_student` DISABLE KEYS */;
INSERT INTO `caisam_student` VALUES (1,'Sovan Mony','Reth','Male','Grade 11','New Student','16','2007-05-13','Cambodian','SDA Christian','202103004','202103004@caisedu.com','IMG_0459_cfyFRAc.JPG','Living','Sovan Henry','Reth','Pastor','Living','Sovan ALiza','Reth','Housewife','rethsovanhenry','+855 69 78 15 46','+855 59 68 65 78','St. #43 Krovanh Phum Kraseng','Kratie','Cambodia','2023-05-13',27),(2,'Malyta','Bin','Female','Grade 11','Existing Student','15','2008-05-13','Cambodian','SDA Christian','202103001','202103001@caisedu.com','DSC_1798.JPG','Living','Bin','Chaknith','IT','Living','Coleno','Bin','Housewife','binchaknith@gmail.com','+855 48 68 78 98','+855 59 68 48 59','Phum Tumnub, Toul Kork','Phnom Penh','Cambodia','2023-05-13',23),(3,'Pisalsak','Channa','Male','Grade 7','New Student','11','2012-05-14','Cambodian','SDA Christian','202102001','202102001@caisedu.com','DSC_3278.JPG','Living','Setha','Channa','Dentist','Living','Choum','Sereyvuthy','IT','channasetha@gmail.com','+855 063 6903 897','+855 023 214 319','#150Eo, St.156 S/K Phsaar Deepou Muoy, Khan Tuol Kouk','Phnom Penh','Cambodia','2023-05-14',33),(4,'Angech','Lee','Female','Grade 3','New Student','7','2016-05-14','Cambodian','Buddhism','202101001','202101001@caisedu.com','DSC_1293.JPG','Living','Kuymeng','Lee','Businessman','Living','Sunita','Sun','Saleperson','leekuymeng@gmail.com','+855 89 78 85 95','+855 16 54 85 59','#50Eo, St.156 S/K Phsaar Deepou Muoy, Khan Tuol Kouk','Phnom Penh','Cambodia','2023-05-14',38),(7,'Sovan Daniel','Reth','Male','Grade 11','Existing Student','16','2008-05-13','Cambodian','SDA Christian','202103007','202103007@caisedu.com','DSC_3482.JPG','Living','Thorn Sovan','Nhean','Pastor','Living','Sreyleak','Chin','Housewife','nheanthornsovan@gmail.com','+855 89 79 45 68','+855 16 86 59 45','#792, National Road 5 S/K Ruessei Kaev, Khan Ruessei Kaev','Phnom Penh','Cambodia','2023-05-14',29),(8,'Zamana','Piphoup','Female','Grade 11','New Student','16','2008-05-12','Cambodian','SDA Christian','2021003004','202103004@caisedu.com','','Living','Jokchey','Piphoup','Businessman','Living','Sopheaktra','Srun','Housewife','piphoupjokchey@gmail.com','+855 12 595 000','+855 15 595 000','#48Eo, St.156 S/K Phsaar Deepou Muoy, Khan Tuol Kouk','Phnom Penh','Cambodia',NULL,26);
/*!40000 ALTER TABLE `caisam_student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-14 11:31:48
