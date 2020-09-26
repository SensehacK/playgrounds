// --- Directions
// Write a function that accepts a positive number N.
// The function should console log a pyramid shape
// with N levels using the # character.  Make sure the
// pyramid has spaces on both the left *and* right hand sides
// --- Examples
//   pyramid(1)
//       '#'
//   pyramid(2)
//       ' # '
//       '###'
//   pyramid(3)
//       '  #  '
//       ' ### '
//       '#####'

function pyramid(n) {
	for (let row = 0; row < n; row++) {
		var pyramidStr = "";

		for (let column = 0; column < n + (n - 1); column++) {
			if (column < n - row - 1 || column > n + row - 1) {
				pyramidStr += " ";
			} else {
				pyramidStr += "#";
			}
		}
		console.log(pyramidStr);
	}
}

module.exports = pyramid;
