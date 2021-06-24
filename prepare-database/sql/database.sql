-- drop database test_1;

create database test_1;

create table people (
  `id` bigint unsigned not null auto_increment,
  `nome` varchar(200) not null,
  `sexo` varchar(9) not null,
  `email` varchar(200) not null,
  `cpf` varchar(11) not null,
  `rg` varchar(15) not null,
  `celular` varchar(15) not null,
  `cep` varchar(20) not null,
  `endereco` varchar(200) not null,
  `numero` varchar(10) not null,
  `bairro` varchar(75) not null,
  `cidade` varchar(100) not null,
  `estado` varchar(4) not null,
  `peso` varchar(5) not null,
  `tipo_sanguineo` varchar(3) not null,
  `data_nasc` date not null, -- yyyy-dd-mm

  primary key (`id`)
);

select * from people;
