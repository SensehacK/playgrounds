const express = require('express')
const app = express()
const morgan = require('morgan')
const mysql = require('mysql')


app.use(morgan('short'))



app.get('/', (req, res) => {
    console.log('Hi reached main server');
    res.send('Hello Sensehack!');
});


app.get('/custom_user', (req, res) => {
    var user1 = { firstName: 'Kautilya', lastName: 'Save' }

    const user2 = { firstName: 'Lebron', lastName: 'James' }

    res.json([user1, user2])

})

app.get('/user/:id', (req, res) => {
    const id = req.params.id;
    console.log('Fetching user ID', id);
    // res.send('Getting the user ID')

    const connection = mysql.createConnection({
        host: 'localhost',
        user: 'root',
        password: 'kautilya',
        database: 'node_js'
    })
    const queryString = 'SELECT * FROM users WHERE id = ?'
    connection.query(queryString, [id], (err, rows, fields) => {

        if (err) {
            console.log('Error in the executing query', err);
            res.send('Something unexpected happened');
            // res.end()
        }
        if (rows.length === 0) {
            console.log('Empty row query');
            res.send('Query resulted no results, Please try with different input!')
            res.end()
        } else {
            console.log('Hi fetching users successfully', rows);
            res.json(rows)
        }

    })

    // res.end()
})

// Getting all the users
app.get('/users', (req, res) => {
    const connection = mysql.createConnection({
        host: 'localhost',
        user: 'root',
        password: 'kautilya',
        database: 'node_js'
    })

    const queryString = 'SELECT * FROM users2'
    connection.query(queryString, (err, rows, field) => {
        if (err) {

            console.log('Error in the executing query', err);
            res.send('Something unexpected happened');
            // res.end()
        }
        res.json(rows);
    })
})


app.listen(3001, () => {
    console.log('Server is up and listening on 3003...');
})

