-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 24, 2020 at 09:01 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pt_presisi`
--

-- --------------------------------------------------------

--
-- Table structure for table `bekerja`
--

CREATE TABLE `bekerja` (
  `id_proyek` varchar(15) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `namaProyek` varchar(50) DEFAULT NULL,
  `deadline` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bekerja`
--

INSERT INTO `bekerja` (`id_proyek`, `nama`, `namaProyek`, `deadline`) VALUES
('1a1', 'Alya', 'Proyek Berjalan Bersama', NULL),
('1a1', 'Holly', 'Proyek Berjalan Bersama', NULL),
('2b2', 'Alya', 'Proyek Milestone 3', NULL),
('2b2', 'Holly', 'Proyek Milestone 3', '2020-11-23 23:59:59');

-- --------------------------------------------------------

--
-- Table structure for table `pekerja`
--

CREATE TABLE `pekerja` (
  `ID_telegram` varchar(40) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `divisi` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pekerja`
--

INSERT INTO `pekerja` (`ID_telegram`, `nama`, `divisi`) VALUES
('1406537907', 'Alya', 'Sekretaris'),
('2', 'Denny', 'HR'),
('4', 'Shofu', 'Sekretaris'),
('5', 'notAlya', 'notSekretaris'),
('935037005', 'Holly', 'HR');

-- --------------------------------------------------------

--
-- Table structure for table `progress`
--

CREATE TABLE `progress` (
  `id_proyek` varchar(15) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `namaProyek` varchar(50) DEFAULT NULL,
  `progress` varchar(100) DEFAULT NULL,
  `waktuprogress` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `progress`
--

INSERT INTO `progress` (`id_proyek`, `nama`, `namaProyek`, `progress`, `waktuprogress`) VALUES
('2b2', 'Holly', 'Proyek Milestone 3', 'Menginisialisasi basis data baru', '2020-11-22 22:28:43'),
('2b2', 'Holly', 'Proyek Milestone 3', 'Menginisialisasi basis data 2.0 baru juga tapi ngetes', '2020-11-22 22:28:55'),
('2b2', 'Holly', 'Proyek Milestone 3', 'Menginisialisasi basis data 3.0 baru juga tapi ngetes ketiga kali huehueheeh', '2020-11-22 22:29:10');

-- --------------------------------------------------------

--
-- Table structure for table `proyek`
--

CREATE TABLE `proyek` (
  `ID_proyek` varchar(15) NOT NULL,
  `namaProyek` varchar(50) NOT NULL,
  `deskripsi` varchar(200) DEFAULT NULL,
  `startdate` datetime DEFAULT NULL,
  `deadline` datetime DEFAULT NULL,
  `jenisProyek` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `proyek`
--

INSERT INTO `proyek` (`ID_proyek`, `namaProyek`, `deskripsi`, `startdate`, `deadline`, `jenisProyek`) VALUES
('1a1', 'Proyek Berjalan Bersama', 'Proyek ini menjadi sebuah data inisialisasi di dalam sebuah database sql blablabla gatau nulis apa lagi', '2020-11-22 22:24:01', '2020-11-24 23:59:59', 'inisialisasi data'),
('2b2', 'Proyek Milestone 3', 'Proyek ini menjadi sebuah data inisialisasi kedua yey semangat gais nugasnya', '2020-11-22 22:24:48', '2020-11-23 23:59:59', 'inisialisasi data');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bekerja`
--
ALTER TABLE `bekerja`
  ADD PRIMARY KEY (`id_proyek`,`nama`),
  ADD KEY `nama` (`nama`),
  ADD KEY `namaProyek` (`namaProyek`);

--
-- Indexes for table `pekerja`
--
ALTER TABLE `pekerja`
  ADD PRIMARY KEY (`ID_telegram`),
  ADD UNIQUE KEY `nama_unik_const` (`nama`);

--
-- Indexes for table `progress`
--
ALTER TABLE `progress`
  ADD PRIMARY KEY (`id_proyek`,`nama`,`waktuprogress`),
  ADD KEY `nama` (`nama`),
  ADD KEY `namaProyek` (`namaProyek`);

--
-- Indexes for table `proyek`
--
ALTER TABLE `proyek`
  ADD PRIMARY KEY (`ID_proyek`),
  ADD UNIQUE KEY `namaProyek` (`namaProyek`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bekerja`
--
ALTER TABLE `bekerja`
  ADD CONSTRAINT `bekerja_ibfk_1` FOREIGN KEY (`id_proyek`) REFERENCES `proyek` (`ID_proyek`),
  ADD CONSTRAINT `bekerja_ibfk_2` FOREIGN KEY (`nama`) REFERENCES `pekerja` (`nama`),
  ADD CONSTRAINT `bekerja_ibfk_3` FOREIGN KEY (`namaProyek`) REFERENCES `proyek` (`namaProyek`);

--
-- Constraints for table `progress`
--
ALTER TABLE `progress`
  ADD CONSTRAINT `progress_ibfk_1` FOREIGN KEY (`nama`) REFERENCES `bekerja` (`nama`),
  ADD CONSTRAINT `progress_ibfk_2` FOREIGN KEY (`namaProyek`) REFERENCES `bekerja` (`namaProyek`),
  ADD CONSTRAINT `progress_ibfk_3` FOREIGN KEY (`id_proyek`) REFERENCES `bekerja` (`id_proyek`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
