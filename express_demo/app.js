// Global variables
const express = require('express')
const app = express()
const morgan = require('morgan')
const mysql = require('mysql')
const bodyParser = require('body-parser')


// App use binding
app.use(express.static('./public'))
app.use(bodyParser.urlencoded({ extended: false }))
app.use(morgan('short'))


// Root access
app.get('/', (req, res) => {
    console.log('Hi reached main server');
    res.send('Hello Sensehack!');
});

// Router 
const router = require('./routes/user.js')
app.use(router)

// Wake up init
app.listen(3003, () => {
    console.log('Server is up and listening on 3003...');
})



