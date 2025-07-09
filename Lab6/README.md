# CloudComputing_Lab6_SakshiPathrikar

1. Introduction To your project
    1. This project demonstrates containerization of the SQL Scripts written for the my_guitar_shop database

2. Description of your project
    1. . The project consists of a docker compose which is used to containerize a set of SQL queries executed on the my_guitar_shop database, which includes tables such as:
        1. addresses
        2. administrators
        3. categories
        4. customers
        5. orders
        6. order_items
        7. products

3. Design of your project
    1. This project contains a docker compose file that connects docker to the my_guitar_shop database and shows the tables and the database in docker. 

4. Detailed instructions on how to run your project
    1. To create an image of this project in docker:
        1. Clone the repository in source code editor of choice
        2. cd into Lab 6 folder
        3. Enter the command docker-compose -f DockerCompose.yaml up in the terminal of the source code editor
        4. Open Docker and a folder called Lab6 should be there in the container section and from actions run the container
        5. Then open the terminal in Docker and  enter the command: docker exec -it sqlScripts mysql -uroot -p
        6. It should ask for a password and the password is Sakshi@1234. This should log into mysql
        7. But mysql won't have any data yet, so go in dbeaver, open a new connection choose port 3307 with the password Sakshi@1234, change the permissions for    public key retrival to true under driver properties tab.
        8. Then open a new sql script load the my_guitar_shop by running the createguitar script.
        9. Then, run the Lab5_Scripts and you should be able to see the results.