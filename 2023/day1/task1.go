package day1

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func Task1() {

	file, err := os.Open("day1/data.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	sum := 0
	for scanner.Scan() {
		line := scanner.Text()
		firstNumberFound := false
		var firstNumber, secondNumber string
		for _, c := range line {
			_, err := strconv.Atoi(string(c))
			if err == nil {
				if !firstNumberFound {
					firstNumber = string(c)
					firstNumberFound = true
				}
				secondNumber = string(c)
			}
		}
		combined, _ := strconv.Atoi(firstNumber + secondNumber)
		sum += combined
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	fmt.Println(sum)
}

func Reverse(s string) (result string) {
	for _, v := range s {
		result = string(v) + result
	}
	return
}

func Task2() {

	replacer := strings.NewReplacer(
		"one", "1",
		"two", "2",
		"three", "3",
		"four", "4",
		"five", "5",
		"six", "6",
		"seven", "7",
		"eight", "8",
		"nine", "9",
	)

	replacerReversed := strings.NewReplacer(
		"eno", "1",
		"owt", "2",
		"eerht", "3",
		"ruof", "4",
		"evif", "5",
		"xis", "6",
		"neves", "7",
		"thgie", "8",
		"enin", "9",
	)

	file, err := os.Open("day1/data.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	sum := 0
	for scanner.Scan() {
		line := scanner.Text()
		line = replacer.Replace(line)
		var firstNumber, secondNumber string
		for _, c := range line {
			if _, err := strconv.Atoi(string(c)); err == nil {
				firstNumber = string(c)
				break
			}
		}
		line = scanner.Text()
		line = Reverse(line)
		line = replacerReversed.Replace(line)
		for _, c := range line {
			if _, err := strconv.Atoi(string(c)); err == nil {
				secondNumber = string(c)
				break
			}
		}
		combined, _ := strconv.Atoi(firstNumber + secondNumber)
		sum += combined
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	fmt.Println(sum)
}
