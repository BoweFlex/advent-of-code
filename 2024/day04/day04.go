/*
Input is word search, looking for the word 'XMAS'. Word can occur horizontally,
vertically, diagonally, backwards, or overlapping other words. Must find all occurences.

Part 1: How many times does XMAS occur in the input?
Part 2: The word search is actually looking for two "MAS" in the shape of X, i.e.
M.S
.A.
M.S
How many times do these X-MAS appear?
*/
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	// "sync"
)

// var wg sync.WaitGroup
var wordSearch [][]string

func processInput(input *os.File) {
	scanner := bufio.NewScanner(input)
	for scanner.Scan() {
		wordSearch = append(wordSearch, strings.Split(scanner.Text(), ""))
	}
}

func checkDirection(y, x int, direction []int) (letter string) {
	newY := y + direction[0]
	newX := x + direction[1]
	if newY < len(wordSearch) && newY >= 0 && newX >= 0 && newX < len(wordSearch[0]) {
		return wordSearch[newY][newX]
	} else {
		return "."
	}
}

func Part1() {
	fmt.Println("**** STARTING PART 1 ****")
	var validWords int
	directions := [][][3]int{
		{{1, 0}, {2, 0}, {3, 0}},
		{{-1, 0}, {-2, 0}, {-3, 0}},
		{{0, 1}, {0, 2}, {0, 3}},
		{{0, -1}, {0, -2}, {0, -3}},
		{{1, 1}, {2, 2}, {3, 3}},
		{{-1, -1}, {-2, -2}, {-3, -3}},
		{{1, -1}, {2, -2}, {3, -3}},
		{{-1, 1}, {-2, 2}, {-3, 3}},
	}
	for y := range wordSearch {
		for x := range wordSearch[y] {
			currLetter := wordSearch[y][x]
			if currLetter != "X" {
				continue
			}
			for _, direction := range directions {
				if y+direction[2][0] >= len(wordSearch) || y+direction[2][0] < 0 || x+direction[2][1] >= len(wordSearch[y]) || x+direction[2][1] < 0 {
					continue
				}
				word := currLetter + wordSearch[y+direction[0][0]][x+direction[0][1]] + wordSearch[y+direction[1][0]][x+direction[1][1]] + wordSearch[y+direction[2][0]][x+direction[2][1]]
				if word == "XMAS" {
					validWords++
				}
			}
		}
	}
	fmt.Printf("> Number of 'XMAS' found: %v\n", validWords)
}

func Part2() {
	fmt.Println("**** STARTING PART 2 ****")
	var validX int
	for y := range wordSearch {
		for x := range wordSearch[y] {
			currLetter := wordSearch[y][x]
			if currLetter != "A" {
				continue
			} else if y-1 < 0 || y+1 >= len(wordSearch) || x-1 < 0 || x+1 >= len(wordSearch[y]) {
				continue
			}

			descLeft := wordSearch[y-1][x+1] + currLetter + wordSearch[y+1][x-1]
			descRight := wordSearch[y-1][x-1] + currLetter + wordSearch[y+1][x+1]
			if descLeft != "MAS" && descLeft != "SAM" || descRight != "MAS" && descRight != "SAM" {
				continue
			} else {
				validX++
			}

		}
	}
	fmt.Printf("> Number of 'X-MAS' found: %v\n", validX)
}

func main() {
	processInput(os.Stdin)
	Part1()
	Part2()
}
