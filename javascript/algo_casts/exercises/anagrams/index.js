// --- Directions
// Check to see if two provided strings are anagrams of eachother.
// One string is an anagram of another if it uses the same characters
// in the same quantity. Only consider characters, not spaces
// or punctuation.  Consider capital letters to be the same as lower case
// --- Examples
//   anagrams('rail safety', 'fairy tales') --> True
//   anagrams('RAIL! SAFETY!', 'fairy tales') --> True
//   anagrams('Hi there', 'Bye there') --> False

function anagrams(stringA, stringB) {
	const cleanedStrA = stringA.replace(/[^\w]/g, "");
	const cleanedStrB = stringB.replace(/[^\w]/g, "");
	const charsA = {};
	const charsB = {};
	var isAnagram = true;

	// Character mapping

	for (let char of cleanedStrA) {
		if (charsA[char]) {
			charsA[char] += 1;
		} else {
			charsA[char] = 1;
		}
	}

	for (let char of cleanedStrB) {
		if (charsB[char]) {
			charsB[char] += 1;
		} else {
			charsB[char] = 1;
		}
	}

	// debug checks
	console.log(Object.keys(charsA).length);
	console.log(Object.keys(charsB).length);
	charsB.hasOwnProperty("f");

	// iterating & comparing key values with each other.
	// switching out boolean value !true false
	if (Object.keys(charsA).length == Object.keys(charsB).length) {
		for (const key in charsA) {
			if (charsB.hasOwnProperty(key) && charsA.hasOwnProperty(key)) {
				isAnagram = charsA[key] === charsB[key] ? true : false;
			} else {
				isAnagram = false;
			}
		}
	} else {
		isAnagram = false;
	}
	return isAnagram;
}

anagrams("rail safety", "fairy tales");

module.exports = anagrams;
