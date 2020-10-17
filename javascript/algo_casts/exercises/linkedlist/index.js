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
}

module.exports = { Node, LinkedList };
