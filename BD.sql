create database instituto;
use instituto;
create table if not exists candidatos 
(id int auto_increment primary key,
nome varchar(30) not null,
data_nascimento date not null,
cpf varchar(20) not null unique
);

create table votos(
id_votos int auto_increment primary key,
votos varchar(50) default 0 not null,
id_candidato int,
foreign key (id_candidato) references candidatos (id)
);


