package day5

import (
	"bufio"
	"github.com/anras5/AdventOfCode2022/helpers"
	"log"
	"os"
	"strconv"
	"strings"
	"unicode"
)

func inputParser(filename string) ([]helpers.Stack[string], error) {
	file, _ := os.Open(filename)
	scanner := bufio.NewScanner(file)

	var numberOfStacks int
	var stacks []helpers.Stack[string]

	for scanner.Scan() {

		text := scanner.Text()
		if unicode.IsNumber(rune(text[1])) {
			numberOfStacks, _ = strconv.Atoi(string(text[len(text)-1]))
			break
		}
	}
	err := file.Close()
	if err != nil {
		return nil, err
	}

	for i := 0; i < numberOfStacks; i++ {
		stacks = append(stacks, helpers.NewStack[string]())
	}

	file, _ = os.Open(filename)
	scanner = bufio.NewScanner(file)
	for scanner.Scan() {
		// get text from scanner
		text := scanner.Text()
		textLength := len(text)

		// break after input statement
		if unicode.IsNumber(rune(text[1])) {
			break
		}

		// push values to stacks
		j := 0
		for i := 0; i+3 <= textLength; i += 4 {
			croppedText := text[i+1 : i+2]
			if croppedText != " " {
				stacks[j].Push(croppedText)
			}
			j++
		}

	}
	for _, stack := range stacks {
		stack.Reverse()
	}
	err = file.Close()
	if err != nil {
		return nil, err
	}
	return stacks, nil
}

func commandsParser(filename string) [][]int {
	file, _ := os.Open(filename)
	scanner := bufio.NewScanner(file)
	defer file.Close()

	isCommand := false
	var commands [][]int

	for scanner.Scan() {
		if isCommand {
			command := strings.Split(scanner.Text(), " ")
			move, _ := strconv.Atoi(command[1])
			from, _ := strconv.Atoi(command[3])
			to, _ := strconv.Atoi(command[5])
			commands = append(commands, []int{move, from, to})
		}

		if scanner.Text() == "" {
			isCommand = true
		}
	}

	return commands
}

func Zad5() []string {

	stacks, err := inputParser("day5/data5.txt")
	if err != nil {
		log.Fatal(err)
	}
	//fmt.Println("Input stacks:")
	//fmt.Println(stacks)

	commands := commandsParser("day5/data5.txt")
	//fmt.Println("Input commands:")
	//fmt.Println(commands)

	for _, command := range commands {
		howMany := command[0]
		from := command[1]
		to := command[2]
		for i := 0; i < howMany; i++ {
			temp := stacks[from-1].Pop()
			stacks[to-1].Push(temp)
		}
	}

	//fmt.Println("Output stacks:")
	//fmt.Println(stacks)

	// get last items
	var output []string
	for _, stack := range stacks {
		output = append(output, stack.Pop())
	}

	return output
}

func Zad5b() []string {
	stacks, err := inputParser("day5/data5.txt")
	if err != nil {
		log.Fatal(err)
	}

	commands := commandsParser("day5/data5.txt")

	for _, command := range commands {
		howMany := command[0]
		from := command[1]
		to := command[2]
		var temp []string
		for i := 0; i < howMany; i++ {
			temp = append(temp, stacks[from-1].Pop())
		}
		for i := len(temp) - 1; i >= 0; i-- {
			stacks[to-1].Push(temp[i])
		}

	}

	//fmt.Println("Output stacks:")
	//fmt.Println(stacks)

	// get last items
	var output []string
	for _, stack := range stacks {
		output = append(output, stack.Pop())
	}

	return output
}
