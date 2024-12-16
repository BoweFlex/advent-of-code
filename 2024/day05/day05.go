/*
Input has two sections:
- Order for pages to be printed, if number on left and number on right appear in update then the number on left must appear first
  - i.e. `47|53`

- Page numbers included in an update (line = update).
  - i.e. `75,47,61,53,29`

Part 1: Start by identifying which updates are in the right order (all pages appear before any pages that depend on them).

	What is the sum of each middle number from valid updates?

Part 2: Taking only invalid updates, reorder them so that the pages are in the correct order.

	What is the sum of each middle number from these updates?
*/
package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
	"sync"
)

var wg sync.WaitGroup
var updates [][]int
var invalidUpdates [][]int
var dependencies = make(map[int][]int)

func processInput(input *os.File) {
	scanner := bufio.NewScanner(input)
	for scanner.Scan() {
		text := scanner.Text()
		if strings.Contains(text, "|") {
			nums := strings.Split(text, "|")
			first, _ := strconv.Atoi(nums[0])
			second, _ := strconv.Atoi(nums[1])
			dependencies[first] = append(dependencies[first], second)
		} else if strings.Contains(text, ",") {
			nums := strings.Split(text, ",")
			update := []int{}
			for _, num := range nums {
				i, _ := strconv.Atoi(num)
				update = append(update, i)
			}
			updates = append(updates, update)
		}
	}
}

func Part1() {
	fmt.Println("**** STARTING PART 1 ****")
	var middlePageSum int
	for _, update := range updates {
		valid := true
		for i, page := range update {
			if !valid {
				break
			}
			deps, ok := dependencies[page]
			if !ok {
				// No dependencies exist, page is fine
				continue
			}
			for j := 0; j < i; j++ {
				if slices.Contains(deps, update[j]) {
					// Page is invalid if a previous page depends on it
					valid = false
					break
				}
			}
		}
		if valid {
			middlePageSum += update[len(update)/2]
		} else {
			invalidUpdates = append(invalidUpdates, update)
		}
	}
	fmt.Printf("> Sum of middle pages in valid updates: %v\n", middlePageSum)
}

func Part2() {
	fmt.Println("**** STARTING PART 2 ****")
	var middlePageSum int
	for _, update := range invalidUpdates {
		var newUpdate []int
		for _, page := range update {
			newUpdate = append(newUpdate, page)
			deps, ok := dependencies[page]
			if !ok {
				continue
			}
			for j := 0; j < slices.Index(newUpdate, page); j++ {
				if slices.Contains(deps, newUpdate[j]) {
					depPage := newUpdate[j]
					newUpdate = append(newUpdate[:j], newUpdate[j+1:]...)
					newUpdate = append(newUpdate, depPage)
					j--
				}
			}
		}
		middlePageSum += newUpdate[len(newUpdate)/2]
	}

	fmt.Printf("> Sum of middle pages in invalid updates: %v\n", middlePageSum)
}

func main() {
	processInput(os.Stdin)
	Part1()
	Part2()
}
