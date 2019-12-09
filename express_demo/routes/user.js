// User routes file.
const express = require('express')
const mysql = require('mysql')

const router = express.Router()


router.get('/messages', (req, res) => {
    console.log('Show some messages2222');
    res.end()

})


router.get('/custom_user', (req, res) => {
    var user1 = { firstName: 'Kautilya', lastName: 'Save' }

    const user2 = { firstName: 'Lebron', lastName: 'James' }

    res.json([user1, user2])

})

router.get('/user/:id', (req, res) => {
    const id = req.params.id;
    console.log('Fetching user ID', id);
    // res.send('Getting the user ID')

    const connection = getConnection();

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
            const users = rows.map((row) => {
                return {
                    firstName: row.first_name,
                    lastName: row.last_name
                }
            })
            res.json(users)
        }

    })

    // res.end()
})

// Getting all the users
router.get('/users', (req, res) => {
    const connection = getConnection()

    const queryString = 'SELECT * FROM users'
    connection.query(queryString, (err, rows, field) => {

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
            const users = rows.map((row) => {
                return {
                    firstName: row.first_name,
                    lastName: row.last_name
                }
            })
            res.json(users)
        }
    })
})

router.post('/user_create', (req, res) => {
    console.log('In user Create service API endpoint');
    console.log('Logging the req of post data');

    const first_name = req.body.first_name
    const last_name = req.body.last_name


    const queryString = 'INSERT INTO  users (first_name, last_name) VALUES (? , ?)'

    getConnection().query(queryString, [first_name, last_name], (err, results, field) => {

        if (err) {
            console.log('Error in the executing query', err);
            res.sendStatus(500);
            return;
        }
        console.log('Inserted data to Database', first_name, last_name)

        // We can't use "res object while in the body of executing the query"
        // res.send('Inserted data to Database', first_name, last_name);
        res.end()
    })


    res.end()

})

const pool = mysql.createPool({
    host: 'localhost',
    user: 'root',
    password: 'kautilya',
    database: 'node_js'
})

function getConnection() {
    return pool
}


module.exports = router