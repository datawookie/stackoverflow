import express, { Request, Response } from 'express'
import mysql from 'mysql'

const pool = mysql.createPool({
    connectionLimit : 10,
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_NAME,
    port: Number(process.env.DB_PORT)
});

const app = express()
const PORT = 3000;

app.listen(PORT, () => {
    console.log("user:     "+process.env.DB_USER);
    console.log("password: "+process.env.DB_PASSWORD);

    pool.query('SELECT 1', (err, results) => {
        if (err) {
            return console.error('Error connecting to the database:', err);
        }
        console.log('Database connection successfully created.');
    });
})
