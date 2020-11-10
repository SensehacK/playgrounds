// --- Directions
// Given a linked list, return the element n spaces
// from the last node in the list.  Do not call the 'size'
// method of the linked list.  Assume that n will always
// be less than the length of the list.
// --- Examples
//    const list = new List();
//    list.insertLast('a');
//    list.insertLast('b');
//    list.insertLast('c');
//    list.insertLast('d');
//    fromLast(list, 2).data // 'b'

function fromLast(list, n) {
	var shortJump = list.getFirst();
	var fastJump = list.getFirst();

	for (let index = 0; index < n; index++) {
		fastJump = fastJump.next;
	}

	while (fastJump.next) {
		shortJump = shortJump.next;
		fastJump = fastJump.next;
		console.log("next linkedList shortJump : ", shortJump);
		console.log("next linkedList fastJump : ", fastJump);
	}

	return shortJump;
}

module.exports = fromLast;

const L = require("./linkedlist");
const Node = L.Node;
const LinkedList = L.LinkedList;
const list = new LinkedList();
list.insertLast("a");
list.insertLast("b");
list.insertLast("c");
list.insertLast("d");
console.log(fromLast(list, 2).data); // 'b'
