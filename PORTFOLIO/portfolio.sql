-- phpMyAdmin SQL Dump
-- version 4.9.3
-- https://www.phpmyadmin.net/
--
-- ホスト: localhost:8889
-- 生成日時: 2020 年 3 月 27 日 04:18
-- サーバのバージョン： 5.7.26
-- PHP のバージョン: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- データベース: `portfolio`
--

-- --------------------------------------------------------

--
-- テーブルの構造 `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- テーブルのデータのダンプ `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('238fb1fe30f9');

-- --------------------------------------------------------

--
-- テーブルの構造 `login`
--

CREATE TABLE `login` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- テーブルのデータのダンプ `login`
--

INSERT INTO `login` (`id`, `username`, `password`) VALUES
(1, 'test', 'test'),
(2, 'A-friend', 'A-friwend'),
(3, 'B-friend', 'B-friend'),
(4, 'testetest', 'testtest');

-- --------------------------------------------------------

--
-- テーブルの構造 `post`
--

CREATE TABLE `post` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `photopost` varchar(200) NOT NULL,
  `tagpost` varchar(200) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `login_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- テーブルのデータのダンプ `post`
--

INSERT INTO `post` (`id`, `username`, `photopost`, `tagpost`, `created_at`, `updated_at`, `login_id`) VALUES
(1, 'test', 'jam_03.png', '', '2020-03-26 12:18:02', '2020-03-26 12:18:02', 1),
(2, 'test', 'jam_03.png', '#jam', '2020-03-26 12:18:08', '2020-03-26 12:18:08', 1),
(3, 'test', 'jam_04.png', '#jam2', '2020-03-26 12:26:16', '2020-03-26 12:26:16', 1),
(4, 'B-friend', '572A6A83-A525-49EB-B961-4D2B774E8C51.jpeg', '#lake', '2020-03-26 15:14:31', '2020-03-26 15:14:31', 3),
(5, 'B-friend', 'sample1.png', 'sample', '2020-03-26 15:41:07', '2020-03-26 15:41:07', 3),
(6, 'B-friend', '3.png', 'flog', '2020-03-26 15:43:41', '2020-03-26 15:43:41', 3),
(7, 'test', 'pig.png', '#pig', '2020-03-26 15:57:33', '2020-03-26 15:57:33', 1),
(8, 'test', 'girl.png', '#girl', '2020-03-26 15:59:35', '2020-03-26 15:59:35', 1),
(9, 'test', 'pinokio.png', '#pinokio', '2020-03-26 16:02:35', '2020-03-26 16:02:35', 1),
(10, 'test', '2.gif', '#2', '2020-03-27 09:17:01', '2020-03-27 09:17:01', 1),
(11, 'test', 'pinokio.png', '#pinokiosan', '2020-03-27 11:56:22', '2020-03-27 11:56:22', 1);

-- --------------------------------------------------------

--
-- テーブルの構造 `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(50) NOT NULL,
  `login_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- テーブルのデータのダンプ `users`
--

INSERT INTO `users` (`id`, `email`, `name`, `username`, `password`, `login_id`) VALUES
(1, 'test@test', 'test', 'test123', 'test', 1),
(2, 'A-friend@friend', 'A-friend', 'A-friend', 'A-friend', 2),
(3, 'B-friend@friend', 'B-friend', 'B-friend', 'B-friend', 3),
(4, 'testtest@testq', 'testtest', 'testetest', 'testtest', 4);

--
-- ダンプしたテーブルのインデックス
--

--
-- テーブルのインデックス `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- テーブルのインデックス `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`id`);

--
-- テーブルのインデックス `post`
--
ALTER TABLE `post`
  ADD PRIMARY KEY (`id`),
  ADD KEY `login_id` (`login_id`);

--
-- テーブルのインデックス `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD KEY `login_id` (`login_id`);

--
-- ダンプしたテーブルのAUTO_INCREMENT
--

--
-- テーブルのAUTO_INCREMENT `login`
--
ALTER TABLE `login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- テーブルのAUTO_INCREMENT `post`
--
ALTER TABLE `post`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- テーブルのAUTO_INCREMENT `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- ダンプしたテーブルの制約
--

--
-- テーブルの制約 `post`
--
ALTER TABLE `post`
  ADD CONSTRAINT `post_ibfk_1` FOREIGN KEY (`login_id`) REFERENCES `login` (`id`);

--
-- テーブルの制約 `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`login_id`) REFERENCES `login` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
