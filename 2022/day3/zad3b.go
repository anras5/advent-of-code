package day3

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func Zad3b() {
	file, _ := os.Open("data3.txt")
	defer file.Close()
	scanner := bufio.NewScanner(file)

	score := 0
	var set []string

	for scanner.Scan() {

		set = append(set, scanner.Text())

		if len(set) == 3 {
			for _, char := range set[0] {
				if strings.ContainsRune(set[1], char) && strings.ContainsRune(set[2], char) {
					points := int(char)
					if points > 96 {
						score += points - 96
					} else {
						score += points - 38
					}
					break
				}
			}
			set = nil

		}

	}

	fmt.Println(score)
}
