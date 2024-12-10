/*
Input is memory for shop computer, but memory is corrupted.
Memory is intended to multiply given values, in the format "mul(X,Y)".
X and Y will always be between 1 and 3 digits.
Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

Part 1: Find any real multiplication commands, complete the multiplication,
and sum all of the products. What is the total of all the multiplication results?
*/
package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"sync"
)

var wg sync.WaitGroup

func processInput(input *os.File) (commandsList [][][]string) {
	r := regexp.MustCompile(`mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)`)
	scanner := bufio.NewScanner(input)
	for scanner.Scan() {
		text := scanner.Text()
		commands := r.FindAllStringSubmatch(text, -1)
		commandsList = append(commandsList, commands)
	}
	return
}

func Part1(commandsList [][][]string) {
	var productSum int
	productChannel := make(chan int)
	fmt.Println("**** STARTING PART 1 ****")
	for _, commands := range commandsList {
		for _, command := range commands {
			if command[0][0:3] != "mul" {
				continue
			}
			wg.Add(1)
			go func(c chan<- int) {
				val1, _ := strconv.Atoi(command[1])
				val2, _ := strconv.Atoi(command[2])
				c <- val1 * val2
				wg.Done()
			}(productChannel)
			productSum = productSum + <-productChannel
		}
	}
	fmt.Printf("> Total of multiplication results: %v\n", productSum)
}

func Part2(commandsList [][][]string) {
	var productSum int
	processing := true
	productChannel := make(chan int)
	fmt.Println("**** STARTING PART 2 ****")
	for _, commands := range commandsList {
		for _, command := range commands {
			if command[0][0:3] != "mul" {
				processing = command[0][0:2] == "do" && command[0][0:3] != "don"
				continue
			}
			if !processing {
				continue
			}
			wg.Add(1)
			go func(c chan<- int) {
				val1, _ := strconv.Atoi(command[1])
				val2, _ := strconv.Atoi(command[2])
				c <- val1 * val2
				wg.Done()
			}(productChannel)
			productSum = productSum + <-productChannel
		}
	}
	fmt.Printf("> Total of multiplication results: %v\n", productSum)
}

func main() {
	commandsList := processInput(os.Stdin)
	Part1(commandsList)
	Part2(commandsList)
}
