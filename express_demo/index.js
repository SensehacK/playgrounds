const express = require('express');
const app = express();

// enable parsing object
app.use(express.json());

const courses = [
    { id: 1, name: 'MobileWeb' },
    { id: 2, name: 'InternetComp' },
    { id: 3, name: 'Algorithm' },
]


app.get('/', (req, res) => {
    console.log('Hi reached main server');

    res.send('Hello Sensehack!');
});


app.get('/api/courses', (req, res) => {
    res.send(courses);
});

app.get('/api/courses/:id', (req, res) => {

    let course = (courses.find(c => c.id === parseInt(req.params.id)));

    if (!course) {
        // 404 
        res.status(404).send('The course wasn\'t found');
    }
    else {
        res.send(course);
    }

    // res.send(req.params.id);
});

app.post('/api/courses', (req, res) => {
    const course = {
        id: courses.length + 1,
        name: req.body.name
    };
    courses.push(course);
    res.send(course);
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
