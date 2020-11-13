// --- Directions
// 1) Implement the Node class to create
// a binary search tree.  The constructor
// should initialize values 'data', 'left',
// and 'right'.
// 2) Implement the 'insert' method for the
// Node class.  Insert should accept an argument
// 'data', then create an insert a new node
// at the appropriate location in the tree.
// 3) Implement the 'contains' method for the Node
// class.  Contains should accept a 'data' argument
// and return the Node in the tree with the same value.

class Node {
	constructor(data) {
		this.data = data;
		this.left = null;
		this.right = null;
	}

	insert(data, node) {
		// Recursive if condition check
		if (node) {
			if (data < node.data) {
				if (node.left) {
					this.insert(data, node.left);
				} else {
					node.left = new Node(data);
				}
			} else {
				if (node.right) {
					this.insert(data, node.right);
				} else {
					node.right = new Node(data);
				}
			}
		} else if (this.data) {
			if (data < this.data) {
				if (this.left) {
					this.insert(data, this.left);
				} else {
					this.left = new Node(data);
				}
			} else {
				if (this.right) {
					this.insert(data, this.right);
				} else {
					this.right = new Node(data);
				}
			}
		}

		// Too many if else conditions,
		// I need to work on logical coding and combining logical conditions with this function.
		// But this is my first draft and also first proper try to work on recursion
		// I did have to utilize a debugger to go through the loops and visualize the exit condition.
	}

	contains(data) {
		if (data === this.data) {
			return this;
		}

		if (data < this.data && this.left) {
			return this.left.contains(data);
		} else if (data > this.data && this.right) {
			return this.right.contains(data);
		}

		return null;
	}
}

module.exports = Node;
const node = new Node(10);
node.insert(5);
node.insert(15);
node.insert(17);
