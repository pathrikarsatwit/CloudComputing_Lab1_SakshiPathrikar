from collections import defaultdict

from fastapi import FastAPI


app = FastAPI()

avenger_names = defaultdict(str)
quote = defaultdict(str)
quote["Thor"] = "Whosoever holds this hammer, if he be worthy, shall possess the power of Thor."
quote["Iron Man"] = "And I... am Iron Man."
quote["Captain America"] = "I can do this all day."
quote["Spider-Man"] = "That thing does not obey the laws of physics at all"
quote["Black Panther"] = "Wakanda forever!"
quote["Hulk"] = "Puny God!"
quote["Ultron"] = "Do you see the beauty of it? The inevitability? You rise, only to fall."
quote["Thanos"] = "Reality is often disappointing."
quote["Red Skull"] = "It is my curse to know all who journey here."
quote["Hela"] = "You're in my seat."
quote["Loki"] = "We have a hulk"
#1. Root Route
@app.get("/")
async def read_root():
    return  "Hello, Welcome to Marvel!"

#2. Simple Route
@app.get("/avengers")
async def avengers():
    return ["Iron Man", "Captain America", "Spider-Man", "Black Panther", "Hulk", "Thor"]

#3. Simple Route
@app.get("/villan")
async def villan():
    return ["Ultron", "Thanos", "Red Skull", "Hella", "Doctor Octopus", "Green Goblin"]

#4. Query String
@app.get("/avengername")
async def avengername (name: str):
    avenger_names["name"] = name
    return f"Your favorite avenger is {name}!"

#5. Query String
@app.get("/moviename")
async def favoritemovie (movie: str):
    avenger_names["movie"] = movie
    return f"Your favorite movie is {movie}!"

#6. Query String
@app.get("/villans")
async def villans(villans: str):
    avenger_names["villans"] = villans
    return f"Your favorite villan is {villans}!"

#7. Path Route
@app.get("/gadget/{gadgetName}/{avenger}")
async def gadget(gadgetName: str, avenger: str):
    avenger_names["gadget"] = gadgetName
    avenger_names["avenger"] = avenger
    return f"Your favorite gadget is {gadgetName} which belongs to {avenger}!"

#8. Path Route
@app.get("/quotes/{avenger}")
async def quotes(avenger: str ):
    avenger_names["quote"] = avenger
    return f"Quote from {avenger} is {quote[avenger]}!"

#9. Path Route
@app.get("/quotesvillan/{villansquotes}")
async def quotes(villansquotes: str):
    avenger_names["quotevillan"] = villansquotes
    return f"Quote from {villansquotes} is {quote[villansquotes]}!"

#10. Simple route
@app.get("/yourAvenger")
async def youravenger():
    return {

        "name": avenger_names["name"],
        "movie": avenger_names["movie"],
        "villans": avenger_names["villans"],
        "gadget": avenger_names["gadget"],
        "quote": quote.get(avenger_names["quote"], "No quote saved"),
        "quotevillan": quote.get(avenger_names["quotevillan"], "No quote saved")
    }
