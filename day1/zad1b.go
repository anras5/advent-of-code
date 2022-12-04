package day1

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
)

func Zad1b() {

	file, err := os.Open("day1/data1.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	var sums []int
	sum := 0

	for scanner.Scan() {
		line := scanner.Text()
		if line != "" {
			integer, _ := strconv.Atoi(line)
			sum = sum + integer
		} else {
			sums = append(sums, sum)
			sum = 0
		}
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	sort.Slice(sums, func(i, j int) bool {
		return sums[i] > sums[j]
	})
	fmt.Println(sums[0] + sums[1] + sums[2])

}
