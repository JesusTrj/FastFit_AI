CREATE DATABASE hackmty_fit;

Use hackmty_fit;

drop table if exists Users;
drop table if exists Garments;
drop table if exists Outfit;

create table Users (
ID int primary key,
Users_Name varchar(255),
Last_Name varchar(255),
Email varchar(255)
);

create table Garments (
ID int primary key,
user_ID int not null,
img_path varchar(255) not null,
garment_type int,      /*blouse, tshirt, dress, short, etc*/
garment_category int,  /*top or bottom*/
formality int,         /*sport, casual, formal*/
weather int,           /*sunny, cold, rainny*/
foreign key (user_ID) references Users(ID)
);

create table Outfit (
user_ID int,
top_ID int,  
bottom_ID int,  
formality int,
weather int,
color float,
is_favorite bool, /*not used in training*/
user_rate float,  
model_rate float  /*preferably not used in training models*/
);