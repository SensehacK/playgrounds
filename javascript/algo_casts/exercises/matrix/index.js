// --- Directions
// Write a function that accepts an integer N
// and returns a NxN spiral matrix.
// --- Examples
//   matrix(2)
//     [[1, 2],
//     [4, 3]]
//   matrix(3)
//     [[1, 2, 3],
//     [8, 9, 4],
//     [7, 6, 5]]
//  matrix(4)
//     [[1,   2,  3, 4],
//     [12, 13, 14, 5],
//     [11, 16, 15, 6],
//     [10,  9,  8, 7]]

function matrix(n) {
	var tempAr = [[]];
	var startCol = 0;
	var startRow = 0;
	var endCol = n - 1;
	var endRow = n - 1;
	var value = 1;
	var currentRowRange = n;
	var currentColRange = n;

	for (let index = 0; index < n; index++) {
		tempAr[index] = [];

		for (let internalIndex = 0; internalIndex < n; internalIndex++) {
			tempAr[index][internalIndex] = 0;
		}
	}

	while (startRow <= endRow && startCol <= endCol) {
		if (value > n * n) {
			break;
		}

		for (let index = 0; index < currentColRange; index++) {
			tempAr[startRow][startCol] = value;
			value++;

			if (index == currentColRange - 1) {
				startRow++;
				currentRowRange--;
			} else {
				startCol++;
			}

			/*
			if (startCol == endCol) {
				startRow++;
				currentRowRange--;
			} else {
				startCol++;
			}
			*/
		}

		if (value > n * n) {
			break;
		}

		for (let index = 0; index < currentRowRange; index++) {
			tempAr[startRow][startCol] = value;
			value++;

			if (index == currentRowRange - 1) {
				startCol--;
				endCol--;
				currentColRange--;
			} else {
				startRow++;
			}

			/*
			if (startRow == endCol) {
				startCol--;
				endCol--;
				currentColRange--;
			} else {
				startRow++;
			}
			*/
		}

		if (value > n * n) {
			break;
		}

		for (let index = 0; index < currentColRange; index++) {
			tempAr[startRow][startCol] = value;
			value++;

			if (index == currentColRange - 1) {
				startRow--;
				endRow--;
				currentRowRange--;
			} else {
				startCol--;
			}
			/*
			if (startRow == endRow && startCol == 0) {
				startRow--;
				endRow--;
				currentRowRange--;
			} else {
				startCol--;
			}
			*/
		}

		if (value > n * n) {
			break;
		}

		for (let index = 0; index < currentRowRange; index++) {
			tempAr[startRow][startCol] = value;
			value++;

			if (index == currentRowRange - 1) {
				currentColRange--;
				startCol++;
			} else {
				startRow--;
			}
			/*
			if (startRow == endRow - 1) {
				startCol++;
			} else {
				startRow--;
			}
			*/
		}
	}

	return tempAr;
}

module.exports = matrix;

// console.log(matrix(2));
// console.log(matrix(3));
// console.log(matrix(4)); // works fine
console.log(matrix(5));
/*
function two_dimensional_arr() {
	var tempAr = [[]];

	for (let index = 0; index < n; index++) {
		tempAr[index] = [];
		for (let internalIndex = 0; internalIndex < n; internalIndex++) {
			tempAr[index][internalIndex] = index + internalIndex + 2;
		}
	}

	for (let index = 0; index < n; index++) {
		for (let internalIndex = 0; internalIndex < n; internalIndex++) {
			console.log(tempAr[index][internalIndex]);
		}
	}
}
*/
