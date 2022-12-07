package day7

import (
	"bufio"
	"github.com/anras5/AdventOfCode2022/helpers"
	"os"
	"strconv"
	"strings"
)

func loadData() *helpers.TreeNode {
	file, _ := os.Open("day7/data7.txt")
	scanner := bufio.NewScanner(file)

	var currentNode *helpers.TreeNode
	var root *helpers.TreeNode

	// build tree
	for scanner.Scan() {

		args := strings.Split(scanner.Text(), " ")

		if args[0] == "$" {
			if args[1] == "cd" {
				if args[2] == "/" {
					// cd to root
					currentNode = &helpers.TreeNode{
						Name: "/",
					}
					root = currentNode
				} else if args[2] == ".." {
					// cd one up
					currentNode = currentNode.Parent
				} else {
					// cd to folder
					child := helpers.FindChild(currentNode, args[2])
					currentNode = child
				}
			}
			if args[1] == "ls" {
				// ls files
			}
		} else if args[0] == "dir" {
			// create new child - dir
			child := &helpers.TreeNode{
				Name:   args[1],
				Parent: currentNode,
			}
			currentNode.Children = append(currentNode.Children, child)
		} else {
			// create new child - file
			size, _ := strconv.Atoi(args[0])
			child := &helpers.TreeNode{
				Name:   args[1],
				Size:   size,
				Parent: currentNode,
			}
			currentNode.Children = append(currentNode.Children, child)
		}
	}

	return root
}

func Zad7() int {

	root := loadData()

	//Print the tree
	//helpers.PrintTree(root, 0)

	// Assign sizes to directories
	helpers.AssignSize(root)

	// Find nodes that have children and are smaller than 100000
	sizes := helpers.FindNodeSizes(root)
	var total int
	for _, number := range sizes {
		total += number
	}
	return total

}

func Zad7b() int {
	root := loadData()

	// Assign sizes to directories
	helpers.AssignSize(root)

	// Get size of the node
	return helpers.FindTheSmallest(root, 70000000, 30000000, root.Size)

}
