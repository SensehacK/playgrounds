// --- Directions
// Print out the n-th entry in the fibonacci series.
// The fibonacci series is an ordering of numbers where
// each number is the sum of the preceeding two.
// For example, the sequence
//  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
// forms the first ten entries of the fibonacci series.
// Example:
//   fib(4) === 3

function fib(n) {
	num1 = 0;
	num2 = 1;
	for (let index = 1; index < n; index++) {
		// if (n < 2) {
		// 	return num2;
		// } else {
		// 	var temp = num1;
		// 	num1 = num2;
		// 	num2 = temp + num2;
		// }

		var temp = num1;
		num1 = num2;
		num2 = temp + num2;
	}

	return num2;
}

module.exports = fib;
