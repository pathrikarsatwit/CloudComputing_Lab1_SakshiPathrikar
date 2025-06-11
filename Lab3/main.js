const express = require('express');
const path = require('path');

const app = express();
app.use(express.json());


//prohpecy list: 
let prophecyList = [["You shall go west, and face the god who has turned, You shall find what was stolen, and see it safely returned, You shall be betrayed by one who calls you a friend, And you shall fail to save what matters most, in the end."],
["You shall sail the iron ship with warriors of bone, You shall find what you seek and make it your own, But despair for your life entombed within stone, And fail without friends, to fly home alone."],
["One shall be lost in the land without rain, One shall be lost in the land without rain, The bane of Olympus shows the trail, Campers and Hunters combined prevail, The Titan's curse must one withstand, And one shall perish by a parent's hand."],
["You shall delve in the darkness of the endless maze, The dead, the traitor, and the lost one raise, You shall rise or fall by the ghost king's hand, The Child of Athena's final stand, Destroy with a hero's final breath, And lose a love to worse than death."]
];

//weapons dict:
weaponsList = {
    Percy: "Riptide",
    Annabeth: "Sword",
    Zeus: "Lightning bolt",
    Posiedon: "Trident",
    Grover: "Reed Pipe",
    Clarisse: "Backbiter"
};
//use http module
const http = require('http');
//http server for routes

//1. HTML Content
app.get('/',(req,res)=>{
    res.status(200);
    res.send("<h1>Welcome to Camp Half-Blood!</h1>");
});

app.get('/cabins',(req,res)=>{
    res.status(200);
    res.send("<h2>List of cabins: Zeus, Hera, Posideon, Ares, Apollo, Hephaestus, Dionysus, Aphrodite, Artemis, Athena, Demeter, Hermes, Hades</h2>");

});

    //3. HTML Content
app.get('/demigods',(req,res)=>{
   res.status(200);
    res.send("<h2>List of demigods: Percy Jackson, Annabeth Chase, Grover Underwood, Thalia Grace, Luke Castellan, Leo Valdez, Frank Zhang, Jason Grace</h2>");
});

    //4. HTML Content
app.get('/prophecy',(req,res)=>{
    let random_integer = Math.floor(Math.random() * prophecyList.length);
    res.status(200);
    res.send(prophecyList[random_integer]);
});

    //5. HTML Content

app.get('/weapons',(req,res)=>{
    res.status(200);
    res.send("List of weapons: Riptide, Sword, Reed Pipe, Lightning Bolt, Trident, Backbiter ");
});

    //6. Query Parameters
app.get('/demigod', (req,res)=>{

    const name = req.query.name;
    res.send({message: `Your name is ${name}`});
});
    
    //7. Query Parameters
app.get('/age',(req,res)=>{

    const age = req.query.age;
    res.send({message: `Age is ${age}`});
});

//8. Query Parameters
app.get('/weapon/demigod',(req,res)=>{
    const name = req.query.name;
    const weapon = weaponsList[name];
    res.send({message: `Weapon of ${name} is ${weapon}`});
});


    //9. Query Parameters
app.get('/parent',(req,res)=>{

    const parent = req.query.parent;
    res.send({message: `Parent is ${parent}`});
});


    //10. Query Paramater
app.get('/cabin',(req,res)=>{

    const cabin = req.query.cabin;
    res.send({message: `Cabin number is ${cabin}`});
});

    //11. header route
app.get('/verify-demigod',(req,res)=>{
    const demigod = req.headers['demigod'];
    if(demigod == 'Percy'){
        res.send("Hi Percy!");
    }else{
        res.send("You are not Percy!");
    }
});


    //12. body inputs
app.post("/welcome", (req, res) => {
    const { name, cabin } = req.body;
    res.send(`Welcome ${name} to cabin ${cabin}`);
});


app.listen(8080,() =>{
    console.log('Server running');
});
