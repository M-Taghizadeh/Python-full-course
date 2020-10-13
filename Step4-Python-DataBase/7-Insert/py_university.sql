-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 02, 2020 at 08:38 PM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.3.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `py_university`
--

-- --------------------------------------------------------

--
-- Table structure for table `faculty`
--

CREATE TABLE `faculty` (
  `Faculty_ID` int(11) NOT NULL,
  `Faculty_name` varchar(30) DEFAULT NULL,
  `Faculty_Admin` varchar(30) DEFAULT NULL,
  `YearOfFundation` char(4) DEFAULT NULL,
  `Faculty_Address` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `faculty`
--

INSERT INTO `faculty` (`Faculty_ID`, `Faculty_name`, `Faculty_Admin`, `YearOfFundation`, `Faculty_Address`) VALUES
(1, 'Computer Faculty', 'Dr Karimi', '1378', 'Tehran'),
(2, 'Software Engineering Faculty', 'Dr Karimi', '1378', 'Tehran'),
(3, 'Art Faculty', 'Dr Mohammadi', '1381', 'Mashhad'),
(4, 'Math Faculty', 'Dr Alavi', '1390', 'Tabriz'),
(5, 'Industrial Faculty', 'Dr Rezaei', '1381', 'Esfehan'),
(6, 'Computer Faculty', 'Dr Ghasemi', '1370', 'Tehran');

-- --------------------------------------------------------

--
-- Table structure for table `field`
--

CREATE TABLE `field` (
  `Field_ID` int(11) NOT NULL,
  `Field_Name` varchar(30) DEFAULT NULL,
  `Orientation` varchar(30) DEFAULT NULL,
  `Course` varchar(30) DEFAULT NULL,
  `Faculty_ID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `field`
--

INSERT INTO `field` (`Field_ID`, `Field_Name`, `Orientation`, `Course`, `Faculty_ID`) VALUES
(1, 'Computer', 'Software', 'Bachelore', 6),
(2, 'Computer', 'Hardware', 'Master', 1),
(3, 'Computer', 'Software', 'Master', 6),
(4, 'Computer', 'Hardware', 'bachelor', 6);

-- --------------------------------------------------------

--
-- Table structure for table `master`
--

CREATE TABLE `master` (
  `Master_ID` int(11) NOT NULL,
  `Master_Name` varchar(30) DEFAULT NULL,
  `Master_Family` varchar(30) DEFAULT NULL,
  `Degree` varchar(20) DEFAULT NULL,
  `Field` varchar(30) DEFAULT NULL,
  `Faculty_Member` bit(1) DEFAULT NULL,
  `Faculty_ID` int(11) DEFAULT NULL,
  `Phone` char(11) DEFAULT NULL,
  `Address` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `master`
--

INSERT INTO `master` (`Master_ID`, `Master_Name`, `Master_Family`, `Degree`, `Field`, `Faculty_Member`, `Faculty_ID`, `Phone`, `Address`) VALUES
(1, 'hadi', 'mohammadi', 'dr', 'software', b'1', 6, '09115598844', 'Tehran'),
(2, 'reza', 'naseri', 'master', 'software', b'0', 1, '09323242424', 'Tehran'),
(3, 'ehsan', 'nazemi', 'dr', 'hardware', b'1', 6, '091213131', 'Guilan'),
(4, 'amir', 'samadi', 'master', 'software', b'0', 6, '09122322424', 'Tehran');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `Student_ID` int(11) NOT NULL,
  `Student_Name` varchar(30) NOT NULL,
  `Student_Family` varchar(30) NOT NULL,
  `Field_ID` int(11) NOT NULL,
  `Entrance_Year` char(4) DEFAULT NULL,
  `Address` varchar(50) DEFAULT NULL,
  `Average` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`Student_ID`, `Student_Name`, `Student_Family`, `Field_ID`, `Entrance_Year`, `Address`, `Average`) VALUES
(1, 'mohammad', 'amiri', 1, '1395', 'Guilan', 18),
(2, 'mahdi', 'mirzaei', 2, '1390', 'Tehran', 17),
(3, 'sara', 'nasiri', 1, '1397', 'Guilan', 16),
(4, 'nasim', 'mottahari', 4, '1395', 'Tehran', 19.5),
(5, 'nasrin', 'azizi', 2, '1389', 'Guilan', 11),
(6, 'nastaran', 'mostafavi', 1, '1390', 'Tehran', 15);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `faculty`
--
ALTER TABLE `faculty`
  ADD PRIMARY KEY (`Faculty_ID`);

--
-- Indexes for table `field`
--
ALTER TABLE `field`
  ADD PRIMARY KEY (`Field_ID`),
  ADD KEY `Faculty_ID` (`Faculty_ID`);

--
-- Indexes for table `master`
--
ALTER TABLE `master`
  ADD PRIMARY KEY (`Master_ID`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`Student_ID`),
  ADD KEY `Field_ID` (`Field_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `master`
--
ALTER TABLE `master`
  MODIFY `Master_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `Student_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `field`
--
ALTER TABLE `field`
  ADD CONSTRAINT `field_ibfk_1` FOREIGN KEY (`Faculty_ID`) REFERENCES `faculty` (`Faculty_ID`);

--
-- Constraints for table `student`
--
ALTER TABLE `student`
  ADD CONSTRAINT `student_ibfk_1` FOREIGN KEY (`Field_ID`) REFERENCES `field` (`Field_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
