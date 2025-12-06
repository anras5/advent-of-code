package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func main() {

	file, _ := os.Open("input.txt")
	scanner := bufio.NewScanner(file)

	var values [][]int
	var partialAnswers []int

	var finalAnswer int
	var re = regexp.MustCompile(`\s+`)
	for scanner.Scan() {
		line := scanner.Text()
		lineNormalized := strings.TrimSpace(line)
		lineNormalized = re.ReplaceAllString(lineNormalized, " ")
		lineValues := strings.Split(lineNormalized, " ")

		for i, value := range lineValues {
			intValue, err := strconv.Atoi(value)
			if err != nil {
				break
			}
			if i > len(values)-1 {
				values = append(values, []int{})
			}
			values[i] = append(values[i], intValue)
		}

		for i, sign := range lineValues {
			if sign == "*" {
				answer := 1
				for _, value := range values[i] {
					answer *= value
				}
				partialAnswers = append(partialAnswers, answer)
			} else if sign == "+" {
				answer := 0
				for _, value := range values[i] {
					answer += value
				}
				partialAnswers = append(partialAnswers, answer)
			}
		}
		for _, value := range partialAnswers {
			finalAnswer += value
		}
	}
	fmt.Println(values)
	fmt.Println(partialAnswers)
	fmt.Println(finalAnswer)

}
