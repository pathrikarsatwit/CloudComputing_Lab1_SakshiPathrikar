const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql2/promise');
const session = require('express-session');

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));

app.use(session({
  secret: 'pikachu-rules',
  resave: false,
  saveUninitialized: false
}));

const db = mysql.createPool({
  host:"db",
  user: 'root',
  password: 'Sakshi@1234',
  database: 'pokemon_shop'
});

app.get('/', (req, res) => {
  if (req.session.pokemon) {
    return res.send(`Welcome ${req.session.pokemon.pokemon_name}! <a href="/logout">Logout</a>`);
  }

  res.send(`
    <form method="POST">
      <h2>Pokémon Login</h2>
      <input name="name" placeholder="Pokémon Name" required /><br/>
      <input name="level" type="number" placeholder="Level" required /><br/>
      <button type="submit">Login</button>
    </form>
  `);
});

app.post('/', async (req, res) => {
  const { name, level } = req.body;
  const [rows] = await db.query(
    'SELECT * FROM Pokemon WHERE pokemon_name = ? AND pokemon_level = ?',
    [name, level]
  );

  if (rows.length > 0) {
    req.session.pokemon = rows[0];
    return res.redirect('/');
  }

  res.send('Invalid Pokémon name or level. <a href="/">Try again</a>');
});

// Logout
app.get('/logout', (req, res) => {
  req.session.destroy(() => res.redirect('/'));
});

app.listen(3000, () => console.log('Pokémon login running at http://localhost:3000'));