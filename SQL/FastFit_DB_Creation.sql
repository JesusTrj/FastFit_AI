drop table if exists Garments;
drop table if exists Outfit;
drop table if exists Users;

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
formality int,
weather int,
foreign key (Users_ID) references Users(ID)
);

create table Outfit (
user_ID int,
top_ID int,  
bottom_ID int,  
formality int,
weather int,
color float, 
user_rate float,
model_rate float
);

-- Insert Query
-- 


