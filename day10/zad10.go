package day10

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func checkCycle(cycleNumber int) bool {
	switch cycleNumber {
	case 20, 60, 100, 140, 180, 220:
		return true
	default:
		return false
	}
}

func sum(list []int) int {
	var result int
	for _, val := range list {
		result += val
	}
	return result
}

func Zad10() int {

	file, _ := os.Open("day10/data10.txt")
	scanner := bufio.NewScanner(file)
	defer file.Close()

	cycle := 0
	X := 1
	var results []int

	for scanner.Scan() {

		text := scanner.Text()
		instruction := strings.Split(text, " ")
		if instruction[0] == "noop" {
			cycle++
			if checkCycle(cycle) {
				results = append(results, cycle*X)
			}
		} else {
			cycle++
			if checkCycle(cycle) {
				results = append(results, cycle*X)
			}
			cycle++
			if checkCycle(cycle) {
				results = append(results, cycle*X)
			}
			add, _ := strconv.Atoi(instruction[1])
			X += add

		}

	}
	return sum(results)
}

func printToConsole(cycleNumber int, val int) {
	//fmt.Println(cycleNumber, val)
	if math.Abs(float64((cycleNumber%40)-val)) <= 1 {
		fmt.Print("#")
	} else {
		fmt.Print(".")
	}
	switch cycleNumber {
	case 39, 79, 119, 159, 199, 239:
		fmt.Print("\n")
	}
}

func Zad10b() {

	file, _ := os.Open("day10/data10.txt")
	scanner := bufio.NewScanner(file)
	defer file.Close()

	cycle := -1
	X := 1

	for scanner.Scan() {

		text := scanner.Text()
		instruction := strings.Split(text, " ")

		if instruction[0] == "noop" {
			cycle++
			printToConsole(cycle, X)
		} else {
			cycle++
			printToConsole(cycle, X)
			cycle++
			printToConsole(cycle, X)
			add, _ := strconv.Atoi(instruction[1])
			X += add

		}

	}

}
