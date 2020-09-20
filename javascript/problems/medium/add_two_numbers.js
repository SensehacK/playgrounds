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
	this.val = (val === undefined ? 0 : val)
	this.next = (next === undefined ? null : next)
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {

	while (l1) {
		console.log(l1.val)
		l1 = l1 ? l1.next : null
	}
};

var printS = function () {

	console.log("Hello Sensehack!")

};

printS()
let node3 = new ListNode(1)
let node2 = new ListNode(4, node3)
let node1 = new ListNode(8, node2)

let bode3 = new ListNode(3)
let bode2 = new ListNode(6, bode3)
let bode1 = new ListNode(5, bode2)


addTwoNumbers(node1, bode1)