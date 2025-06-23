CloudComputing_Lab3_SakshiPathrikar
1. Introduction To your project
    1. This lab demonstrates how to containerize the FastAPI application using Docker.

2. Description of your project
    1. This FastAPI app features:
        1. A welcome message at the root.
        2. Lists of popular Avengers and villains.
        3. Routes to retrieve and store favorite characters, quotes, movies, and gadgets using query and path parameters.
        4. A final route to summarize choices.


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
    1. To build an image in docker enter in terminal of your editor: docker build -t marvel .
    2. To build the container enter in terminal of your editor: docker run -it --name marverlcontainer marvel
    3. To map the port in docker terminal enter: docker run -p 8080:8080 marvelcontainer
