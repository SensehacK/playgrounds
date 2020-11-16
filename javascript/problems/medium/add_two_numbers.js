/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

/**
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

 */

//  Definition for singly - linked list.
function ListNode(val, next) {
	this.val = val === undefined ? 0 : val;
	this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
	const arr1 = [];
	const arr2 = [];
	while (l1) {
		// console.log(l1.val);
		arr1.push(l1.val);
		l1 = l1 ? l1.next : null;
	}

	while (l2) {
		// console.log(l2.val);
		arr2.push(l2.val);
		l2 = l2 ? l2.next : null;
	}
	const reverseArr1 = arr1.toString().split(",").reverse().join("");
	//console.log(reverseArr1);
	const reverseArr2 = arr2.toString().split(",").reverse().join("");
	//console.log(reverseArr2);

	const intArr1 = parseInt(reverseArr1);
	const intArr2 = parseInt(reverseArr2);
	// console.log(intArr1, intArr2);
	const result = intArr1 + intArr2;
	//console.log(result);
	const resultStr = result.toString().split("").join("");
	// console.log(resultStr);
	// console.log("Length", resultStr.length);

	var tempNode = new ListNode(parseInt(resultStr[0]));
	// console.log(headNode.val);
	// var tempN = new ListNode(24, headNode);
	// console.log(tempN);

	for (let index = 1; index < resultStr.length; index++) {
		// console.log("Array Value");
		// console.log(resultStr[index]);
		// console.log("Temporary node Value");
		// console.log(tempNode.val);
		// console.log(tempNode);
		tempNode = new ListNode(parseInt(resultStr[index]), tempNode);
		// console.log("after reassign");
		// console.log(tempNode);
		// if (index == resultStr.length - 1) {
		// 	tempNode = new ListNode(parseInt(resultStr[index]));
		// } else {
		// 	tempNode = new ListNode(parseInt(resultStr[index], tempNode));
		// }
	}
	// console.log("Looping tempNode");

	// Needed to comment out tempNode while loop as the next variable of tempnode was getting overridden by the loop
	// while (tempNode) {
	// 	console.log(tempNode.val);
	// 	// console.log(tempNode.next);
	// 	tempNode = tempNode.next ? tempNode.next : null;
	// }

	return tempNode;
	// for (let variable of resultStr) {
	// 	//console.log(variable);

	// 	let node2 = new ListNode(4, node3);
	// 	let node1 = new ListNode(8, node2);
	// 	resultArr.push();
	// }
	// console.log(resultArr);
	// return resultArr;
};

var printS = function () {
	console.log("Hello Sensehack!");
};

// printS();
let node3 = new ListNode(1);
let node2 = new ListNode(4, node3);
let node1 = new ListNode(8, node2);

let bode3 = new ListNode(3);
let bode2 = new ListNode(6, bode3);
let bode1 = new ListNode(5, bode2);

addTwoNumbers(node1, bode1);
