-- Drop all trainee tables
Drop TABLE FoodCategory cascade constraints;
Drop TABLE FoodItem cascade constraints;
Drop TABLE CheckoutCart cascade constraints;
Drop Table User_Transactions cascade constraints;


-- Table for storing FoodCategory dNAils 
CREATE TABLE FoodCategory (
  FCId          	INTEGER PRIMARY KEY,
  Category_Name  VARCHAR2(40) ,
  Restaurant_Type CHAR(2) CHECK ( Restaurant_Type IN ('V' , 'NV'))
);

-- Data for FoodCategory table  --
------------------------------
INSERT INTO FoodCategory (FCID,Category_Name,Restaurant_Type) VALUES (1,'Chicken' , 'NV');
INSERT INTO FoodCategory (FCID,Category_Name,Restaurant_Type) VALUES (2,'Fish' , 'NV');
INSERT INTO FoodCategory (FCID,Category_Name,Restaurant_Type) VALUES (3,'Mutton' , 'NV');
INSERT INTO FoodCategory (FCID,Category_Name,Restaurant_Type) VALUES (4,'Sea Food' , 'NV');
INSERT INTO FoodCategory (FCID,Category_Name,Restaurant_Type) VALUES (5,'Egg' , 'NV');
INSERT INTO FoodCategory (FCID,Category_Name,Restaurant_Type) VALUES (6,'Vegetarian', 'V');
INSERT INTO FoodCategory (FCID,Category_Name,Restaurant_Type) VALUES (7,'Starters', 'V');


select * from FoodCategory;

commit;



CREATE TABLE FoodItem (
  Id          	INTEGER PRIMARY KEY,
  FoodName    	VARCHAR2(40)  ,
  Food_Type  CHAR(2)  CHECK(Food_Type IN ('V','NV')),
  Price      	DECIMAL(9,2)  ,
  Availability  CHAR(2)  CHECK(Availability IN ('A','NA')),
  Restaurant_Name VARCHAR2(40)  ,
  Category_Name VARCHAR2(40) 
);

-- Data for FoodItem table  --
------------------------------


INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (1,'Chicken Fry' , 'NV',500,'A' ,'KAMAT HOTEL' , 'Chicken');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (2,'Fish' , 'NV',900,'NA' ,'MODERN RESTAURANT' , 'Fish' );
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (3,'Mutton' , 'NV',250,'NA' ,'BIRYANI HOUSE', 'Mutton');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (4,'Sea Food' , 'NV',300,'NA' ,'SUKH SAGAR' , 'Sea Food');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (5,'Egg' , 'NV',400,'A' ,'KAMAT HOTEL' , 'Chicken');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (6,'Vegetarian', 'NV',350,'NA' ,'KAMAT HOTEL' , 'Vegetarian');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (7,'Starters', 'V',507,'A' ,'MODERN RESTAURANT' , 'Starters');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (8,'Paneer', 'V',300,'A' ,'KAMAT HOTEL' , 'Vegetarian');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (9,'Green Peas', 'V',180,'A' ,'KAMAT HOTEL' , 'Vegetarian');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (10,'Bhindi Masala', 'V',280,'A' ,'KAMAT HOTEL' , 'Vegetarian');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (11,'Chicken Tawa' , 'NV',700,'A' ,'SUKH SAGAR' , 'Chicken');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (12,'Bhindi Masala', 'V',280,'A' ,'KAMAT HOTEL' , 'Egg');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (13,'Promphet Masala', 'NV',780,'A' ,'KAMAT HOTEL' , 'Sea Food');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (14,'Lamb Masala', 'NV',880,'A' ,'KAMAT HOTEL' , 'Mutton');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (15,'Masala Papad', 'V',80,'A' ,'KAMAT HOTEL' , 'Starters');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (16,'Manchurian Dry', 'V',120,'A' ,'KAMAT HOTEL' , 'Starters');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (17,'Fish' , 'NV',900,'NA' ,'MODERN RESTAURANT' , 'Fish' );
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (18,'Bhindi Do Pyaza', 'V',280,'A' ,'KAMAT HOTEL' , 'Egg');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (19,'Mackarel Masala', 'NV',780,'A' ,'KAMAT HOTEL' , 'Sea Food');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (20,'Lamb Roast', 'NV',880,'A' ,'KAMAT HOTEL' , 'Mutton');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (21,'Chineese Bhel', 'V',50,'A' ,'KAMAT HOTEL' , 'Starters');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (22,'Gobi Manchurian', 'V',120,'A' ,'KAMAT HOTEL' , 'Starters');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (23,'Bombay Duck' , 'NV',300,'NA' ,'SUKH SAGAR' , 'Fish' );
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (24,'Fish Curry' , 'NV',800,'NA' ,'MODERN RESTAURANT' , 'Fish' );
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (25,'Mutton Gravy' , 'NV',550,'NA' ,'BIRYANI HOUSE', 'Mutton');
commit;



INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (26,'Papad', 'V',180,'A' ,'KAMAT HOTEL' , 'Starters');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (27,'Masala', 'V',60,'NA' ,'KAMAT HOTEL' , 'Starters');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (28,'Papad', 'V',80,'A' ,'KAMAT' , 'Starters');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (29,'Bombay Duck', 'V',280,'NA' ,'KAMAT' , 'Starters');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (30,'Raitha', 'V',40,'A' ,'KAMAT' , 'Starters');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (31,'Chineese Bhel', 'V',80,'NA' ,'MODERN' , 'Starters');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (32,'FishTai', 'NV',80,'A' ,'KAMAT' , 'Fish');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (33,'Masala', 'V',80,'NA' ,'MODERN' , 'Chicken');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (34,'Chicken', 'NV',80,'A' ,'KAMAT' , 'Chicken');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (35,'Egg', 'NV',80,'NA' ,'KAMAT' , 'Starters');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (36,'Papad', 'V',80,'A' ,'MODERN' , 'Starters');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (37,'Bombay Duck', 'NV',80,'NA' ,'MODERN' , 'Fish');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (38,'Egg', 'NV',80,'A' ,'MODERN' , 'Starters');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (39,'Bhel', 'V',80,'NA' ,'MODERN' , 'Starters');
INSERT INTO FoodItem (ID,FoodName,Food_Type,Price,Availability,Restaurant_Name,Category_Name ) VALUES (40,'Mutton', 'V',80,'NA' ,'MODERN' , 'Mutton');



commit;










commit;

select * from fooditem;
select * from FoodCategory;
select * from restaurants;
select * from Registration;

select ID,FoodName,Price,Availability,Restaurant_Name,Category_Name from FoodItem ;

-- Join both tables from restaurant & fooditems
select * from fooditem fi join restaurants rt on fi.Restaurant_Name = rt.RestaurantName;


-- For getting category from restaurant 

select unique category_name from fooditem where restaurant_name = 'KAMAT HOTEL' ;

-- For getting data from fooditem where restaurant_name & category wise select
select foodname , price , availability from fooditem where restaurant_name = 'KAMAT HOTEL' and category_name = 'Chicken';

-- Check whether the given items are available from fooditem  
select availability from fooditem where foodname in ( 'Fish' , 'Egg' , 'Vegetarian' );

--Sp

ecific Availability
select availability from fooditem where foodname = 'Masala Papad' and restaurant_name = 'KAMAT HOTEL' ;

select availability from fooditem where foodname = 'Papad' and restaurant_name = 'KAMAT' ;



-- Inserting Values with Quantity into CheckoutCart Table
select * from checkoutcart;

insert into checkoutcart(username ,foodname , quantity) values ('Kautilya','Masala', 200);


select * from checkoutcart;
delete from checkoutcart where username = 'Kautilya' and foodname = 'Masala' ;
delete from checkoutcart where username = 'Kautilya' and foodname = 'Papad';
 
--Deleting the cart from the table
delete from checkoutcart where username =:'user_n';

-- SQL Python query





cur.execute("delete from checkoutcart where username =:user_n",{"user_n": username})
 
select * from checkoutcart;

select * from checkoutcart where username = 'Mains';

CREATE TABLE CheckoutCart (
  Username         VARCHAR2(40),
  FoodName    	VARCHAR2(40)  ,
  quantity  INTEGER  ,
  Price      	DECIMAL(9,2)  ,
  total_price INTEGER ,
  Restaurant_Name VARCHAR2(40) 
);


