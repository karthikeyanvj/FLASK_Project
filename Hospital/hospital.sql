-- phpMyAdmin SQL Dump
-- version 4.0.4
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 03, 2021 at 01:48 PM
-- Server version: 5.6.12-log
-- PHP Version: 5.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `hospital`
--
CREATE DATABASE IF NOT EXISTS `hospital` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `hospital`;

-- --------------------------------------------------------

--
-- Table structure for table `appointment`
--

CREATE TABLE IF NOT EXISTS `appointment` (
  `pt_id` int(11) NOT NULL,
  `pt_name` varchar(30) NOT NULL,
  `pt_age` int(11) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `visit_date` date NOT NULL,
  `timing` time NOT NULL,
  `symptoms` varchar(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `appointment`
--

INSERT INTO `appointment` (`pt_id`, `pt_name`, `pt_age`, `gender`, `visit_date`, `timing`, `symptoms`) VALUES
(1, 'Moorthi', 45, 'male', '2021-05-07', '04:58:00', 'Fever, Cold'),
(3, 'Vijay', 34, 'male', '2021-05-20', '12:34:00', 'cough'),
(9, 'ram', 34, 'male', '2021-05-15', '13:58:00', 'neck pain');

-- --------------------------------------------------------

--
-- Table structure for table `doctordetail`
--

CREATE TABLE IF NOT EXISTS `doctordetail` (
  `doctorid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `experience` int(11) NOT NULL,
  `speciality` varchar(30) NOT NULL,
  `gender` varchar(30) NOT NULL,
  PRIMARY KEY (`doctorid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Dumping data for table `doctordetail`
--

INSERT INTO `doctordetail` (`doctorid`, `name`, `experience`, `speciality`, `gender`) VALUES
(2, 'anu', 45, 'ghrfhnrf', 'female'),
(6, 'dshf', 0, 'df', 'male'),
(7, 'saajy', 4, 'cardio', 'male'),
(8, 'sandhya', 10, 'heart', 'female'),
(9, 'sai', 6, 'ortho', 'male');

-- --------------------------------------------------------

--
-- Table structure for table `medicine`
--

CREATE TABLE IF NOT EXISTS `medicine` (
  `med_id` int(11) NOT NULL AUTO_INCREMENT,
  `medicine_name` varchar(30) NOT NULL,
  `expiry_date` date NOT NULL,
  `manf_date` date NOT NULL,
  `availability` varchar(10) NOT NULL,
  PRIMARY KEY (`med_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `medicine`
--

INSERT INTO `medicine` (`med_id`, `medicine_name`, `expiry_date`, `manf_date`, `availability`) VALUES
(1, 'dsfgsdfh', '2021-05-28', '2021-04-28', 'YES'),
(2, 'jjgkfgjkgk', '2021-06-03', '2021-06-05', 'YES'),
(3, 'hgklgh', '2021-06-02', '2021-05-21', 'NO'),
(4, 'jhjhkghhkg', '2021-04-30', '2021-05-22', 'YES');

-- --------------------------------------------------------

--
-- Table structure for table `patientdetail`
--

CREATE TABLE IF NOT EXISTS `patientdetail` (
  `patientid` int(11) NOT NULL AUTO_INCREMENT,
  `pt_name` varchar(30) NOT NULL,
  `pt_age` int(11) NOT NULL,
  `ctnumber` int(11) NOT NULL,
  `pt_gender` varchar(30) NOT NULL,
  PRIMARY KEY (`patientid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=16 ;

--
-- Dumping data for table `patientdetail`
--

INSERT INTO `patientdetail` (`patientid`, `pt_name`, `pt_age`, `ctnumber`, `pt_gender`) VALUES
(1, 'Moorthi', 46, 2147483647, 'male'),
(3, 'Vjay', 76, 2147483647, 'male'),
(6, 'sdfh', 0, 878, 'male'),
(7, 'dfgh', 0, 346, 'male'),
(8, 'Vjay', 0, 67, 'male'),
(9, 'ram', 56, 5436447, 'male'),
(10, 'sdfh', 54, 457547, 'male'),
(11, 'hfghf', 56, 756845854, 'female'),
(12, 'hfghf', 56, 756845854, 'female'),
(13, 'surya', 45, 2147483647, 'male'),
(14, 'sudan', 56, 456734643, 'male'),
(15, 'selva', 57, 2147483647, 'male');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
