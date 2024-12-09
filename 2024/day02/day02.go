/*
Analyzing "unusual data" from reactor report, each line of input is one report.
Each report is a list of levels, each separated by spaces.
Checking if reports are "safe", defined by:
- levels are either all increasing or all decreasing
- any two adjacent levels differ by at least 1 and at most 3

Part 1: How many reports are safe?
Part 2: Of any unsafe levels, one can be removed from each unsafe report.
How many reports are safe now?
*/
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func processInput(input *os.File) [][]int {
	var reports [][]int
	scanner := bufio.NewScanner(input)
	for scanner.Scan() {
		report := []int{}
		text := scanner.Text()
		levels := strings.Split(text, " ")
		for _, level := range levels {
			level_int, _ := strconv.Atoi(level)
			report = append(report, level_int)
		}
		reports = append(reports, report)
	}
	return reports
}

func isReportSafe(report []int) bool {
	var safe bool
	var increasing bool
	if report[0] == report[len(report)-1] {
		return false
	}

	increasing = report[0] < report[len(report)-1]
	for i := 1; i < len(report); i++ {
		difference := (report[i] - report[i-1])
		if increasing {
			safe = (difference > 0 && difference <= 3)
		} else {
			safe = (difference < 0 && difference >= -3)
		}
		if !safe {
			break
		}
	}
	return safe
}

func generatePermutations(report []int) (potential_reports [][]int) {
	for i := range report {
		permutation := make([]int, len(report)-1)
		copy(permutation[:i], report[:i])
		copy(permutation[i:], report[i+1:])
		potential_reports = append(potential_reports, permutation)
	}
	return
}

func Part1(reports [][]int) {
	fmt.Println("**** STARTING PART 1 ****")
	var safe_reports int
	for _, report := range reports {
		if isReportSafe(report) {
			safe_reports++
		}
	}
	fmt.Printf("> Number of safe reports: %v\n", safe_reports)
}

func Part2(reports [][]int) {
	fmt.Println("**** STARTING PART 2 ****")
	var safe_reports int
	for _, report := range reports {
		if isReportSafe(report) {
			safe_reports++
		} else {
			permutated_reports := generatePermutations(report)
			for _, permutation := range permutated_reports {
				if isReportSafe(permutation) {
					safe_reports++
					break
				}
			}
		}
	}
	fmt.Printf("> Number of safe reports: %v\n", safe_reports)
}

func main() {
	var reports [][]int
	reports = processInput(os.Stdin)
	Part1(reports)
	Part2(reports)
}
