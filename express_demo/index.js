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
        return res.status(404).send('The course wasn\'t found');
    }
    else {
        res.send(course);
    }

    // res.send(req.params.id);
});

app.post('/api/courses', (req, res) => {

    const { error } = validateCourse(req.body);
    if (error) {
        console.log(error);
        return res.status(400).send(error.details[0].message);
    }

    const course = {
        id: courses.length + 1,
        name: req.body.name
    };
    courses.push(course);
    res.send(course);
});

// Updating HTTP Put method for alteration of object data
app.put('/api/courses/:id', (req, res) => {

    // check course present in the array
    let course = (courses.find(c => c.id === parseInt(req.params.id)));

    if (!course) return res.status(404).send('The course wasn\'t found');

    // Validation input part
    const { error } = validateCourse(req.body);
    if (error) {
        return res.status(400).send(error.details[0].message);
    }

    // update course
    course.name = req.body.name;

    // res.send(course);
    res.send(courses);


});


function validateCourse(course) {

    // Using JOI validate Course func for request input validation
    const schema = {
        name: Joi.string().min(3).required()
    };
    return Joi.validate(course, schema);

}

/*
// Double parameters
app.get('/api/courses/:year/:course', (req, res) => {
    res.send(req.params);
});
*/



app.delete('/api/courses/:id', (req, res) => {
    // Look up the course
    // check course present in the array
    let course = (courses.find(c => c.id === parseInt(req.params.id)));

    if (!course) {
        // 404 
        return res.status(404).send('The course ID wasn\'t found');
    }

    // Delete 
    const index = courses.indexOf(course);
    console.log('Index for deletion', index);

    console.log("Before deletion", courses);

    courses.splice(index, 1);

    console.log("After splice deletion", courses);

    console.log('Deleted course', course);




    // Return the same course
    res.send(course);
    // Second response send doesn't work as it has already ran before.
    res.send(courses);
    // res.send("Full List of courses", courses);

});

app.get('/api/courses/:year/:month', (req, res) => {
    res.send(req.query);
});



// Port
const port = process.env.PORT || 3000;
// Set PORT number via terminal 'export PORT=5000'

app.listen(port, () => console.log(`Listening on port ${port}`));
