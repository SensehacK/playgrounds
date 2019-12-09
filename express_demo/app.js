const express = require('express')
const app = express()
const morgan = require('morgan')
const mysql = require('mysql')


app.use(morgan('short'))



app.get('/', (req, res) => {
    console.log('Hi reached main server');
    res.send('Hello Sensehack!');
});


app.get('/users', (req, res) => {
    var user1 = { firstName: 'Kautilya', lastName: 'Save' }

    const user2 = { firstName: 'Lebron', lastName: 'James' }

    res.json([user1, user2])

})

app.get('/user/:id', (req, res) => {
    console.log('Fetching user ID', req.params.id);
    // res.send('Getting the user ID')

    const connection = mysql.createConnection({
        host: 'localhost',
        user: 'root',
        database: 'test'
    })
    const queryString = 'SELECT * FROM test_two'
    connection.query(queryString, (err, rows, fields) => {
        console.log('Printing error ', err);

        console.log('Hi fetching users successfully', rows);
        res.json(rows)
    })

    // res.end()
})


app.listen(3000, () => {
    console.log('Server is up and listening on 3003...');
})

