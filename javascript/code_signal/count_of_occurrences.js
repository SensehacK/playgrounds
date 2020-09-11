// For n = 10, the output should be countOccurrences(n) = 4.

// The digit 0 appears in numbers 0 and 10 once, for a total of 2 occurrences,
// The digit 2 appears in the number 2 once, for a total of 1 occurrence,
// The digit 4 appears in the number 4 once, for a total of 1 occurrence.

// So the answer is 2 + 1 + 1 = 4.

function countOccurrences(n) {
	var sumCount = 0;

	console.log(n.toString().length);
	var countArr = { 0: 0, 2: 0, 4: 0 };
	console.log("Number % 2" + (n % 2));
	for (let value = 0; value <= n; value++) {
		let variableStr = value.toString();
		for (let index = 0; index < variableStr.length; index++) {
			const element = variableStr[index];
			if (element == 0) {
				countArr[0]++;
			} else if (element == 2) {
				countArr[2]++;
			} else if (element == 4) {
				countArr[4]++;
			}
		}
	}

	for (const value in countArr) {
		sumCount += countArr[value];
	}
	return sumCount;
}

countOccurrences(22);
