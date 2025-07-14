# CloudComputing_Lab7_SakshiPathrikar

1. Introduction To your project:
    1. This project implements a python command line driver that executes sql queries from Lab 5, either on docker or locally. It also includes a built-in testing framework for verifying query correctness using a separate test module.

2. Description of your project:
    1. The project consists of a set of SQL queries executed on the my_guitar_shop database using a python command line driver, which includes tables such as:
        1. addresses
        2. administrators
        3. categories
        4. customers
        5. orders
        6. order_items
        7. products

3. Design of your project:
    1. The cli.py file executes the command line driver and it includes the connection between python and mysql using the cursor object.
        1. While making the connection to mysql, I have also added the port parameter which helps connect to port 3307 which is the docker port or 3306 which is the local port. 
    2. The docker compose file is used to connect docker to the my_guitar_shop database and shows the tables and the database in docker. 
    3. The tests.py file includes TestDatabase class that validates the accuracy and expected behavior of 10 SQL queries using automated tests.

4. Detailed instructions on how to run your project:
    1. To run this project on port 3306, which is the local instance :
        1. In cli.py, change the port number to 3306.
        2. Then if using pycharm, right click and select run, if using vs code click the run button from the top right hand corner.
        3. Then in the terminal all the queries should be displayed and enter the key (number next to the query) of the query you want to run and you shouldd see the output.
        4. When you want to exit the driver enter 0.
    2. To run this project on port 3307, which is the docker instance: 
        1. Make sure port in cli.py file is 3307.
        2. If you have the docker instance already setup: 
            1. If using pycharm, right click and select run, if using vs code click the run button from the top right hand corner.
            2. Then in the terminal all the queries should be displayed and enter the key (number next to the query) of the query you want to run and you shouldd see the output.
            3. When you want to exit the driver enter 0.
            4. To run the tests enter 11.
        3. If docker instance is not set up: 
            1. cd into Lab 7 folder
            2. Enter the command docker-compose -f DockerCompose.yaml up in the terminal of the source code editor
            3. Open Docker and a folder called Lab6 should be there in the container section and from actions run the container
            4. Then open the terminal in Docker and  enter the command: docker exec -it sqlScripts mysql -uroot -p
            5. It should ask for a password and the password is Sakshi@1234. This should log into mysql
            6. But mysql won't have any data yet, so go in dbeaver, open a new connection choose port 3307 with the password Sakshi@1234, change the permissions for public key retrival to true under driver properties tab
            7. Then open a new sql script load the my_guitar_shop by running the createguitar script. 
            8. Then in pycharm or vs code, If using pycharm, right click and select run, if using vs code click the run button from the top right hand corner.
            9. Then in the terminal all the queries should be displayed and enter the key (number next to the query) of the query you want to run and you shouldd see the output.
            10. When you want to exit the driver enter 0.
            11. To run the tests enter 11.