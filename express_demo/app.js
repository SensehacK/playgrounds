const express = require('express')
const app = express()
const morgan = require('morgan')
const mysql = require('mysql')
const bodyParser = require('body-parser')



app.use(express.static('./public'))
app.use(bodyParser.urlencoded({ extended: false }))
app.use(morgan('short'))



app.get('/', (req, res) => {
    console.log('Hi reached main server');
    res.send('Hello Sensehack!');
});

const router = express.Router()
router.get('/messages', (req, res) => {
    console.log('Show some messages');
    res.end()

})

app.use(router)


app.get('/custom_user', (req, res) => {
    var user1 = { firstName: 'Kautilya', lastName: 'Save' }

    const user2 = { firstName: 'Lebron', lastName: 'James' }

    res.json([user1, user2])

})

app.get('/user/:id', (req, res) => {
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
app.get('/users', (req, res) => {
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

app.post('/user_create', (req, res) => {
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


app.listen(3003, () => {
    console.log('Server is up and listening on 3003...');
})

function getConnection() {
    return mysql.createConnection({
        host: 'localhost',
        user: 'root',
        password: 'kautilya',
        database: 'node_js'
    });
}

