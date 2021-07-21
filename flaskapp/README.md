#### This is a simple flask app which performs basic CRUD operations on a Relational Database -> MYSQL.The user can register using a username and password which starts a session for that user and add, edit and delete articles.

#### The libraries that are to be installed via pip3-
* flask
* Flask_WTF
* passlib

#### The sql-server can be installed by-
```py
sudo apt-get install mysql-server libmysqlclient-dev
```
#### Start the mysql-server -
```py
/usr/bin/mysql -u root -p
```
#### In Ubuntu systems running MySQL 5.7 (and later versions), the root MySQL user is set to authenticate using the auth_socket plugin by default rather than with a password. This allows for some greater security. In many cases,it can also complicate things when you need to allow an external program to access the user.Enter your password in 'password' to configure flask app with mysql-server.Use the commands.

```py
SELECT user,authentication_string,plugin,host FROM mysqluser;
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
FLUSH PRIVILEGES;
exit;
```
#### Use the password set in 
```py
app.config['MYSQL_PASSWORD]='your_password';
```
#### Creating the Database.
```py
CREATE DATABASE myflaskapp;
USE myflaskapp;
```
#### Database created for storing registeres users.
```py
CREATE TABLE users(id INT(11) AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100),email VARCHAR(100),username VARCHAR(30), password VARCHAR(100), register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
```
#### Database created for storing the articles for a user.
```py
CREATE TABLE articles(id INT(11) AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255),author VARCHAR(100),body TEXT, create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
SHOW TABLES;
```
#### To Run the app 
```py
python3 app.py 
```


