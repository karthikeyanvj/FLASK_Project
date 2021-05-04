-- phpMyAdmin SQL Dump
-- version 4.0.4
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 28, 2021 at 09:33 AM
-- Server version: 5.6.12-log
-- PHP Version: 5.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `kar`
--
CREATE DATABASE IF NOT EXISTS `kar` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `kar`;

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE IF NOT EXISTS `employee` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(20) NOT NULL,
  `class` varchar(20) NOT NULL,
  FULLTEXT KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `marks`
--

CREATE TABLE IF NOT EXISTS `marks` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `subject` varchar(20) NOT NULL,
  `marks` int(11) NOT NULL,
  `class` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `marks`
--

INSERT INTO `marks` (`id`, `name`, `subject`, `marks`, `class`) VALUES
(34, 'dshsdf', 'fghnjfd', 33, 3),
(6575, 'hjfg', 'hjpj', 78, 1),
(67, 'hjfgjgf', 'fgkgfk', 56, 1),
(67, 'hjfgjgf', 'fgkgfk', 56, 1),
(45, 'fghfd', 'fdjfd', 45, 4),
(45, 'fghfd', 'fdjfd', 45, 4),
(46, 'dhfg', 'dfg', 56, 1),
(467, 'fgjhfg', 'fg', 86, 1),
(47, 'fgjkh', 'kghjh', 58765, 1),
(47, 'fgjkh', 'kghjh', 58765, 1),
(47, 'fgjkh', 'kghjh', 58765, 1),
(47, 'fgjkh', 'kghjh', 58765, 1),
(45, 'fj', 'fdjf', 45, 1),
(45, 'fj', 'fdjf', 45, 1),
(67, 'fdjf', 'fjg', 45, 1),
(67, 'fdjf', 'fjg', 45, 1),
(456, 'rjhd', 'fjg', 6, 1),
(675, 'fgtjkgf', 'fgjkf', 65, 1),
(675, 'fgtjkgf', 'fgjkf', 65, 1),
(456, 'hfd', 'fgjhfd', 456, 4),
(123, 'karthi', 'maths', 34, 5),
(123, 'karthi', 'science', 45, 5);

-- --------------------------------------------------------

--
-- Table structure for table `studentdetails`
--

CREATE TABLE IF NOT EXISTS `studentdetails` (
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL,
  `age` varchar(3) NOT NULL,
  `college` varchar(20) NOT NULL,
  `degree` varchar(20) NOT NULL,
  `city` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `studentdetails`
--

INSERT INTO `studentdetails` (`name`, `email`, `password`, `age`, `college`, `degree`, `city`) VALUES
('fgsd', 'dsfg@sdh', 'sdfhgdfhfdh', '45', 'fhfdj', 'jffgj', 'djfg'),
('asdgsd', 'sadgsfg@sdhf', 'fdshfgh', '35', 'sdhdsh', 'sdgfds', 'sdfhdf'),
('fghfg', 'fdd@jfgfghjk', 'fdjfg', '78', 'fghfg', 'fdhfhg', 'fdhfdas'),
('karthi', 'karthi@gmail.com', '123456', '22', 'annauniversity', 'be', 'chennai'),
('WTFGERT', 'SH@dfghds', 'sfdhfsfgh', '56', 'dfjfdjdfh', 'dfjgjgf', 'hdgjghf'),
('awgsdgth', 'dfjfg@gfkj', 'fgkgkgf', '47', 'hkjlhg', 'hgkhgl', 'hlhgl'),
('fghfdj', 'fgjlhgl@hkg', 'hglkhglkhg', '65', 'ghlll,g', 'ghlhglg', 'ghlhgljhl');

-- --------------------------------------------------------

--
-- Table structure for table `student_details`
--

CREATE TABLE IF NOT EXISTS `student_details` (
  `id` int(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `class` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student_details`
--

INSERT INTO `student_details` (`id`, `name`, `class`) VALUES
(70, '[p', 5),
(456, 'rjfd', 3),
(544, 'dshdf', 3),
(2565, 'jnkjfh', 4),
(3646, 'rtujfyh', 3),
(4564, 'dfj', 4),
(4575, 'fgkh', 1),
(4675, 'rkgfk', 4),
(5447, 'dfjf', 1),
(5685, 'utr', 1),
(5868, 'khgjghjk', 4),
(7854, 'fgujgf', 3),
(12345, 'karthi', 5),
(43654, 'tujh', 1),
(45643, 'fhjfg', 3),
(46465, '645446', 1),
(436354, 'sdhysfd', 4),
(456743, 'fjuhfg', 1),
(678956, 'yhp;yu', 1);

-- --------------------------------------------------------

--
-- Table structure for table `test`
--

CREATE TABLE IF NOT EXISTS `test` (
  `id` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
