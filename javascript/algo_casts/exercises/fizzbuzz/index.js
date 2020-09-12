// --- Directions
// Write a program that console logs the numbers
// from 1 to n. But for multiples of three print
// “fizz” instead of the number and for the multiples
// of five print “buzz”. For numbers which are multiples
// of both three and five print “fizzbuzz”.
// --- Example
//   fizzBuzz(5);
//   1
//   2
//   fizz
//   4
//   buzz

function fizzBuzz(n) {
	/*
	while (n > 0) {
		if ((n % 3) + (n % 5) == 0) {
			console.log("fizzbuzz");
		} else if (n % 5 == 0) {
			console.log("buzz");
		} else if (n % 3 == 0) {
			console.log("fizz");
		} else {
			console.log(n);
		}
		n--;
	}
	*/

	/*
	var index = 1;
	while (index <= n) {
		if ((index % 3) + (index % 5) == 0) {
			console.log("fizzbuzz");
		} else if (index % 5 == 0) {
			console.log("buzz");
		} else if (index % 3 == 0) {
			console.log("fizz");
		} else {
			console.log(index);
		}
		index++;
	}
	*/
	
	for (let index = 1; index <= n; index++) {
		if ((index % 3) + (index % 5) == 0) {
			console.log("fizzbuzz");
		} else if (index % 5 == 0) {
			console.log("buzz");
		} else if (index % 3 == 0) {
			console.log("fizz");
		} else {
			console.log(index);
		}
	}
}

module.exports = fizzBuzz;

/*
fizzBuzz(5);
console.log("Hello Sensehack!");
fizzBuzz(16);
*/
