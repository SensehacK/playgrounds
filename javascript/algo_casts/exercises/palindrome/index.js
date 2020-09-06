// --- Directions
// Given a string, return true if the string is a palindrome
// or false if it is not.  Palindromes are strings that
// form the same word if it is reversed. *Do* include spaces
// and punctuation in determining if the string is a palindrome.
// --- Examples:
//   palindrome("abba") === true
//   palindrome("abcdefg") === false

function palindrome(str) {
	var string2 = String();

	for (let a = str.length - 1; a >= 0; a--) {
		string2 += str[a];
	}

	return string2 == str;
}

module.exports = palindrome;
