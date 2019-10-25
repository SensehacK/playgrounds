
const EventEmitter = require('events')
const emitter = new EventEmitter();


var log = require('./logger');
// Running the exported module for logger.

log.log("Kautilya");


// Trying Emitter and events

// Listening an event
emitter.on('Kautilya', function () {
    console.log('Event Listened');
})

// Raising an event
emitter.emit('Kautilya');

