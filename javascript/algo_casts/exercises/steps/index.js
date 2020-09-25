// --- Directions
// Write a function that accepts a positive number N.
// The function should console log a step shape
// with N levels using the # character.  Make sure the
// step has spaces on the right hand side!
// --- Examples
//   steps(2)
//       '# '
//       '##'
//   steps(3)
//       '#  '
//       '## '
//       '###'
//   steps(4)
//       '#   '
//       '##  '
//       '### '
//       '####'

function steps(n) {
	for (let index = 0; index < n; index++) {
		console.log(optimized(index, parseInt(n)));
	}
}

/*
This function logic is partly thanks to the video I was referring, 
& I did had something in mind like this but on my first attempt my solution felt bit more bloated and verbose.
I tend to work on optimizing the code logic on the second play.
Even though I should have just worked on optimized logic at first.
But I do believe that bigger complex problems gets broken down first and solved in simple manner.
The optimization part can come after creating Proof of concept\
*/
function optimized(index, n) {
	var hashStr = "";
	for (let j = 0; j < n; j++) {
		if (j <= index) {
			hashStr = hashStr + "#";
		} else {
			hashStr = hashStr + " ";
		}
	}
	return hashStr;
}

module.exports = steps;

/*
function steps(n) {
	for (let index = 1; index <= n; index++) {
		console.log(hashStr(index, parseInt(n)));
	}
}

function hashStr(index, n) {
	var hashStr = "";
	var emptyStr = "";

	for (let j = 0; j < index; j++) {
		hashStr = hashStr + "#";
	}

	for (let k = 0; k < n - index; k++) {
		emptyStr = emptyStr + " ";
	}
	return hashStr + emptyStr;
}

*/
