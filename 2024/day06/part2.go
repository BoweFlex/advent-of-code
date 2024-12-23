/*
Input is map with '#' for obstacles and '^' for starting location of guard (facing up).
Guard will move in the direction where they are facing until they hit an obstacle,
then turn 90 degrees to the right, then move forward again, then continue this pattern
until leaving the map.

Part 1: How many distinct positions will the guard visit before leaving the map?
*/
package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strings"
)

type guard struct {
	position position
	direction direction
}

type position struct {
	y, x int
}

type direction struct {
	yDir, xDir int
}

func (d direction) turn() direction {
	/* Valid directions:
		- North: [-1, 0]
		- East: [0, 1]
		- South: [1, 0]
		- West: [0, -1]
	*/
	if d.yDir == 0 {
		return direction{d.xDir, 0}
	}
	return direction{0, d.yDir * -1}
}

func main() {
	fmt.Println("**** Finding number of potential loops to trap guard ****")
	var guardMap [][]string
	var guard = guard{position{0,0},direction{-1,0}}

	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		row := strings.Split(scanner.Text(), "")
		guardMap = append(guardMap, row)
		guardIndex := slices.Index(row, "^")

		if guardIndex > -1 {
			guard.position.y = len(guardMap)-1
			guard.position.x = guardIndex
		}
	}

	var loops int
	for y := 0; y < len(guardMap); y++ {
		for x := 0; x < len(guardMap[y]); x++ {
			if guardMap[y][x] == "." {
				guardMap[y][x] = "#"
				if detectLoop(guardMap, guard) {
					loops++
				}
				guardMap[y][x] = "."
			}
		}
	}

	fmt.Printf("> Result: %v\n", loops)
}

func detectLoop(guardMap [][]string, guard guard) bool {
	positionsVisited := make(map[string]bool)
	
	for {
		coords := fmt.Sprintf("%v, %v", guard.position, guard.direction)
		if visited, ok := positionsVisited[coords]; ok && visited {
			return true
		}

		positionsVisited[coords] = true

		var nextPosition = position{guard.position.y + guard.direction.yDir, guard.position.x + guard.direction.xDir}
		if nextPosition.y >= len(guardMap) || nextPosition.y < 0 || nextPosition.x >= len(guardMap[0]) || nextPosition.x < 0 {
			return false
		}

		if guardMap[nextPosition.y][nextPosition.x] == "#" {
			guard.direction = guard.direction.turn()
			continue
		}
		guard.position = nextPosition
	}
}
