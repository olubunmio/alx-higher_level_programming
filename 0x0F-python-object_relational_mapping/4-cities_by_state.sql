-- Create database `hbtn_0e_4_usa`
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;

-- Create `states` table with some data
CREATE TABLE IF NOT EXISTS states (
       id INT NOT NULL AUTO_INCREMENT,
       name VARCHAR(256) NOT NULL,
       PRIMARY KEY (id)
);
-- Insert values into `states` table
INSERT INTO states (name) VALUES ('California'),
       	    	   	  	 ('Arizona'),
				 ('Texas'),
				 ('New York'),
				 ('Nevada');



-- Create `cities` table with some data
CREATE TABLE IF NOT EXISTS cities (
       id INT NOT NULL AUTO_INCREMENT,
       state_id INT NOT NULL,
       name VARCHAR(256) NOT NULL,
       PRIMARY KEY (id),
       FOREIGN KEY(state_id) REFERENCES states(id)
);
-- Insert values into `cities` table
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"),
       	    	   	      	    	   (1, "san Jose"),
					   (1, "Los Angeles"),
					   (1, "Fremont"),
					   (1, "Livermore");

INSERT INTO cities (state_id, name) VALUES (2, "Page"),
       	    	   	      	    	   (2,"Phoenix");

INSERT INTO cities (state_id, name) VALUES (3, "Dallas"),
       	    	   	      	    	   (3, "Houston"),
					   (3, "Austin");

INSERT INTO cities (state_id, name) VALUES (4, "New York");

INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"),
       	    	   	      	    	   (5, "Reno"),
					   (5, "Henderson"),
					   (5, "Carson City");
