// --- Directions
// Given an integer, return an integer that is the reverse
// ordering of numbers.
// --- Examples
//   reverseInt(15) === 51
//   reverseInt(981) === 189
//   reverseInt(500) === 5
//   reverseInt(-15) === -51
//   reverseInt(-90) === -9

function reverseInt(n) {
	console.log("Values of data" + n);
	console.log(n % 10);
	const reverseStr = n.toString().split("").reverse().join("");
	console.log(reverseStr);

	const integer = parseInt(reverseStr);
	console.log("the value of reverse integer" + integer);
	console.log("Math.sign: " + Math.sign(n));
	const tempVar = Math.sign(n) == 1 ? integer : integer - integer * 2;
	console.log("Variable of temporary" + tempVar);

	// console.log(
	// 	"Values of data" + Math.sign(n) ? integer : integer - integer * 2
	// );

	// n.toString();
	return tempVar;
}

// reverseInt(500);

// reverseInt(056);

// reverseInt(325);

// reverseInt(-3265);

module.exports = reverseInt;
