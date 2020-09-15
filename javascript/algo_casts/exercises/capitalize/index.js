// --- Directions
// Write a function that accepts a string.  The function should
// capitalize the first letter of each word in the string then
// return the capitalized string.
// --- Examples
//   capitalize('a short sentence') --> 'A Short Sentence'
//   capitalize('a lazy fox') --> 'A Lazy Fox'
//   capitalize('look, it is working!') --> 'Look, It Is Working!'

//console.log(capitalize("Kautilya is a dumbass! baka"));

module.exports = capitalize;

// /*
function capitalize(str) {
	var capitalizeSentence = "";
	for (const word of str.split(" ")) {
		capitalizeSentence = capitalizeSentence + uppercase(word);
	}
	return capitalizeSentence.slice(0, -1); // removes the extra space added due to suffix space added every time.
	// We could check whether it's the last element of the array but that would introduce nth amount of if condition checking.
}

function uppercase(str) {
	const modifiedStr = str[0].toUpperCase() + str.slice(1);
	return modifiedStr + " ";
}
// */

/* efficient
function capitalize(str) {
	const words = [];
	for (const word of str.split(" ")) {
		words.push(word[0].toUpperCase() + word.slice(1));
	}
	return words.join(" ");
}
*/
