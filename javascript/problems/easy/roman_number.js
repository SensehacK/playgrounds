/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
	var count = s.length;
	console.log("Count of s: ", count);
	var stack = s.split("").join("");

	var result = 0;

	for (let index = 0; index < count; index++) {
		const element_one = stack[index];
		const element_two = stack[index + 1];
		console.log("Printing Index start", index);
		if (element_one == "I") {
			result = result + 1;
			if (element_two == "V") {
				result = result + 3;
				index++;
			} else if (element_two == "X") {
				result = result + 8;
				index++;
			}
			console.log("Printing Index", index);
		} else if (element_one == "V") {
			result = result + 5;
		} else if (element_one == "X") {
			result = result + 10;
			if (element_two == "L") {
				result = result + 30;
				index++;
			} else if (element_two == "C") {
				result = result + 80;
				index++;
			}
		} else if (element_one == "L") {
			result = result + 50;
		} else if (element_one == "C") {
			result = result + 100;

			if (element_two == "D") {
				result = result + 300;
				index++;
			} else if (element_two == "M") {
				result = result + 800;
				index++;
			}
		} else if (element_one == "D") {
			result = result + 500;
		} else if (element_one == "M") {
			result = result + 1000;
		}
		console.log("Printing Index end", index);
		console.log("Printing result every loop", result);
	}

	console.log("Final result: ", result);
	// if(stack[0])
	return result;
};

// romanToInt("LVIII");

// romanToInt("III");
// romanToInt("VIII");

romanToInt("MCMXCIV");