INSERT INTO CheckoutCart (Username,FoodName,quantity,Price) VALUES ( 'Rohita' , 'Chicken Fry' , 2 ,300);
INSERT INTO CheckoutCart (Username,FoodName,quantity,Price) VALUES ( 'Kautilya' , 'Fish' , 2 ,400);
INSERT INTO CheckoutCart (Username,FoodName,quantity,Price) VALUES ( 'George' , 'Fish' , 3 ,440);
INSERT INTO CheckoutCart (Username,FoodName,quantity,Price) VALUES ( 'Alex' , 'Fish' , 2 ,234);
INSERT INTO CheckoutCart (Username,FoodName,quantity,Price) VALUES ( 'Mains' , 'Fish' , 4 ,650);

commit;



select * from checkoutcart;





-- For Module 5 Common Module 


Drop Table User_Transactions cascade constraints;

CREATE TABLE User_Transactions (
  Username         VARCHAR2(40) PRIMARY KEY,
  Order_count    	INTEGER  ,
  Overall_total_price  INTEGER 
);


INSERT INTO User_Transactions (Username,Order_count,Overall_total_price) VALUES ( 'Rohita', 27 ,30078);
INSERT INTO User_Transactions (Username,Order_count,Overall_total_price) VALUES ( 'Kautilya', 134, 342078);
INSERT INTO User_Transactions (Username,Order_count,Overall_total_price) VALUES ( 'Gaurav', 64 ,540078);
INSERT INTO User_Transactions (Username,Order_count,Overall_total_price) VALUES ( 'Anand', 543 ,1390338);
INSERT INTO User_Transactions (Username,Order_count,Overall_total_price) VALUES ( 'Komal', 7 ,3078);
INSERT INTO User_Transactions (Username,Order_count,Overall_total_price) VALUES ( 'Vaibhav', 27 ,34353);
INSERT INTO User_Transactions (Username,Order_count,Overall_total_price) VALUES ( 'Razi', 17 ,21078);
INSERT INTO User_Transactions (Username,Order_count,Overall_total_price) VALUES ( 'Rohini', 37 ,30078);
INSERT INTO User_Transactions (Username,Order_count,Overall_total_price) VALUES ( 'Kaustub', 44 ,334078);
INSERT INTO User_Transactions (Username,Order_count,Overall_total_price) VALUES ( 'Saurav', 23 ,740078);
INSERT INTO User_Transactions (Username,Order_count,Overall_total_price) VALUES ( 'Kumar', 323 ,390338);
INSERT INTO User_Transactions (Username,Order_count,Overall_total_price) VALUES ( 'Jal', 7 ,3078);
INSERT INTO User_Transactions (Username,Order_count,Overall_total_price) VALUES ( 'Vishal', 57 ,33453);
INSERT INTO User_Transactions (Username,Order_count,Overall_total_price) VALUES ( 'Gazi', 28 ,22078);
INSERT INTO User_Transactions (Username,Order_count,Overall_total_price) VALUES ( 'Kaushal', 44 ,334078);
INSERT INTO User_Transactions (Username,Order_count,Overall_total_price) VALUES ( 'Ritvik', 23 ,740078);
INSERT INTO User_Transactions (Username,Order_count,Overall_total_price) VALUES ( 'Ramesh', 233 ,14038);
INSERT INTO User_Transactions (Username,Order_count,Overall_total_price) VALUES ( 'Suresh', 72 ,23078);
INSERT INTO User_Transactions (Username,Order_count,Overall_total_price) VALUES ( 'Vignesh', 57 ,33453);
INSERT INTO User_Transactions (Username,Order_count,Overall_total_price) VALUES ( 'Gaziy', 218 ,12378);
commit;




select * from User_Transactions;

--Module 5 - Module 1 Functionality




--Module 5 - Module 2 Functionality

select username, max(order_count) from User_Transactions group by username;

select username from User_Transactions where order_count = ( select max(order_count) from User_Transactions);


--Module 5 - Module 3 Functionality





--Komal queries done before module 4. Remember to execute
--Update the count values of transactions in table User_Transactions from Module 4 when the TRANSACTION is completed
select order_count from User_Transactions where username = 'Kautilya';

update User_Transactions set order_count = :inc_order_count where username = 'Kautilya';


--Update the total overall price values of transactions in table User_Transactions from Module 4 when the TRANSACTION is completed
select Overall_total_price from User_Transactions where username = 'Kautilya';

where restaurant_name =:restaurant_n and category_name =:category_n",{"restaurant_n":restaurant_name, "category_n":category_name })

cur.execute("update User_Transactions set Overall_total_price = :inc_overall_total_price where username = 'Kautilya'",{"inc_overall_total_price" : overall_total_inc_price}")