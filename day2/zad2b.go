package day2

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func Zad2b() {
	file, err := os.Open("day2/data2.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	score := 0

	rules := map[string]int{
		"A X": 3 + 0,
		"A Y": 1 + 3,
		"A Z": 2 + 6,
		"B X": 1 + 0,
		"B Y": 2 + 3,
		"B Z": 3 + 6,
		"C X": 2 + 0,
		"C Y": 3 + 3,
		"C Z": 1 + 6,
	}

	for scanner.Scan() {

		score += rules[scanner.Text()]

	}

	fmt.Println(score)
}
