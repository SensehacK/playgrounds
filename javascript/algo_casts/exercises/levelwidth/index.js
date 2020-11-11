// --- Directions
// Given the root node of a tree, return
// an array where each element is the width
// of the tree at each level.
// --- Example
// Given:
//     0
//   / |  \
// 1   2   3
// |       |
// 4       5
// Answer: [1, 3, 2]

function levelWidth(root) {
	var counters = [0];
	var treeArr = [root, "s"];
	while (treeArr.length > 1) {
		const node = treeArr.shift();

		if (node === "s") {
			counters.push(0);
			treeArr.push("s");
		} else {
			counters[counters.length - 1]++;
			treeArr.push(...node.children);
		}
	}
	return counters;
}

module.exports = levelWidth;

