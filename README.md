# CloudComputing_Lab1_SakshiPathrikar

1. Introduction To your project
   1. I have built a FastAPI-based web application which allows the users to select their favorite Avenger!

2. Description of your project
   1. Users can enter their favorite avenger, the favorite movie of the avenger, gadget, quote and the villian. 
   2. This app stores the information and displays it back at the end.

3. Design of your project
   1. Project Structure:
      1. main.py: The main file containing all route definitions. 
      2. avenger_names: A dictionary that stores user preferences. 
      3. quote: A dictionary with quotes for Avengers and villains.
   2. Endpoints: 
      1. / : Welcome Message
      2. /avengers : Displays a list of Avengers
      3. /villan : Displays a list of Villans
      4. /avengername?name : Sets the Avengers Name
      5. /moviename?movie : Sets movie's name
      6. /villans?villans : Sets Villans name
      7. /gadget/{gadgetName}/{avenger} : Sets the gadget and the Avenger
      8. /quotes/{avenger} : Returns the quote of the Avenger from the quote dictionary
      9. /quotesvillan/{villansquotes} : Returns the quote of the Villian from the quote dictionary
      10. /yourAvenger : Returns all the saved prefrenced in JSON Format

   
4. Detailed instructions on how to run your project
   1. / : To view a welcome message
   2. /avengers: To view the avengers list
   3. /villan : To view the villians list 
   4. /avengername?name=Thor (here the avenger is Thor) : To set the Avenger as Thor
   5. /moviename?movie=Thor: Ragnarok :To set the movie as Thor: Ragnarok
   6. /villans?villans=Hela : To set the villian as Hela
   7. /gadget/Mjolnir/Thor : To set the gadget as Mjolnir and Avenger as Thor
   8. /quotes/Thor: To view Thor's quote
   9. /quotes/Hela: To view Hela's quote
   10. /yourAvenger: To view all the prefrences of the user
