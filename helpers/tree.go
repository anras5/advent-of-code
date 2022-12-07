package helpers

import "fmt"

type TreeNode struct {
	Name     string
	Size     int
	Parent   *TreeNode
	Children []*TreeNode
}

// FindChild returns the child of the given node with the given value, or nil if no such child exists
func FindChild(node *TreeNode, name string) *TreeNode {
	for _, child := range node.Children {
		//fmt.Println(child.Name)
		if child.Name == name {
			return child
		}
	}
	return nil
}

// PrintTree prints the tree rooted at the given node in a readable format
func PrintTree(root *TreeNode, level int) {
	// Print the value of the current node and its level
	fmt.Printf("%*s%s - %d\n", level*2, "", root.Name, root.Size)

	// Recursively print the children of the current node
	for _, child := range root.Children {
		PrintTree(child, level+1)
	}
}

func AssignSize(root *TreeNode) {
	if root == nil {
		return
	}

	for _, child := range root.Children {
		AssignSize(child)
		root.Size += child.Size
	}
}

func FindNodeSizes(root *TreeNode) []int {
	var result []int

	// Recursively search through the tree
	var search func(node *TreeNode)
	search = func(node *TreeNode) {
		// Check if the current node has children and a size larger than 100000
		if node.Children != nil && node.Size < 100000 {
			result = append(result, node.Size)
		}

		// Recurse on all children of the current node
		for _, child := range node.Children {
			search(child)
		}
	}

	// Start the search at the root node
	search(root)

	return result

}

func FindTheSmallest(root *TreeNode, memoryAll, memoryNeeded, memoryTaken int) int {

	var possibleDirs []*TreeNode

	var search func(node *TreeNode)
	search = func(node *TreeNode) {
		// Check if the current node is directory and is suitable to free up enough space

		unusedMemory := memoryAll - (memoryTaken - node.Size)

		if node.Children != nil && unusedMemory > memoryNeeded {
			possibleDirs = append(possibleDirs, node)
		}

		for _, child := range node.Children {
			search(child)
		}
	}

	search(root)

	// Find node with minimal suitable memory
	smallestNode := possibleDirs[0]
	for _, node := range possibleDirs {
		if smallestNode.Size > node.Size {
			smallestNode = node
		}
	}

	return smallestNode.Size

}
