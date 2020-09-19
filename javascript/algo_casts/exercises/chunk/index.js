// --- Directions
// Given an array and chunk size, divide the array into many subarrays
// where each subarray is of length size
// --- Examples
// chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
// chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
// chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
// chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
// chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]

function chunk(array, size) {
	var arr = [];
	var subArr = [];
	var increment = 0;
	console.log("Starting ########### " + size);

	for (let index = 0; index < array.length; index++) {
		if (increment < size) {
			subArr.push(array[index]);
			increment++;
		} else {
			arr.push(subArr);
			subArr = [];
			subArr.push(array[index]);
			increment = 1;
		}
		// Endgame if only 1 case last check
		if (array.length - 1 === index) {
			arr.push(subArr);
		}
	}

	/*
	array.forEach((element) => {
		console.log("Printing element: " + element);
		if (increment < size) {
			subArr.push(element);
			increment++;
		} else {
			arr.push(subArr);
			subArr = [];
			subArr.push(element);
			increment = 1;
		}
	});
	*/

	/*
	for (const index of array) {
		console.log("Printing index: " + index);
		console.log("Printing element: " + array[index]);
		console.log("Length of array: " + array.length);
		if (increment < size) {
			subArr.push(element);
			increment++;
			if (array.length - 1 === index + 1) {
				arr.push(subArr);
			}
		} else {
			arr.push(subArr);
			subArr = [];
			subArr.push(element);
			increment = 1;
		}
	}

	*/

	return arr;
}

// chunk([1, 2, 3, 4], 2);

chunk([1, 2, 3], 1);

module.exports = chunk;
