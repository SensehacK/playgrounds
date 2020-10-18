// --- Directions
// Implement classes Node and Linked Lists
// See 'directions' document

class Node {
	constructor(data, next = null) {
		this.data = data;
		this.next = next;
	}
}

class LinkedList {
	constructor() {
		this.head = null;
	}

	insertFirst(data) {
		var tempNode = new Node(data);
		tempNode.next = this.head;
		this.head = tempNode;
	}

	size() {
		var size = 0;
		var currentNode = this.head;
		// console.log("#########", currentNode);
		// console.log("#########", this.head.next);

		// console.log("#### currentNode.next ", currentNode.next);
		// console.log("#### currentNodetype of ", typeof currentNode.next);
		// if currentNode
		while (currentNode) {
			currentNode = currentNode.next;
			size++;
			// console.log("Hello next node", currentNode);
		}

		/*
		while (currentNode.next != null) {
			size += 1;
			currentNode = this.head.next;
		}
		*/
		return size;
	}

	getFirst() {
		return this.head;
	}

	getLast() {
		const arraySize = this.size();
		var currentNode = this.head;
		for (let index = 0; index < arraySize; index++) {
			if (index == arraySize - 1) {
				return currentNode;
			}
			currentNode = currentNode.next;
		}
	}

	clear() {
		this.head = null;
	}

	removeFirst() {
		if (this.head) {
			this.head = this.head.next;
		}
	}

	removeLast() {
		if (this.head) {
			const arraySize = this.size();
			var currentNode = this.head;
			for (let index = 0; index < arraySize; index++) {
				if (index == arraySize - 2) {
					currentNode.next = null;
					// Returning doesn't get you anything,
					// it just prevents the last statement from running in the loop.
					return;
				} else if (arraySize == 1) {
					this.removeFirst();
				}
				currentNode = currentNode.next;
			}
		}
	}

	insertLast(data) {
		var tempNode = new Node(data);
		// Doesn't check whether Getlast function returns any node object. Zero LinkedList scenario
		console.log("Last Data", this.getLast());
		if (this.getLast()) {
			this.getLast().next = tempNode;
		} else {
			this.head = tempNode;
		}
	}

	getAt(step) {
		const arraySize = this.size();
		var currentNode = this.head;
		for (let index = 0; index < arraySize; index++) {
			if (index == step) {
				return currentNode;
			} else {
				currentNode = currentNode.next;
			}
		}
		return null;
	}

	removeAt(step) {
		const arraySize = this.size() - 1;
		var previousNode = this.getAt(step - 1);
		var nextNode = this.getAt(step + 1);
		if (step <= arraySize && step >= 0) {
			if (previousNode) {
				console.log("previous Node", previousNode);
				console.log("Next Node", nextNode);
				previousNode.next = nextNode;
			} else {
				this.head = nextNode;
			}
		}
		// No need for extra checks as javascript assigns returns null value directly.
		else if (step == arraySize) {
			// previousNode.next = null;
		} else if (step == 0) {
			// this.head = null;
		}
	}

	insertAt(data, step) {
		var tempNode = new Node(data);
		const arraySize = this.size() - 1;
		var previousNode = this.getAt(step - 1);
		var nextNode = this.getAt(step);
		console.log("previous Node", previousNode);
		console.log("Next Node", nextNode);
		console.log("arraySize", arraySize);

		// Maybe this two if conditions could be utilized in just calling Insert Last function.
		// Reusable code.
		if (arraySize == -1) {
			this.head = tempNode;
		}

		if (step == arraySize + 1 || step > arraySize) {
			this.getLast().next = tempNode;
		}
		// if (!previousNode) {
		// 	console.log("!previousNode");
		// 	tempNode.next = nextNode;
		// 	this.head = tempNode;
		// }

		if (step <= arraySize && step >= 0) {
			if (previousNode) {
				console.log("previous Node", previousNode);
				console.log("Next Node", nextNode);
				previousNode.next = tempNode;
				tempNode.next = nextNode;
			} else {
				console.log("Else condition");
				// this.head = tempNode;
				console.log("!previousNode");
				tempNode.next = nextNode;
				this.head = tempNode;
			}
		}
	}

	forEach(node) {
		console.log(typeof node);
	}
}

// const list = new LinkedList();
// list.insertFirst(6);
// list.insertFirst(12);
// list.insertFirst(9);
// list.insertFirst(3);
// list.insertLast(24);
// console.log("listets");
// console.log(list);

// const sie = list.size();
// console.log("Size", sie);

/* Test to check insertLast func with empty linkedlist
const list = new LinkedList();
list.insertLast(24);
console.log(list);
*/

/* Tests for checking last Node remove At
const list = new LinkedList();
console.log(list);

list.insertLast(10);
list.insertLast(20);
list.insertLast(30);
list.insertLast(40);
list.removeAt(3);
console.log(list.getAt(3));
/* Printing logs
LinkedList { head: null }
Last Data undefined
Last Data Node { data: 10, next: null }
Last Data Node { data: 20, next: null }
Last Data Node { data: 30, next: null }
previous Node Node { data: 30, next: Node { data: 40, next: null } }
Next Node null
null
*/

// */

// /*
// const list = new LinkedList();
// console.log(list);
// list.insertAt("hi", 0);
// console.log(list);
// console.log("Get First");
// console.log(list.getFirst());

// const l = new LinkedList();
// l.insertLast("a");
// l.insertLast("b");
// l.insertLast("c");
// l.insertAt("hi", 0);
// console.log(l.getAt(0).data);
// console.log(l.getAt(1).data);
// console.log(l.getAt(2).data);
// console.log(l.getAt(3).data);

// const l = new LinkedList();
// l.insertLast("a");
// l.insertLast("b");
// l.insertAt("hi", 2);
// console.log(l.getAt(0).data);
// console.log(l.getAt(1).data);
// console.log(l.getAt(2).data);

// */

// /*
// const l = new LinkedList();

// l.insertLast(1);
// l.insertLast(2);
// l.insertLast(3);
// l.insertLast(4);

// l.forEach((node) => {
// 	node.data += 10;
// });

// */
module.exports = { Node, LinkedList };
