package day8

import (
	"bufio"
	"log"
	"os"
	"strconv"
)

func stringToSlice(str string) []int {
	var result []int
	for _, character := range str {
		number, err := strconv.Atoi(string(character))
		if err != nil {
			log.Fatal(err)
		}
		result = append(result, number)
	}
	return result
}

func inputParser(filename string) [][]int {
	file, _ := os.Open(filename)
	scanner := bufio.NewScanner(file)
	defer file.Close()

	var result [][]int

	for scanner.Scan() {
		text := scanner.Text()
		result = append(result, stringToSlice(text))
	}
	return result
}

func Zad8() int {
	data := inputParser("day8/data8.txt")

	counter := 0

	for i := 0; i < len(data); i++ {
		for j := 0; j < len(data[i]); j++ {
			if i == 0 || i == len(data)-1 || j == 0 || j == len(data[i])-1 {
				counter++
				continue
			} else {
				// check column top
				isTopOk := true
				for z := 0; z < i; z++ {
					if data[z][j] >= data[i][j] {
						isTopOk = false
						break
					}
				}
				// check column bottom
				isBottomOk := true
				for z := i + 1; z < len(data); z++ {
					if data[z][j] >= data[i][j] {
						isBottomOk = false
						break
					}
				}
				// check row left
				isLeftOk := true
				for z := 0; z < j; z++ {
					if data[i][z] >= data[i][j] {
						isLeftOk = false
						break
					}
				}
				// check row right
				isRightOk := true
				for z := j + 1; z < len(data[i]); z++ {
					if data[i][z] >= data[i][j] {
						isRightOk = false
						break
					}
				}
				// check if visible
				if isTopOk || isBottomOk || isLeftOk || isRightOk {
					counter++
				}
			}
		}
	}
	return counter

}

func Zad8b() int {
	data := inputParser("day8/data8.txt")

	maxScore := 0

	for i := 0; i < len(data); i++ {
		for j := 0; j < len(data[i]); j++ {
			score := 0
			if i == 0 || i == len(data)-1 || j == 0 || j == len(data[i])-1 {
				score = 0
			} else {
				// check column top
				distanceTop := 0
				for index, z := 1, i-1; z >= 0; index, z = index+1, z-1 {
					if data[z][j] >= data[i][j] {
						distanceTop = index
						break
					}
					if z == 0 {
						distanceTop = index
					}
				}
				// check column bottom
				distanceBottom := 0
				for index, z := 1, i+1; z < len(data); index, z = index+1, z+1 {
					if data[z][j] >= data[i][j] {
						distanceBottom = index
						break
					}
					if z == len(data)-1 {
						distanceBottom = index
					}
				}
				// check row left
				distanceLeft := 0
				for index, z := 1, j-1; z >= 0; index, z = index+1, z-1 {
					if data[i][z] >= data[i][j] {
						distanceLeft = index
						break
					}
					if z == 0 {
						distanceLeft = index
					}
				}
				// check row right
				distanceRight := 0
				for index, z := 1, j+1; z < len(data[i]); index, z = index+1, z+1 {
					if data[i][z] >= data[i][j] {
						distanceRight = index
						break
					}
					if z == len(data[i])-1 {
						distanceRight = index
					}
				}
				// calculate score
				score = distanceTop * distanceBottom * distanceLeft * distanceRight
				//fmt.Println(data[i][j], distanceTop, distanceBottom, distanceLeft, distanceRight)
			}
			if maxScore < score {
				maxScore = score
			}
		}
	}
	return maxScore
}
