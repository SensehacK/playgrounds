// --- Directions
// Given a string, return the character that is most
// commonly used in the string.
// --- Examples
// maxChar("abcccccccd") === "c"
// maxChar("apple 1231111") === "1"

function maxChar(str) {
	const chars = {};

	// Character mapping
	for (let char of str) {
		if (chars[char]) {
			chars[char] += 1;
		} else {
			chars[char] = 1;
		}
	}
	console.log("Printing the whole chars");
	console.log(chars);

	// for (let val of chars) {
	// 	console.log("Values : " + val);
	// }

	var highestRep = 0;
	var highestIndex = 0;

	for (const val in chars) {
		if (chars.hasOwnProperty(val)) {
			const element = chars[val];
			highestRep = element > highestRep ? element : highestRep;

			highestIndex = element >= highestRep ? val : highestIndex;

			console.log("element values : " + element);
			console.log("element highest : " + val);
		}
	}

	console.log("element highestRep : " + highestRep);
	console.log("element highestIndex : " + highestIndex);

	console.log("value is : " + highestIndex);
	// console.log("contains" + chars.present(5));
	return highestIndex;
}

maxChar("21124242421");

maxChar("agnajngw3rnawkng");

module.exports = maxChar;
