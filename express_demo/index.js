const express = require('express');
const Joi = require('joi');
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


    // Using Joi package for request input validation
    const schema = {
        name: Joi.string().min(3).required()
    };

    const result = Joi.validate(req.body, schema);
    console.log(result);
    if (result.error) {
        res.status(400).send(result.error);
        res.status(400).send(result.error.details[0].message);
    }

    if (!req.body.name || req.body.name.length < 3) {
        //400 Bad request
        res.status(400).send('Name is mandatory and should be greater than 3');
        return;
    }



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
