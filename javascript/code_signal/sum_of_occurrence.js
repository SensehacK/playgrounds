// Add every ith digit of the first string to the ith digit of the second string, both counted from the end. If the ith digit of one of the strings is absent, the sum will be the ith digit of the other string. Return a string of those sums concatenated with each other.

// Example

//     For a = "99" and b = "99", the output should be sumOfStrings(a, b) = "1818".

//     The sums of both, the first and the second numbers are 18, so the answer is 1818.

//     For a = "11" and b = "9", the output should be sumOfStrings(a, b) = "110".

//     The sum of the first numbers from the end is 10, and the sum of the second numbers from the end is 1, so the answer is 110.

function sumOfStrings(a, b) {
	let strA = a.toString().split("").reverse().join("");
	let strB = b.toString().split("").reverse().join("");
	var sumCount = [];

	var countArr = {};
	var isCarry = 0;

	let isFirstLong = strA.length < strB.length ? false : true;
	let numberDigits = isFirstLong ? strB.length : strA.length;

	for (let index = 0; index < numberDigits; index++) {
		const elementA = strA[index];
		const elementB = strB[index];
		var result = parseInt(elementA) + parseInt(elementB) + isCarry;
		/*
		if (result > 9) {
			isCarry = 1;
		}
		if (index == strA.length - 1) {
			result++;
		}
		*/
		countArr[index] = result;
	}

	for (const key in countArr) {
		if (countArr.hasOwnProperty(key)) {
			sumCount.push(countArr[key]);
		}
	}

	// Handle the difference in two numbers.
	let diffDigits = Math.abs(strA.length - strB.length);
	let startingIndex = isFirstLong ? strA.length : strB.length;
	let remainingStr = isFirstLong ? strA : strB;

	for (let index = startingIndex - diffDigits; index <= diffDigits; index++) {
		const element = remainingStr[index];
		sumCount.push(parseInt(element));
	}
	console.log(sumCount.reverse().join(""));
	return sumCount.join("");
}

//sumOfStrings(11, 90);
// sumOfStrings(11, 9);
sumOfStrings(99, 99);
