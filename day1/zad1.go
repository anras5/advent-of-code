package day1

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func Zad1() {

	file, err := os.Open("day1/data1.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	max := 0
	sum := 0

	for scanner.Scan() {
		line := scanner.Text()
		if line != "" {
			integer, _ := strconv.Atoi(line)
			sum = sum + integer
		} else {
			if sum > max {
				max = sum
			}
			sum = 0
		}
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	fmt.Println(max)

}
