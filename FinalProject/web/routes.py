from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import mysql.connector
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def connect_to_db():
    return mysql.connector.connect(
        host="db",
        user="root",
        password="Sakshi@1234",
        database="pokemon_shop"
    )

# HTML Routes

@app.get("/")
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
def login(request: Request, name: str = Form(...), level: int = Form(...)):
    db = connect_to_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pokemon WHERE pokemon_name = %s AND pokemon_level = %s", (name, level))
    user = cursor.fetchone()
    cursor.close()
    db.close()

    if user:
        return RedirectResponse(url="/dashboard", status_code=303)
    return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid credentials"})

@app.get("/dashboard")
def dashboard(request: Request):
    db = connect_to_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM pokemon")
    pokemons = cursor.fetchall()

    cursor.execute("SELECT * FROM type")
    types = cursor.fetchall()

    cursor.execute("SELECT * FROM specialattacks")
    attacks = cursor.fetchall()

    cursor.close()
    db.close()

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "pokemons": pokemons,
        "types": types,
        "attacks": attacks
    })



@app.get("/add")
def add_page(request: Request):
    db = connect_to_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM type")
    types = cursor.fetchall()
    cursor.execute("SELECT * FROM specialattacks")
    attacks = cursor.fetchall()
    cursor.close()
    db.close()
    return templates.TemplateResponse("addPokemon.html", {"request": request, "types": types, "attacks": attacks})

@app.post("/addPokemon")
def add_pokemon(
    request: Request,
    pokemmon_name: str = Form(...),
    pokemon_level: int = Form(...),
    type_id: int = Form(...),
    attack_id: int = Form(...)
):
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO pokemon (pokemon_name, pokemon_level) VALUES (%s, %s)", (pokemmon_name, pokemon_level))
    db.commit()
    pokemon_id = cursor.lastrowid

    cursor.execute("INSERT INTO pokemontype (pokemon_id, type_id) VALUES (%s, %s)", (pokemon_id, type_id))
    db.commit()
    cursor.execute("INSERT INTO pokemonspecialattacks (pokemon_id, attack_id) VALUES (%s, %s)", (pokemon_id, attack_id))
    db.commit()
    cursor.close()
    db.close()

    # Send email
    send_email_notification(pokemmon_name, pokemon_level)

    return RedirectResponse(url=f"/addedPokemon/{pokemon_id}", status_code=303)

def send_email_notification(name, level):
    sender = "noreply@pokemon.com"
    recipient = "ash@trainer.com"  # This will be caught by MailHog
    subject = "New Pokémon Added"
    body = f"A new Pokémon has been added:\n\nName: {name}\nLevel: {level}"

    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("postfix2", 587) as server:  # Connect to Postfix container
            server.sendmail(sender, recipient, msg.as_string())
    except Exception as e:
        print("Failed to send email:", e)


@app.get("/addedPokemon/{pokemon_id}")
def added_pokemon(request: Request, pokemon_id: int):
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("""
        SELECT 
            p.pokemon_name, p.pokemon_level, 
            sa.attack_name, sa.attack_power, 
            t.type_name, t.description
        FROM pokemon p
        JOIN pokemontype pt ON p.pokemon_id = pt.pokemon_id
        JOIN type t ON pt.type_id = t.type_id
        JOIN pokemonspecialattacks ps ON p.pokemon_id = ps.pokemon_id
        JOIN specialattacks sa ON ps.attack_id = sa.attack_id
        WHERE p.pokemon_id = %s
    """, (pokemon_id,))
    data = cursor.fetchone()
    cursor.close()
    db.close()
    return templates.TemplateResponse("addedPokemon.html", {"request": request, "pokemon": data})
@app.get("/about")
def about_page(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

# Route to display form to add a new type
@app.get("/addType")
def add_type_page(request: Request):
    return templates.TemplateResponse("addType.html", {"request": request})

# Route to handle form submission for new type
@app.post("/addType")
def add_type(request: Request, type_name: str = Form(...), description: str = Form(...)):
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO type (type_name, description) VALUES (%s, %s)", (type_name, description))
    db.commit()
    cursor.close()
    db.close()
    return RedirectResponse(url="/dashboard", status_code=303)

# Route to display form to add a new special attack
@app.get("/addAttack")
def add_attack_page(request: Request):
    return templates.TemplateResponse("addAttack.html", {"request": request})

# Route to handle form submission for new special attack
@app.post("/addAttack")
def add_attack(request: Request, attack_name: str = Form(...), attack_power: int = Form(...)):
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO specialattacks (attack_name, attack_power) VALUES (%s, %s)", (attack_name, attack_power))
    db.commit()
    cursor.close()
    db.close()
    return RedirectResponse(url="/dashboard", status_code=303)