package day9

import (
	"bufio"
	"math"
	"os"
	"strconv"
	"strings"
)

type Marker struct {
	x int
	y int
}

func Zad9() int {

	file, _ := os.Open("day9/data9.txt")
	scanner := bufio.NewScanner(file)
	defer file.Close()

	head := Marker{}
	tail := Marker{}

	locations := make(map[[2]int]bool)

	for scanner.Scan() {

		instructions := strings.Split(scanner.Text(), " ")
		way := instructions[0]
		number, _ := strconv.Atoi(instructions[1])

		for i := 0; i < number; i++ {
			// move head
			switch way {
			case "R":
				head.x++
			case "L":
				head.x--
			case "U":
				head.y++
			case "D":
				head.y--
			}

			// move tail
			if math.Abs(float64(head.x-tail.x)) > 1 || math.Abs(float64(head.y-tail.y)) > 1 {
				if head.x == tail.x {
					tail.y = (tail.y + head.y) / 2
				} else if head.y == tail.y {
					tail.x = (tail.x + head.x) / 2
				} else {
					if head.x > tail.x {
						tail.x++
					} else {
						tail.x--
					}
					if head.y > tail.y {
						tail.y++
					} else {
						tail.y--
					}
				}
			}

			// remember tail location

			locations[[2]int{tail.x, tail.y}] = true

			//fmt.Println("HEAD: ", head)
			//fmt.Println("TAIL: ", tail)
		}
	}
	// return number of positions
	return len(locations)
}

func Zad9b() int {
	file, _ := os.Open("day9/data9.txt")
	scanner := bufio.NewScanner(file)
	defer file.Close()

	snake := make([]Marker, 10)

	locations := make(map[[2]int]bool)

	for scanner.Scan() {

		instructions := strings.Split(scanner.Text(), " ")
		way := instructions[0]
		number, _ := strconv.Atoi(instructions[1])

		for i := 0; i < number; i++ {
			// move head
			switch way {
			case "R":
				snake[0].x++
			case "L":
				snake[0].x--
			case "U":
				snake[0].y++
			case "D":
				snake[0].y--
			}

			// move tail
			for j := 1; j < len(snake); j++ {
				if math.Abs(float64(snake[j-1].x-snake[j].x)) > 1 || math.Abs(float64(snake[j-1].y-snake[j].y)) > 1 {
					if snake[j-1].x == snake[j].x {
						snake[j].y = (snake[j].y + snake[j-1].y) / 2
					} else if snake[j-1].y == snake[j].y {
						snake[j].x = (snake[j].x + snake[j-1].x) / 2
					} else {
						if snake[j-1].x > snake[j].x {
							snake[j].x++
						} else {
							snake[j].x--
						}
						if snake[j-1].y > snake[j].y {
							snake[j].y++
						} else {
							snake[j].y--
						}
					}
				}
			}

			// remember tail location

			locations[[2]int{snake[len(snake)-1].x, snake[len(snake)-1].y}] = true

			//fmt.Println("HEAD: ", head)
			//fmt.Println("TAIL: ", tail)
		}
	}
	// return number of positions
	return len(locations)
}
