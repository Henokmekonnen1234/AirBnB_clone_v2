-- This query we will create a database called hbnnb_dev_db, it will store datas
-- A user who can access the datas with the name hbnb_dev
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS "hbnb_dev"@"localhost"
IDENTIFIED BY "hbnb_dev_pwd";
GRANT ALL ON hbnb_dev_db.* TO "hbnb_dev"@"localhost";
GRANT USAGE ON *.* TO "hbnb_dev"@"localhost";
GRANT SELECT ON performance_schema.* TO "hbnb_dev"@"localhost";
