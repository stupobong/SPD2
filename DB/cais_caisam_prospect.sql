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
-- Table structure for table `caisam_prospect`
--

DROP TABLE IF EXISTS `caisam_prospect`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `caisam_prospect` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `DoB` date DEFAULT NULL,
  `birth_address` varchar(60) DEFAULT NULL,
  `nationality` varchar(100) DEFAULT NULL,
  `religion` varchar(100) DEFAULT NULL,
  `apply_grade_level` varchar(100) DEFAULT NULL,
  `academic_year` varchar(100) DEFAULT NULL,
  `profile_pic` varchar(100) DEFAULT NULL,
  `health_record` varchar(100) DEFAULT NULL,
  `physical_checkup` varchar(100) DEFAULT NULL,
  `vaccinated` varchar(100) DEFAULT NULL,
  `dose_vaccination` varchar(100) DEFAULT NULL,
  `id_vaccine_card` varchar(60) DEFAULT NULL,
  `early_school` varchar(100) DEFAULT NULL,
  `parent_name` varchar(60) DEFAULT NULL,
  `parent_occupation` varchar(60) DEFAULT NULL,
  `parent_email` varchar(60) DEFAULT NULL,
  `parent_contact` varchar(60) DEFAULT NULL,
  `emergency_cont_name` varchar(60) DEFAULT NULL,
  `emergency_contact` varchar(60) DEFAULT NULL,
  `emergency_address` varchar(60) DEFAULT NULL,
  `address` varchar(60) DEFAULT NULL,
  `city` varchar(60) DEFAULT NULL,
  `country` varchar(60) DEFAULT NULL,
  `date_added` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `caisam_prospect`
--

LOCK TABLES `caisam_prospect` WRITE;
/*!40000 ALTER TABLE `caisam_prospect` DISABLE KEYS */;
INSERT INTO `caisam_prospect` VALUES (1,'Malyta','Bin','Female','2008-05-13','St. Rada 321, 3E0 Krang Tnung','Cambodian','Buddhism','Grade 11','2023-2024','DSC_3503.JPG','None','Yes','Yes','5th Dose','551155','Indratevy Secondary School','Bin Chaknith','IT','binchaknith@gmail.com','+855 59 69 89 79','Bin Coleno','+855 59 68 49 45','St. Rada 321, 3E0 Krang Tnung','St. Rada 321, 3E0 Krang Tnung','Phnom Penh','Cambodia','2023-05-13'),(2,'Pisal Sak','Channa','Male','2012-05-13','St. #21, 24E0 Toul Kork','Cambodian','SDA Christian','Grade 5','2023-2024','IMG_2476_orfqLeY.JPG','None','Yes','Yes','4th Dose','226554','Toul Tumpoung Primary School','Channa Setha','Filmaker','channaseth@gmail.com','+855 59 87 96 57','Channa Sovan Sak','+855 36 59 48 85','St. #21, 24E0 Toul Kork','St. #21, 24E0 Toul Kork, Sen Sok','Phnom Penh','Cambodia','2023-05-13'),(3,'Angech','Lee','Female','2015-05-13','St. #21, 278E0 Beoung Snor, Por Sen Chey','Cambodian','Buddhism','Grade 2','2023-2024','DSC_1302.JPG','None','Yes','Yes','3rd Dose','289877','Beoung Snor Primary School','Ly Kuymeng','Businessman','lykuymeng@gmail.com','+855 98 97 84 845','Lee Sakdavuth','+855 59 78 85 98','St. #21, 278E0 Beoung Snor, Por Sen Chey','St. #21, 278E0 Beoung Snor, Por Sen Chey','Phnom Penh','Cambodia','2023-05-13'),(4,'Reth Mony','Sovan','Male','2007-05-13','St. #43 Krovanh Phum Kraseng Kratie Cambodia','Cambodian','SDA Christian','Grade 11','2023-2024','IMG_0459.JPG','None','Yes','Yes','4th Dose','559986','Kratie Primary School','Reth Sovan Henry','Pastor','rethsovanhenry@gmail.com','+855 59 68 65 78','Reth Sovan ALiza','+855 69 78 15 46','St. #43 Krovanh Phum Kraseng Kratie Cambodia','St. #43 Krovanh Phum Kraseng','Kratie','Cambodia','2023-05-13'),(5,'Zamana','Piphoub','Female','2009-02-15','#48Eo, St.156 S/K Phsaar Deepou Muoy, Khan Tuol Kouk','Cambodian','Buddhism','Grade 11','2023-2024','DSC_3515.JPG','None','Yes','Yes','4th Dose','112456','Indratevy Primary School','Piphoup JokChey','Businessman','piphoupjokchey@gmail.com','+855 12 595 000','Son Sopheaktra','+855 015 595 000','#48Eo, St.156 S/K Phsaar Deepou Muoy, Khan Tuol Kouk','#48Eo, St.156 S/K Phsaar Deepou Muoy, Khan Tuol Kouk','Phnom Penh','Cambodia','2023-05-14');
/*!40000 ALTER TABLE `caisam_prospect` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-14 11:32:14
