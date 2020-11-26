function isPrime(n) {
	// Write your code here
	for (let i = 2; i < n; i++) {
		console.log(i);
		if (n % i == 0) {
			console.log(i);
			return i;
		}
	}
	return 1;
}

console.log("Your prime numbers:" + isPrime(4));
