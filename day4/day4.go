package day4

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

func Zad4() int {
	file, _ := os.Open("day4/data4.txt")
	defer file.Close()
	scanner := bufio.NewScanner(file)

	score := 0

	for scanner.Scan() {

		assignmentPairs := strings.Split(scanner.Text(), ",")
		firstAssignment := strings.Split(assignmentPairs[0], "-")
		secondAssignment := strings.Split(assignmentPairs[1], "-")

		firstA0, _ := strconv.Atoi(firstAssignment[0])
		firstA1, _ := strconv.Atoi(firstAssignment[1])
		secondA0, _ := strconv.Atoi(secondAssignment[0])
		secondA1, _ := strconv.Atoi(secondAssignment[1])

		if (firstA0 <= secondA0 && firstA1 >= secondA1) || (secondA0 <= firstA0 && secondA1 >= firstA1) {
			score += 1
		}

	}
	return score

}

func Zad4b() int {
	file, _ := os.Open("day4/data4.txt")
	defer file.Close()
	scanner := bufio.NewScanner(file)

	score := 0

	for scanner.Scan() {

		assignmentPairs := strings.Split(scanner.Text(), ",")
		firstAssignment := strings.Split(assignmentPairs[0], "-")
		secondAssignment := strings.Split(assignmentPairs[1], "-")

		firstA0, _ := strconv.Atoi(firstAssignment[0])
		firstA1, _ := strconv.Atoi(firstAssignment[1])
		secondA0, _ := strconv.Atoi(secondAssignment[0])
		secondA1, _ := strconv.Atoi(secondAssignment[1])

		if !((firstA1 < secondA0) || (secondA1 < firstA0)) {
			score += 1
		}

	}
	return score
}
