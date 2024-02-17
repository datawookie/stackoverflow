USE mysql;

CREATE TABLE `vodovod_ulice` (
  `id` int NOT NULL AUTO_INCREMENT,
  `naziv` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `naziv` (`naziv`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

insert into vodovod_ulice (naziv) values ('Ulica Vuka Karadžića');
