CREATE DATABASE hackmty_fit;

Use hackmty_fit;

drop table if exists Users;
drop table if exists Garments;
drop table if exists Outfit;

create table Users (
user_ID int AUTO_INCREMENT  primary key,
Users_Name varchar(255),
Last_Name varchar(255),
Email varchar(255),
UNIQUE (Email)
);


create table Garments (
garment_ID int AUTO_INCREMENT  primary key,
user_ID int not null,
img_path varchar(1000) not null,
garment_type varchar(255),      /*blouse, tshirt, dress, short, etc*/
garment_category int,  /*top, bottom, shoes*/
formality int,         /*sport, casual, formal*/
weather int,           /*sunny, cold, rainny*/
foreign key (user_ID) references Users(user_ID)
);

create table Outfit (
outfit_ID int AUTO_INCREMENT  primary key,
user_ID int,
top_path varchar(1000),    
bottom_path varchar(1000),    
shoes_path varchar(1000),    
outfit_path varchar(1000),    
formality int,
weather int,
color float,
is_favorite bool, /*not used in training*/
user_rate float,  
model_rate float,  /*preferably not used in training models*/
title varchar(255),
fecha varchar(255),
descr varchar(255),
foreign key (user_ID) references Users(user_ID),
UNIQUE KEY `thekey` (`top_path`,`bottom_path`,`shoes_path`)
);
