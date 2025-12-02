// The ranges are separated by commas (,); each range gives its first ID and last ID separated by a dash (-).
// Since the young Elf was just doing silly patterns, you can find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice. So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.
// None of the numbers have leading zeroes; 0101 isn't an ID at all. (101 is a valid ID that you would ignore.)
// Part 1: What do you get if you add up all of the invalid IDs?
// Part 2: There are actually more invalid IDs - anything that repeats *at least* twice. What is the sum of all the (now) invalid IDs?

package main

import (
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func main() {
	stdin, err := io.ReadAll(os.Stdin)
	if err != nil {
		fmt.Println("Failed to read stdin")
		os.Exit(3)
	}
	ids1, err := part1(string(stdin))
	if err != nil {
		fmt.Println("Part1 failed")
		os.Exit(1)
	}
	fmt.Printf("Invalid IDs: %v\n", ids1)
	ids2, err := part2(string(stdin))
	if err != nil {
		fmt.Println("Part2 failed")
		os.Exit(2)
	}
	fmt.Printf("Even more invalid IDs: %v\n", ids2)
}

func part1(ranges string) (int, error) {
	invalidSum := 0
	for r := range strings.SplitSeq(ranges, ",") {
		trimmed := strings.Trim(r, "\n\r ")
		idEnds := strings.Split(trimmed, "-")
		start, err := strconv.Atoi(idEnds[0])
		if err != nil {
			return 0, err
		}
		end, err := strconv.Atoi(idEnds[1])
		if err != nil {
			return 0, err
		}
		for id := start; id <= end; id++ {
			idStr := fmt.Sprintf("%d", id)
			if idStr[0:len(idStr)/2] == idStr[len(idStr)/2:] {
				invalidSum += id
			}
		}
	}
	return invalidSum, nil
}

func part2(ranges string) (int, error) {
	invalidSum := 0
	for r := range strings.SplitSeq(ranges, ",") {
		trimmed := strings.Trim(r, "\n\r ")
		idEnds := strings.Split(trimmed, "-")
		start, err := strconv.Atoi(idEnds[0])
		if err != nil {
			return 0, err
		}
		end, err := strconv.Atoi(idEnds[1])
		if err != nil {
			return 0, err
		}
		for id := start; id <= end; id++ {
			idStr := fmt.Sprintf("%d", id)
			search := fmt.Sprintf("%d%d", id, id)
			if strings.Count(search[1:len(search)-1], idStr) >= 1 {
				invalidSum += id
			}
		}
	}
	return invalidSum, nil
}
