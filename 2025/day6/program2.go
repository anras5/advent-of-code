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

	var stringValues []string
	var operations []string
	for scanner.Scan() {
		line := scanner.Text()

		if strings.HasPrefix(line, "*") || strings.HasPrefix(line, "+") {

			var re = regexp.MustCompile(`\s+`)
			lineNormalized := strings.TrimSpace(line)
			lineNormalized = re.ReplaceAllString(lineNormalized, " ")
			operations = strings.Split(lineNormalized, " ")
			break
		}

		for i, char := range line {
			if i > len(stringValues)-1 {
				stringValues = append(stringValues, string(char))
			} else {
				stringValues[i] = fmt.Sprintf("%s%s", stringValues[i], string(char))
			}
		}
	}

	var values [][]int
	var i int
	var buffer []int
	for i < len(stringValues) {
		if strings.TrimSpace(stringValues[i]) == "" {
			values = append(values, buffer)
			buffer = []int{}
		} else {
			value, _ := strconv.Atoi(strings.TrimSpace(stringValues[i]))
			buffer = append(buffer, value)
		}
		i++
	}
	values = append(values, buffer)

	var partialAnswers []int
	var finalAnswer int
	for i, sign := range operations {
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

	fmt.Println(partialAnswers)
	fmt.Println(finalAnswer)

}
