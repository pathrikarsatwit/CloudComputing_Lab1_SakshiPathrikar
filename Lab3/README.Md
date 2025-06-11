# CloudComputing_Lab3_SakshiPathrikar


1. Introduction To your project
   1. I have built a Node.js and Express-based web application inspired by Camp Half-Blood from the Percy Jackson. 

2. Description of your project
   1. Users can view a list of demigods, a list of cabins at camp half blood, a list of weapons and a random prophecy.
   2. Users can enter their favorite demigod, his/her age, the weapon they use, their godly parent and the cabin they are in.

3. Design of your project
   1. Project Structure:
      1. index.js: The main file containing all route definitions. 
      2. prophecyList: A list containing random prophecies shown to users.
      3. weaponsList: An object mapping demigods to their respective weapons.
   2. Endpoints: 
      1. /: Returns a welcome message for Camp Half-Blood
      2. /cabins: Displays list of cabins (e.g., Zeus, Poseidon, Hades)
      3. /demigods: Lists famous demigods like Percy, Annabeth, and more
      4. /prophecy: Returns a random prophecy from the list
      5. /weapons: Lists various weapons available in the camp
      6. /demigod?name=Percy: Displays the name of the user/demigod via query parameter
      7. /age?age=15: Displays the user's age
      8. /weapon/demigod?name=Percy: Returns the weapon of a specified demigod
      9. /parent?parent=Poseidon: Returns the godly parent of the demigod
      10. /cabin?cabin=3: Returns the cabin number assigned to a demigod
      11. /verify-demigod: Uses HTTP header demigod to verify identity (e.g., if Percy)
      12. /welcome: Accepts a POST request with name and cabin in JSON body and returns a custom welcome
   
4. Detailed instructions on how to run your project
   1. To View the Project in Browser: cd into Lab3 folder then type node main.js (no other web server required as the server is inbuilt in node js) then in the browser type http://localhost:8080/{route_name}
      1. / : To view a welcome message from Camp Half-Blood
      2. /cabins : To view the list of cabins 
      3. /demigods : To view the list of demigods
      4. /prophecy : To view a random prophecy from the prophecy list
      5. /weapons : To view the list of weapons
      6. /demigod?name=Percy : To set and view the demigod's name as Percy
      7. /age?age=16 : To set and view the demigod's age
      8. /weapon/demigod?name=Annabeth : To view the weapon of the demigod Annabeth
      9. /parent?parent=Athena : To set and view the godly parent as Athena
      10. /cabin?cabin=6 : To set and view the assigned cabin number
      11. /verify-demigod : this is a header which will need a curl command from the terminal. Open another terminal as you cannot run commands when a server is running and a server needs to be running before running: curl -H "demigod: Percy" http://localhost:8080/verify-demigod
      12. /welcome : this is a body input which will need a curl command from the terminal. Open another terminal (if not already open) and type: curl -X POST http://localhost:8080/welcome -H "Content-Type: application/json" -d "{\"name\":\"Annabeth\",\"cabin\":\"6\"}"