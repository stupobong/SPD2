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
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('dua5umrk453xb2ea3aiadp0dhhgn51kb','.eJxVjDEOgzAMRe-SuYoiEhvSsXvPEDm2U2grkAhMqHcvSAzt-t77fzOJ1qVPa9U5DWKupvHm8gsz8UvHw8iTxsdkeRqXecj2SOxpq71Pou_b2f4d9FT7fQ1CHXBBbGLg4NoWOkIAh7GoDx6R2oaRBYsTzhJUY8wFdkAQvUTz-QL98zhb:1py1d6:_GUOKm-gTtX286XxcmBo1Oc7HwBkt4XsMJkgrR7fYDQ','2023-05-28 02:38:36.032219'),('fpscyfu5v46pkgukeotpfuxwpweyvwbz','.eJxVjDsOwyAQBe9CHSFr-RhSps8Z0C4LwUkEkrErK3ePkFwk7ZuZd4iA-1bC3tMaFhZXoZW4_I6E8ZXqIPzE-mgytrqtC8mhyJN2eW-c3rfT_Tso2MuoGXK2emZkE22OwEQMALP1KkFE7TIkSm4CIg_eOENktAHK1qo4OfH5AjyHOMw:1pxzQ4:rKpWIh3sNVV49kzMaj-A4v8fzppAw0bD9Jju0ubAT-k','2023-05-28 00:17:00.847420'),('jmgsrh6mj2rt20g65sxdcxztno114oas','.eJxVjEEOwiAQRe_C2hCgU6Au3XsGMjCDVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwkzgLGMXpd4yYHlx3QnestyZTq-syR7kr8qBdXhvx83K4fwcFe_nWE3N2YMADKY-UgCZnUlaaR2BW1iBhxMGyAsfeeuWGlHVMBrUasnbi_QEdIThe:1py2HV:x-Mx1ypPOMEnQTbQkVHbRIuT9HFcwp0yopRUWd0wV74','2023-05-28 03:20:21.260206'),('rjumdzzmyhoplqrljly4zzdnq21vbhsw','.eJxVjEEOwiAQRe_C2pCB0o64dN8zkIEZpGpoUtqV8e7apAvd_vfef6lA21rC1mQJE6uLMur0u0VKD6k74DvV26zTXNdlinpX9EGbHmeW5_Vw_w4KtfKtUyTkRGYQCznBIB2gIUQjMXbWEPgcxZ57T8khOAuO0ZPvLRt0nL16fwD4dTfu:1py1tY:LcGf-3S3vu8S9LoAllVdsifbjm5imHDYsHxfz4lYx_Q','2023-05-28 02:55:36.820132');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-14 11:32:18
