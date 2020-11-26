function groupSort(arr) {
	// Write your code here
	const frequency = {};
	arr.sort().reverse();
	console.log(arr);
	for (let value = 0; value < arr.length; value++) {
		console.log("vAlue: ", arr[value]);

		if (frequency[arr[value]]) {
			frequency[arr[value]] += 1;
		} else {
			frequency[arr[value]] = 1;
		}
	}

	console.log("frequency: ");
	console.log(frequency);
	var result = [];
	var sameArrItem = [];
	for (let value in frequency) {
		console.log("frequency Value: ");
		if (frequency.hasOwnProperty(value)) {
			console.log(value + " " + frequency[value]);
			sameArrItem.push(frequency[value]);
			result.push(frequency[value]);
			result.push(parseInt(value));
		}
	}
	let isDiffFrequency = false;
	let tempItem = sameArrItem[0];
	for (let item of sameArrItem) {
		console.log(item);
		if (tempItem !== item) {
			console.log("Result array frequency", result);
			console.log("Result array frequency reverse", result.reverse());
			isDiffFrequency = true;
		}
	}

	console.log("length : " + result.length);
	console.log("value at 2 : " + result[2]);

	let finalResultArr = [];
	for (let i = 0; i < result.length; i += 2) {
		console.log(result[i + 1] + " " + result[i]);
		if (isDiffFrequency) {
			finalResultArr.push([result[i], result[i + 1]]);
		} else {
			finalResultArr.push([result[i + 1], result[i]]);
		}
	}
	console.log("final arr");
	console.log(finalResultArr);
}

let arr = [2, 1, 2, 2];
let ar2r = [7, 12, 3];

const result = groupSort(arr);
