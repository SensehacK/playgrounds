// IMPORT LIBRARY PACKAGES NEEDED BY YOUR PROGRAM
// SOME FUNCTIONALITY WITHIN A PACKAGE MAY BE RESTRICTED
// DEFINE ANY FUNCTION NEEDED
// FUNCTION SIGNATURE BEGINS, THIS FUNCTION IS REQUIRED
function cellCompete(states, days) {
	// WRITE YOUR CODE HERE

	console.log("States Hello : ", states);

	console.log(states.length);
	var newStateArr = [];
	var currentArr = states;
	// This thing I believe it just passes the reference so those dirty commits
	// are changing both parameters currentArr and newStateArr
	for (let index = 0; index < days; index++) {
		console.log("In Loop States Hello : ", currentArr);
		for (var i = 0; i < currentArr.length; i++) {
			console.log("Current Cell @@@@ i: " + i);
			console.log("State currentArr $$$$$$ : ", currentArr);
			console.log("State newStateArr $$$$$$ : ", newStateArr);
			let firstCell = currentArr[i - 1];
			let secondCell = currentArr[i + 1];
			console.log("current Cell: " + currentArr[i]);
			console.log("First Cell: " + firstCell);
			console.log("second Cell: " + secondCell);

			newStateArr[i] = determineCell(firstCell, secondCell);
			/*
			if (i < 1) {
				console.log("Completed first condition");
				newStateArr[i] = determineCell(firstCell, secondCell);
			} else if (i == currentArr.length - 1) {
				console.log("Completed end condition");
				newStateArr[i] = determineCell(firstCell, secondCell);
			} else {
				console.log("Completed other condition");
				newStateArr[i] = determineCell(firstCell, secondCell);
			}
			*/
			console.log("New Array created variable: " + newStateArr[i]);
			console.log("Completed for loop");
		}

		console.log("Completed for loop iteration:  " + index);
		console.log("New Array created variable: " + newStateArr);
		console.log("Completed for loop");
		currentArr = [];
		currentArr = newStateArr;
		// I needed to empty this array also to start fresh initialization of the array.
		newStateArr = [];
		// Or else it was mutating on the same array and for some reason it was not properly mutating.
		// Maybe thats why we need to empty the array or just
		// initialize by value rather than initialize by reference.
	}

	console.log("Result after one round " + currentArr);
	return currentArr;
}

function determineCell(first = 0, second = 0) {
	console.log("Output Cell: ## " + (first == second ? 0 : 1));
	return first == second ? 0 : 1;
}
// FUNCTION SIGNATURE ENDS

var states = [0, 1, 0, 0, 1, 0, 1, 0];
var states2 = [1, 0, 0, 0, 0, 1, 0, 0];
var states3 = [1, 1, 1, 0, 1, 1, 1, 1];
// cellCompete(states2, 1);
cellCompete(states3, 2);
