# CloudComputing_FinalProject: SakshiPathrikar and Davud Azizov

1. Introduction To your project
    1. This project is built to provide a cloud environment that a Software developer can use to create an application.

2. Description of your project
    1. There are 10 services that communicate with each other to make the local cloud environment. The 10 services are: Database Service, Dashboard Service,
    Maintain Pokemon Service, Maintain Types Service, Maintain Attacks Service, About Page Service, Identity Provider Service, Load Balancer Service, Post-Fix
    Service and Mail Hog Service. 

3. Design of your project
    1. The database service stores the information of the pokemon, types of pokemon and special attacks of pokemons. The Dashboard service shows a list of all pokemons, types and special attacks in the dataabase, also let's you add a new pokemon, new type or new special attack. The Post-Fix is an email service which sends an email whenever a new pokemon is added. Mail Hog is another service that captures the email sent by Post-Fix and users are able to view it. Maintain Pokemon, Maintain Types and Maintain Attacks are services which hellp maintain pokemons, types and special attacks. The Identity Provider is a service that checks if the pokemon that is being logged in is valid or not. The about page service gives information about the Pokemon Shop. 
    2. The was these services communicate is as follows: 
        1. Database Service - The database has tables that stores information about the pokemon, the types and the special attacks. It also maps pokemon and types tables and pokemon and special attacks tables in a one to many relationship.
        2. Identity Provider Service - When a user enters Pokemon Name and Level, it connects to the database to check if the pokemon with that level exsists or not.
        3. Dashboard Service - Once the identity provider verifies the pokemon, the dashboard service connects to the database to display a list of pokemons, list of the types and list of the special attacks.
        4. Maintain Pokemon Service - This service asks the user to enter pokemon name, level, select the type (which is retrived from the database and displayed), select specialattacks (which is retrived from the database and displayed) and then this record is inserted into the database. After a new record is formed in the database, the pokemon_id is retrived and the details of the newly added pokemon is displayed.
        5. Post-Fix - Once a new pokemon is generated, noreply@pokemon.com sends an email saying a new pokemon is generated.
        6. Mail Hog -  The email sent by Mail Hog is captured by Mail Hog service.
        7. Maintain Types - THis service asks the user to enter the name of the type and a description and then this record is inserted into the database.
        8. Maintain Attacks - This service asks the user to enter the name of the attacks and the power of this attack which is then inserted into the database. 
        9. About Page Service - THis page displays information about Pokemon Shop.
        10. Load Balance - The Load Balancer is implemented by ngnix. In the docker Compose file, there are two instances of fast api services created, one is mapped to 8081 and other is mapped to 8082. The load balancer uses the round robin technique to load balance between 8081 and 8082 on port 8080.

4. Detailed instructions on how to run your project
    1. First build the docker image by following these steps: 
        1. cd into Final_Project Folder in editor of choice.
        2. Enter the command "docker compose up --build" in the terminal of the editor.
    2. Once the docker container is running, 
        1. To run the the Database service:
            1. Once the docker container is up and running, go to MySql Workbench.
            2. In mysql workbench, add a new connection with port 3308 and name Pokemon Shop (or any name you like). 
            3. Once the connection is established, open the instance and open a new query. In the new query copy paste the script from DatabaseScript.sql file and run the query, this will add a database called pokemon_shop and it's tables. 
        2. To run the Load Balancer Service:
            1. For the Load Balancer service, once the docker container is up and running, in browser of your choice simply go navigate to http://localhost:8080/ and you will be able to see the login page. 
            2. Nginx helps load balance between two instances of the fast api service (fastapi-app1 and fastapi-app2) using the round robin method. To see which instance is running navigate to terminal and a message like "fastapi-app1         | INFO:     172.18.0.8:50862 - "GET / HTTP/1.0" 200 OK" or "fastapi-app2         | INFO:     172.18.0.8:37672 - "GET / HTTP/1.0" 200 OK" will be displayed.
        3. To run the identity provider service:
            1. Once you navigate to http://localhost:8080/ you will see the login page where you will be asked to enter the pokemon name (Pikachu for example) and level (15). 
            2. The service connects to the database to validate these credentials. If it exsists then you will be redirected to the dashboard service otherwise an error called invalid credentials will be shown. 
        4. To run the dashboard service: 
            1. Once the docker container is running, navigate to http://localhost:8080/ and login with Pikachu as username and 15 as level. 
            2. Once successfully logged in, you will be redirected to  the dashboard page.
            3. The dashboard page connects to the database and displays a list of all the pokemons, all the types and all the special attacks.
            4. On the dashboard page, there are also buttons to add a new pokemon, add a new type and a special attack which redirects to the maintain pokemon service, maintain types service and maintain special attack service respectively. 
        5. To run the Maintain pokemon service:
            1. Once the docker container is running, navigate to http://localhost:8080/ and login with Pikachu as username and 15 as level and you will be redirected to the dashboard. 
            2. On the dashboard page there will be a button to add a new Pokemon which will redirect to addPokemon page where you will be asked to enter a new pokemon name, its level, select its type and select the attacks. Once create pokemon button is clicked, it will connect to database and insert a new record in the database with the information provided. 
            3. Once a new pokemon is created, you will be redirected to a page where the newly added pokemon and its details will be shown. These details are retrived from the database by using the cursor.lastrowid to retrive the id of the pokemon just created.
        6. To run the Maintain Types service:
            1. Once the docker container is running, navigate to http://localhost:8080/ and login with Pikachu as username and 15 as level and you will be redirected to the dashboard. 
            2. On the dashboard page there will be a button to add a new type which will redirect to addType page where you will be asked to enter the name of the type and a description of the type. Once Add Type button is clicked, it will connect to the database and insert a new record in the type table in the database.
        7. To run the Maintain Attacks service:
            1. Once the docker container is running, navigate to http://localhost:8080/ and login with Pikachu as username and 15 as level and you will be redirected to the dashboard. 
            2. On the dashboard page there will be a button to add new special attack which will redirect you to to the addAttack page where you will be asked to enter the attack name and the power of the attack. Once Add Attack button is clicked, it will connect to the database and insert a new record in the specialattacks table in the database.
        8. To run the about service:
            1.  Once the docker container is running, navigate to http://localhost:8080/ you should see a button called About Pokemon Shop, the button redirects to the about page where you will see information about the pokemon shop.
        9. To run the PostFix Email service: 
            1. When you add a new pokemon to the database from the maintain pokemon service, it will send an email to the PostFix server.
            2. You should see " Failed to send email: {'ash@trainer.com': (554, b'5.7.1 <ash@trainer.com>: Recipient address rejected: Access denied')}" in the terminal.
        10. To run the Mail Hog Email capture service: 
            1. When the a new pokemon is added and an email is sent via postfix, mail hog is used to capture that. 
            2. To see the captured email, navigate to http://localhost:8025/ and once a new pokemon is created, you should see an email sent from noreply@pokemon.com in mailhog.
