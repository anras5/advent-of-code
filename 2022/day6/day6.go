package day6

import (
	"io/ioutil"
	"log"
)

// doLetterRepeat checks if any letter in a string repeats
func doLettersRepeat(text string) bool {

	seenLetters := make(map[rune]bool)
	for _, letter := range text {
		if seenLetters[letter] {
			return true
		}
		seenLetters[letter] = true
	}
	return false
}

func Zad6() int {
	data, err := ioutil.ReadFile("day6/data6.txt")
	if err != nil {
		log.Fatal(err)
	}
	text := string(data)

	characterNumber := 0

	for i := 0; i < len(text)-4; i++ {
		marker := text[i : i+4]
		if !doLettersRepeat(marker) {
			characterNumber = i + 4
			break
		}
	}

	return characterNumber
}

func Zad6b() int {
	data, err := ioutil.ReadFile("day6/data6.txt")
	if err != nil {
		log.Fatal(err)
	}
	text := string(data)

	characterNumber := 0

	for i := 0; i < len(text)-14; i++ {
		marker := text[i : i+14]
		if !doLettersRepeat(marker) {
			characterNumber = i + 14
			break
		}
	}

	return characterNumber
}
