// --- Directions
// Return the 'middle' node of a linked list.
// If the list has an even number of elements, return
// the node at the end of the first half of the list.
// *Do not* use a counter variable, *do not* retrieve
// the size of the list, and only iterate
// through the list one time.
// --- Example
//   const l = new LinkedList();
//   l.insertLast('a')
//   l.insertLast('b')
//   l.insertLast('c')
//   midpoint(l); // returns { data: 'b' }

function midpoint(list) {
	var shortJump = list.getFirst();
	var fastJump = list.getFirst();

	console.log("current linkedList: ", list);
	// shortJump = shortJump.next;

	// console.log("next linkedList shortJump : ", shortJump);

	// fastJump = shortJump.next;
	// console.log("next linkedList fastJump : ", fastJump);

	while (fastJump.next) {
		if (fastJump.next && shortJump.next) {
			fastJump = fastJump.next;
			console.log("next linkedList shortJump : ", shortJump);
			console.log("next linkedList fastJump : ", fastJump);

			if (fastJump.next) {
				fastJump = fastJump.next;
				shortJump = shortJump.next;
				console.log("next linkedList fastJump fastJump.next: ", fastJump);
			} else {
				break;
			}
		}
	}
	return shortJump;
}

module.exports = midpoint;

// const L = require("./linkedlist");
// const Node = L.Node;
// const LinkedList = L.LinkedList;
// const l = new LinkedList();
// l.insertLast("a");
// l.insertLast("b");
// l.insertLast("c");
// l.insertLast("d");
// // l.insertLast("e");
// console.log(midpoint(l).data);
