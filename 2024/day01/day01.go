/*
Looking for list of locations that Chief Historian is visiting.
Two lists of location IDs were created, but don't line up (input).
- Pull input into two separate lists
- Sort each list from smallest to largest
- Find difference between equal indexes in order (list1[0] - list2[0], etc)
- Sum differences for total difference between lists

Part 1: What is the total distance between your lists?
Part 2: What is the similarity score between the two lists?
	Calculate by:
	- Counting number of times each value in list 1 appears in list 2
	- Multiply value from list 1 by count from list 2
*/
package main

import (
	"bufio"
	"os"
	"fmt"
	"strconv"
	"strings"
	"sort"
	"slices"
)

type location_ids []int

func ProcessInput(input *os.File) (location_ids, location_ids) {
	scanner := bufio.NewScanner(input)
	var list1 location_ids
	var list2 location_ids
	for scanner.Scan() {
		text := scanner.Text()
		locations := strings.Split(text, "   ")
		if location_id, err := strconv.Atoi(locations[0]); err == nil {
			list1 = append(list1, location_id)
		}
		if location_id, err := strconv.Atoi(locations[1]); err == nil {
			list2 = append(list2, location_id)
		}

	}
	return list1, list2
}

func Part1(lists ...location_ids) {
	fmt.Println("**** STARTING PART 1 ****")
	for _, list := range lists {
		sort.Ints(list)
	}
	total_difference := 0
	var difference int
	for i, v := range lists[0] {
		v2 := lists[1][i]
		if v > v2 {
			difference = v - v2
		} else if v < v2 {
			difference = v2 - v
		} else {
			difference = 0
		}
		fmt.Printf("> Difference between %v and %v: %v\n", v, v2, difference)
		total_difference += difference
		fmt.Println(total_difference)
	}
	fmt.Printf("> Difference between location lists: %v\n", total_difference)
}

func Part2(lists ...location_ids) {
	fmt.Println("**** STARTING PART 2 ****")
	value_counts := make(map[int]int)
	var similarity_score int
	for _, v := range lists[1] {
		if slices.Contains(lists[0], v) {
			value_counts[v]++
		}
	}
	for _, v := range lists[0] {
		if count, ok := value_counts[v]; ok {
			similarity_score += v * count
		}
	}
	fmt.Printf("> Similarity between location lists: %v\n", similarity_score)
}

func main() {
	list1, list2 := ProcessInput(os.Stdin)
	Part1(list1, list2)
	Part2(list1, list2)
}
