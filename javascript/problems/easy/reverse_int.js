/**

Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

Example 4:

Input: x = 0
Output: 0


Constraints:

    -231 <= x <= 231 - 1

*/

/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
	console.log(x);
	const reverseStr = x.toString().split("").reverse().join("");
	console.log(reverseStr);
	const limit = 2147483648; // Integer 32 bit
	const integer = parseInt(reverseStr);
	console.log("Parsed:", integer);
	const tempVar = Math.sign(x) == 1 ? integer : integer - integer * 2;
	return integer > limit ? 0 : tempVar;
};
