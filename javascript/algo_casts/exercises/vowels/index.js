// --- Directions
// Write a function that returns the number of vowels
// used in a string.  Vowels are the characters 'a', 'e'
// 'i', 'o', and 'u'.
// --- Examples
//   vowels('Hi There!') --> 3
//   vowels('Why do you ask?') --> 4
//   vowels('Why?') --> 0

function vowels(str) {
	let vowelsArr = ["a", "e", "i", "o", "u"];
	vowelCount = 0;
	for (const char of str.toLowerCase()) {
		if (vowelsArr.includes(char)) {
			vowelCount++;
		}
	}
	return vowelCount;
}

module.exports = vowels;
