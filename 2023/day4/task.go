package day4

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func Task1() {
	file, _ := os.Open("day4/data.txt")
	defer file.Close()
	scanner := bufio.NewScanner(file)

	sum := 0

	for scanner.Scan() {
		score := 0

		numbers := strings.Split(strings.Split(scanner.Text(), ":")[1], "|")
		winnings := strings.Split(strings.TrimSpace(numbers[0]), " ")
		numbers = strings.Split(strings.TrimSpace(numbers[1]), " ")

		var winningInts []int
		var numbersInt []int
		for _, winning := range winnings {
			if winning == "" {
				continue
			}
			winningInt, _ := strconv.Atoi(winning)
			winningInts = append(winningInts, winningInt)
		}
		for _, number := range numbers {
			if number == "" {
				continue
			}
			numberInt, _ := strconv.Atoi(number)
			numbersInt = append(numbersInt, numberInt)
		}

		for _, numberInt := range numbersInt {
			for _, winningInt := range winningInts {
				if winningInt == numberInt {
					if score == 0 {
						score = 1
					} else {
						score = score * 2
					}
					break
				}
			}
		}
		sum += score
	}
	fmt.Println(sum)
}

func Task2() {
	file, _ := os.Open("day4/data.txt")
	defer file.Close()
	scanner := bufio.NewScanner(file)

	answer := 0
	numberOfCopies := make(map[int]int)
	currentCard := 1
	numberOfCopies[currentCard] = 0

	for scanner.Scan() {

		for i := 0; i < numberOfCopies[currentCard]+1; i++ {
			answer++
			score := 0

			numbers := strings.Split(strings.Split(scanner.Text(), ":")[1], "|")
			winnings := strings.Split(strings.TrimSpace(numbers[0]), " ")
			numbers = strings.Split(strings.TrimSpace(numbers[1]), " ")

			var winningInts []int
			var numbersInt []int
			for _, winning := range winnings {
				if winning == "" {
					continue
				}
				winningInt, _ := strconv.Atoi(winning)
				winningInts = append(winningInts, winningInt)
			}
			for _, number := range numbers {
				if number == "" {
					continue
				}
				numberInt, _ := strconv.Atoi(number)
				numbersInt = append(numbersInt, numberInt)
			}

			for _, numberInt := range numbersInt {
				for _, winningInt := range winningInts {
					if winningInt == numberInt {
						score++
					}
				}
			}

			for i := currentCard + 1; i < currentCard+score+1; i++ {
				if _, exists := numberOfCopies[i]; !exists {
					numberOfCopies[i] = 0
				}
				numberOfCopies[i]++
			}
		}
		currentCard++
	}

	fmt.Println(answer)
}
