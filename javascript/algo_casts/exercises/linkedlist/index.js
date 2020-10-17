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
		console.log("#########", currentNode);
		// console.log("#########", this.head.next);

		// console.log("#### currentNode.next ", currentNode.next);
		// console.log("#### currentNodetype of ", typeof currentNode.next);
		// if currentNode
		while (currentNode) {
			currentNode = currentNode.next;
			size++;
			console.log("Hello next node", currentNode);
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
}

// const list = new LinkedList();
// list.insertFirst(6);
// list.insertFirst(12);
// list.insertFirst(9);
// list.insertFirst(3);
// console.log("listets");
// console.log(list);

// const sie = list.size();
// console.log("Size", sie);

module.exports = { Node, LinkedList };
