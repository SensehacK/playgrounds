const express = require('express');
const app = express();


app.get('/', (req, res) => {
    console.log('Hi reached main server');

    res.send('Hello Sensehack!');
});


app.get('/api/courses', (req, res) => {
    res.send([1, 4, 6]);
});

app.get('/api/courses/:id', (req, res) => {
    res.send(req.params.id);
});

/*
// Double parameters
app.get('/api/courses/:year/:course', (req, res) => {
    res.send(req.params);
});
*/

app.get('/api/courses/:year/:month', (req, res) => {
    res.send(req.query);
});



// Port
const port = process.env.PORT || 3000;
// Set PORT number via terminal 'export PORT=5000'

app.listen(port, () => console.log(`Listening on port ${port}`));
