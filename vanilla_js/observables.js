var button = document.querySelector("button");

var observerObj = {
  next: function(value) {
    console.log("in Observable next: function");
    console.log(value);
    console.log(value.timeStamp);
  },
  error: function(error) {
    console.log(error);
  },
  complete: function() {
    console.log("Completed");
  }
};

// Event driven Observable.
// Rx.Observable.fromEvent(button, "click").subscribe(value =>
//   console.log(value.clientX)
// );

// Object passed driven Observable.
// Rx.Observable.fromEvent(button, "click").subscribe(observerObj);
/*
Rx.Observable.create(function(obs) {
  console.log("in Observable Create event");
  obs.next("A Value");
  obs.next("A second value");
  setTimeout(function() {
    obs.complete();
  }, 2000);

  //   obs.complete();
  //   obs.error("Errir");
  obs.next("A Third value");
}).subscribe(observerObj);
*/

/*
// continuos subscribed event

Rx.Observable.create(function(obs) {
  button.onclick = function(event) {
    console.log(event);

    obs.next(event);
  };
}).subscribe(observerObj);

*/

// Destroy Observables to avoid memory leak
var rxObsrv = Rx.Observable.create(function(obs) {
  button.onclick = function(event) {
    console.log(event);

    obs.next(event);
  };
}).subscribe(observerObj);

// after 5 secs it would stop the button onclick event monitoring.
setTimeout(function() {
  console.log("calling Memory leak management via unsubscribe method");
  rxObsrv.unsubscribe();
}, 5000);
