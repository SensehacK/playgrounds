// --- Directions
// Given a linked list, return true if the list
// is circular, false if it is not.
// --- Examples
//   const l = new List();
//   const a = new Node('a');
//   const b = new Node('b');
//   const c = new Node('c');
//   l.head = a;
//   a.next = b;
//   b.next = c;
//   c.next = b;
//   circular(l) // true

function circular(list) {
	var shortJump = list.getFirst();
	var fastJump = list.getFirst();

	while (fastJump.next && fastJump.next.next) {
		// console.log(" while fastJump.next  :", fastJump.next);
		shortJump = shortJump.next;
		fastJump = fastJump.next.next;
		// console.log("next linkedList shortJump : ", shortJump);
		// console.log("next linkedList fastJump : ", fastJump);
		if (fastJump === shortJump) {
			return true;
		}
	}
	return false;
}

module.exports = circular;

// const L = require("./linkedlist");
// const Node = L.Node;
// const LinkedList = L.LinkedList;
// const l = new LinkedList();
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// l.head = a;
// a.next = b;
// b.next = c;
// c.next = null;
// console.log(circular(l)); // true
