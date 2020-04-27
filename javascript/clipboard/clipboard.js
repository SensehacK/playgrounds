function myFunction() {
	var copyText = document.getElementById("myInput");
	console.log("Hi Kautilya");
	copyText.select();
	copyText.setSelectionRange(0, 99999);
	document.execCommand("copy");
	//alert("Copied the text: " + copyText.value);
	console.log("printing copytext", copyText.value);
}

function latestClipboard() {
	var copyText = document.getElementById("myInput2");
	navigator.clipboard.writeText(copyText.value).then(
		function () {
			/* clipboard successfully set */
			console.log("clip board set");
		},
		function () {
			/* clipboard write failed */
			alert("Copied the text: " + copyText.value);
			console.log("clip board failed");
		}
	);
}
