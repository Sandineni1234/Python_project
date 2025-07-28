CREATE DATABASE  IF NOT EXISTS `caab_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `caab_db`;
-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: caab_db
-- ------------------------------------------------------
-- Server version	8.4.4

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
-- Table structure for table `categoria`
--

DROP TABLE IF EXISTS `categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categoria` (
  `id` int NOT NULL AUTO_INCREMENT,
  `categoria_values` varchar(255) DEFAULT NULL,
  `created_by` int DEFAULT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_by` int DEFAULT NULL,
  `modified_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_categoria_createdby` (`created_by`),
  KEY `fk_categoria_modifiedby` (`modified_by`),
  CONSTRAINT `fk_categoria_createdby` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_categoria_modifiedby` FOREIGN KEY (`modified_by`) REFERENCES `user` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `commentsincidents`
--

DROP TABLE IF EXISTS `commentsincidents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `commentsincidents` (
  `id` int NOT NULL AUTO_INCREMENT,
  `DealersID` int NOT NULL,
  `Comments` varchar(255) DEFAULT NULL,
  `Incidents` varchar(255) DEFAULT NULL,
  `stageID` int NOT NULL,
  `CreatedBy` int NOT NULL,
  `ModifiedBy` int DEFAULT NULL,
  `Created_date` datetime DEFAULT NULL,
  `Modified_date` datetime DEFAULT NULL,
  `isactive` bit(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `DealersID` (`DealersID`),
  KEY `ModifiedBy` (`ModifiedBy`),
  KEY `CreatedBy` (`CreatedBy`),
  KEY `stageID` (`stageID`),
  CONSTRAINT `commentsincidents_ibfk_1` FOREIGN KEY (`DealersID`) REFERENCES `dealers` (`id`),
  CONSTRAINT `commentsincidents_ibfk_2` FOREIGN KEY (`ModifiedBy`) REFERENCES `user` (`id`),
  CONSTRAINT `commentsincidents_ibfk_3` FOREIGN KEY (`CreatedBy`) REFERENCES `user` (`id`),
  CONSTRAINT `commentsincidents_ibfk_4` FOREIGN KEY (`stageID`) REFERENCES `stage` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `credit_analysis`
--

DROP TABLE IF EXISTS `credit_analysis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `credit_analysis` (
  `id` int NOT NULL AUTO_INCREMENT,
  `DealersID` int NOT NULL,
  `FiscalYear` varchar(255) DEFAULT NULL,
  `Turnover` varchar(255) DEFAULT NULL,
  `EmpNumber` varchar(255) DEFAULT NULL,
  `EBITDA` varchar(255) DEFAULT NULL,
  `CNAE` varchar(255) DEFAULT NULL,
  `Assets` varchar(255) DEFAULT NULL,
  `DecisionDate` datetime DEFAULT NULL,
  `NetAssets` varchar(255) DEFAULT NULL,
  `AsnefCredit` varchar(255) DEFAULT NULL,
  `AsnefJud` varchar(255) DEFAULT NULL,
  `PYMEScore` varchar(255) DEFAULT NULL,
  `RiskScore` varchar(255) DEFAULT NULL,
  `CreatedBy` int NOT NULL,
  `Isactive` bit(1) NOT NULL,
  `ModifiedBy` int DEFAULT NULL,
  `StatusID` int NOT NULL,
  `Created_date` datetime DEFAULT NULL,
  `Modified_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `DealersID` (`DealersID`),
  KEY `ModifiedBy` (`ModifiedBy`),
  KEY `CreatedBy` (`CreatedBy`),
  KEY `StatusID` (`StatusID`),
  CONSTRAINT `credit_analysis_ibfk_1` FOREIGN KEY (`DealersID`) REFERENCES `dealers` (`id`),
  CONSTRAINT `credit_analysis_ibfk_2` FOREIGN KEY (`ModifiedBy`) REFERENCES `user` (`id`),
  CONSTRAINT `credit_analysis_ibfk_3` FOREIGN KEY (`CreatedBy`) REFERENCES `user` (`id`),
  CONSTRAINT `credit_analysis_ibfk_4` FOREIGN KEY (`StatusID`) REFERENCES `table_status` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `dealers`
--

DROP TABLE IF EXISTS `dealers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dealers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Address` varchar(255) DEFAULT NULL,
  `AskForPolicy` bit(1) NOT NULL,
  `CategoryID` int DEFAULT NULL,
  `CEAReceived` bit(1) NOT NULL,
  `Comercial` varchar(255) DEFAULT NULL,
  `CompanyID` varchar(255) DEFAULT NULL,
  `CreatedBy` int DEFAULT NULL,
  `Creation_date` datetime DEFAULT NULL,
  `EconGroup` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `Isactive` bit(1) NOT NULL,
  `LegalName` varchar(255) DEFAULT NULL,
  `MandateID` int DEFAULT NULL,
  `ModifiedBy` int DEFAULT NULL,
  `Municipality` varchar(255) DEFAULT NULL,
  `PartnerNameSurname1` varchar(255) DEFAULT NULL,
  `PartnerNameSurname2` varchar(255) DEFAULT NULL,
  `PartnerNameSurname3` varchar(255) DEFAULT NULL,
  `PostalCode` varchar(255) DEFAULT NULL,
  `Province` varchar(255) DEFAULT NULL,
  `ShareholderNameSurname1` varchar(255) DEFAULT NULL,
  `ShareholderNameSurname2` varchar(255) DEFAULT NULL,
  `ShareholderNameSurname3` varchar(255) DEFAULT NULL,
  `ShareholderPercentage1` varchar(255) DEFAULT NULL,
  `ShareholderPercentage2` varchar(255) DEFAULT NULL,
  `ShareholderPercentage3` varchar(255) DEFAULT NULL,
  `PartnerPercentage1` varchar(255) DEFAULT NULL,
  `PartnerPercentage2` varchar(255) DEFAULT NULL,
  `PartnerPercentage3` varchar(255) DEFAULT NULL,
  `StageId` int DEFAULT NULL,
  `statusID` int DEFAULT NULL,
  `typeID` int DEFAULT NULL,
  `Zone` varchar(255) DEFAULT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `CategoryID` (`CategoryID`),
  KEY `CreatedBy` (`CreatedBy`),
  KEY `MandateID` (`MandateID`),
  KEY `ModifiedBy` (`ModifiedBy`),
  KEY `StageId` (`StageId`),
  KEY `statusID` (`statusID`),
  KEY `typeID` (`typeID`),
  CONSTRAINT `dealers_ibfk_1` FOREIGN KEY (`CategoryID`) REFERENCES `categoria` (`id`),
  CONSTRAINT `dealers_ibfk_2` FOREIGN KEY (`CreatedBy`) REFERENCES `user` (`id`),
  CONSTRAINT `dealers_ibfk_3` FOREIGN KEY (`MandateID`) REFERENCES `mandato` (`id`),
  CONSTRAINT `dealers_ibfk_4` FOREIGN KEY (`ModifiedBy`) REFERENCES `user` (`id`),
  CONSTRAINT `dealers_ibfk_5` FOREIGN KEY (`StageId`) REFERENCES `stage` (`id`),
  CONSTRAINT `dealers_ibfk_6` FOREIGN KEY (`statusID`) REFERENCES `table_status` (`id`),
  CONSTRAINT `dealers_ibfk_7` FOREIGN KEY (`typeID`) REFERENCES `tipo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `department` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `isactive` bit(1) NOT NULL,
  `created_by` int DEFAULT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_by` int DEFAULT NULL,
  `modified_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_department_createdby` (`created_by`),
  CONSTRAINT `fk_department_createdby` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `documents`
--

DROP TABLE IF EXISTS `documents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `documents` (
  `id_doc` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) DEFAULT NULL,
  `created_by` int DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `modified_by` int DEFAULT NULL,
  `modified_date` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `isactive` bit(1) NOT NULL DEFAULT b'1',
  PRIMARY KEY (`id_doc`),
  KEY `created_by` (`created_by`),
  KEY `modified_by` (`modified_by`),
  CONSTRAINT `documents_ibfk_1` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`),
  CONSTRAINT `documents_ibfk_2` FOREIGN KEY (`modified_by`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fileuploader`
--

DROP TABLE IF EXISTS `fileuploader`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fileuploader` (
  `id` int NOT NULL AUTO_INCREMENT,
  `DealersID` int NOT NULL,
  `FilePath` varchar(500) DEFAULT NULL,
  `filename` varchar(255) DEFAULT NULL,
  `stageID` int NOT NULL,
  `CreatedBy` int NOT NULL,
  `ModifiedBy` int DEFAULT NULL,
  `Created_date` datetime DEFAULT NULL,
  `Modified_date` datetime DEFAULT NULL,
  `isactive` bit(1) NOT NULL,
  `DocumentID` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `DealersID` (`DealersID`),
  KEY `ModifiedBy` (`ModifiedBy`),
  KEY `CreatedBy` (`CreatedBy`),
  KEY `stageID` (`stageID`),
  KEY `fk_documentID` (`DocumentID`),
  CONSTRAINT `fileuploader_ibfk_1` FOREIGN KEY (`DealersID`) REFERENCES `dealers` (`id`),
  CONSTRAINT `fileuploader_ibfk_2` FOREIGN KEY (`ModifiedBy`) REFERENCES `user` (`id`),
  CONSTRAINT `fileuploader_ibfk_3` FOREIGN KEY (`CreatedBy`) REFERENCES `user` (`id`),
  CONSTRAINT `fileuploader_ibfk_4` FOREIGN KEY (`stageID`) REFERENCES `stage` (`id`),
  CONSTRAINT `fk_documentID` FOREIGN KEY (`DocumentID`) REFERENCES `documents` (`id_doc`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `mandato`
--

DROP TABLE IF EXISTS `mandato`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mandato` (
  `id` int NOT NULL AUTO_INCREMENT,
  `mandato_values` varchar(255) DEFAULT NULL,
  `created_by` int DEFAULT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_by` int DEFAULT NULL,
  `modified_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_mandato_createdby` (`created_by`),
  KEY `fk_mandato_modifiedby` (`modified_by`),
  CONSTRAINT `fk_mandato_createdby` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_mandato_modifiedby` FOREIGN KEY (`modified_by`) REFERENCES `user` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `menus`
--

DROP TABLE IF EXISTS `menus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menus` (
  `id` int NOT NULL AUTO_INCREMENT,
  `CreatedBy` int DEFAULT NULL,
  `ModifiedBy` int DEFAULT NULL,
  `Description` varchar(255) DEFAULT NULL,
  `Isactive` bit(1) DEFAULT b'1',
  `Name` varchar(255) DEFAULT NULL,
  `Navigateurl` varchar(255) DEFAULT NULL,
  `StageID` int DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `modified_date` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `CreatedBy` (`CreatedBy`),
  KEY `ModifiedBy` (`ModifiedBy`),
  KEY `StageID` (`StageID`),
  CONSTRAINT `menus_ibfk_1` FOREIGN KEY (`CreatedBy`) REFERENCES `user` (`id`),
  CONSTRAINT `menus_ibfk_2` FOREIGN KEY (`ModifiedBy`) REFERENCES `user` (`id`),
  CONSTRAINT `menus_ibfk_3` FOREIGN KEY (`StageID`) REFERENCES `stage` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `select_language`
--

DROP TABLE IF EXISTS `select_language`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `select_language` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Language_values` varchar(255) DEFAULT NULL,
  `created_by` int DEFAULT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_by` int DEFAULT NULL,
  `modified_date` datetime DEFAULT NULL,
  `language_code` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `stage`
--

DROP TABLE IF EXISTS `stage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stage` (
  `id` int NOT NULL AUTO_INCREMENT,
  `CreatedBy` int DEFAULT NULL,
  `ModifiedBy` int DEFAULT NULL,
  `Stage_name` varchar(255) DEFAULT NULL,
  `created_date` datetime DEFAULT NULL,
  `modified_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_stage_createdby` (`CreatedBy`),
  KEY `fk_stage_modifiedby` (`ModifiedBy`),
  CONSTRAINT `fk_stage_createdby` FOREIGN KEY (`CreatedBy`) REFERENCES `user` (`id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_stage_modifiedby` FOREIGN KEY (`ModifiedBy`) REFERENCES `user` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `table_status`
--

DROP TABLE IF EXISTS `table_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table_status` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Status_values` varchar(255) DEFAULT NULL,
  `created_by` int DEFAULT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_by` int DEFAULT NULL,
  `modified_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_ctable_status_createdby` (`created_by`),
  KEY `fk_table_status_modifiedby` (`modified_by`),
  CONSTRAINT `fk_ctable_status_createdby` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_table_status_modifiedby` FOREIGN KEY (`modified_by`) REFERENCES `user` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tipo`
--

DROP TABLE IF EXISTS `tipo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo_values` varchar(255) DEFAULT NULL,
  `created_by` int DEFAULT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_by` int DEFAULT NULL,
  `modified_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_tipo_createdby` (`created_by`),
  KEY `fk_department_modifiedby` (`modified_by`),
  CONSTRAINT `fk_department_modifiedby` FOREIGN KEY (`modified_by`) REFERENCES `user` (`id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_tipo_createdby` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_tipo_modifiedby` FOREIGN KEY (`modified_by`) REFERENCES `user` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `isactive` bit(1) NOT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_date` datetime DEFAULT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` bigint DEFAULT NULL,
  `created_by` int DEFAULT NULL,
  `modified_by` int DEFAULT NULL,
  `department_id` int NOT NULL,
  `userMenuID` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone` (`phone`),
  KEY `department_id` (`department_id`),
  KEY `fk_user_role_menu` (`userMenuID`),
  CONSTRAINT `fk_user_role_menu` FOREIGN KEY (`userMenuID`) REFERENCES `userrolemenus` (`id`),
  CONSTRAINT `user_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `department` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `userrolemenus`
--

DROP TABLE IF EXISTS `userrolemenus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userrolemenus` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userRoleMenuID` varchar(10) NOT NULL,
  `isactive` tinyint(1) DEFAULT '1',
  `menu_ids` text NOT NULL,
  `CreatedBy` int DEFAULT NULL,
  `ModifiedBy` int DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `modified_date` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `CreatedBy` (`CreatedBy`),
  KEY `ModifiedBy` (`ModifiedBy`),
  CONSTRAINT `userrolemenus_ibfk_1` FOREIGN KEY (`CreatedBy`) REFERENCES `user` (`id`),
  CONSTRAINT `userrolemenus_ibfk_2` FOREIGN KEY (`ModifiedBy`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-07-28 15:49:45
