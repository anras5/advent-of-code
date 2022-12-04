package day3

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func Zad3() {
	file, _ := os.Open("data3.txt")
	defer file.Close()
	scanner := bufio.NewScanner(file)

	score := 0

	for scanner.Scan() {

		listOfContents := scanner.Text()

		firstRucksack := listOfContents[:len(listOfContents)/2]
		secondRucksack := listOfContents[len(listOfContents)/2:]

		for _, char := range firstRucksack {
			if strings.ContainsRune(secondRucksack, char) {
				points := int(char)
				if points > 96 {
					score += points - 96
				} else {
					score += points - 38
				}
				break
			}
		}

	}

	fmt.Println(score)
}
