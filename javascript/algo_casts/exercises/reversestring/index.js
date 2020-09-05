// --- Directions
// Given a string, return a new string with the reversed
// order of characters
// --- Examples
//   reverse('apple') === 'leppa'
//   reverse('hello') === 'olleh'
//   reverse('Greetings!') === '!sgniteerG'

function reverse(str) {
	var str2 = new String();
	//var str2; // this leads to having undefined variable as it is not initialized with new String()
	console.log("printing length" + str.length);

	for (var a = str.length - 1; a >= 0; a--) {
		console.log("Value of a is " + a);

		console.log(str[a]);
		str2 += str[a];
	}

	return str2;
}

module.exports = reverse;
