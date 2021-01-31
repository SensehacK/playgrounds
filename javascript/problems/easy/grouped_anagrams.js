const { group } = require("console");

function groupedAnagrams(strs) {
	console.log("Hello", strs);
	console.log("Hello tye", typeof strs);



	strs.forEach((word) => {
		console.log("Hello arr", word);
		var sortedStr = word.split("").sort();
		console.log("Sorted", sortedStr.join(""));
	});
}

var anagram = ["tea", "eat"];
groupedAnagrams(anagram);
