/*
Dial starts at fifty, and input is series of rotations, i.e.:
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
If rotated past 99 or below 0, number should wrap around. With sample input, dial points at 0 three times.
Part 1: Need to decode password based on how many times a dial is left pointing at 0 after a turn.
Part 2: Actually, password should also include any times the dial *crossed* 0.
*/
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
	pass1, err := part1(string(stdin))
	if err != nil {
		fmt.Println("Part1 failed")
		os.Exit(1)
	}
	fmt.Printf("Password with ending on 0: %v\n", pass1)
	pass2, err := part2(string(stdin))
	if err != nil {
		fmt.Println("Part2 failed")
		os.Exit(2)
	}
	fmt.Printf("Password with crossing 0: %v\n", pass2)
}

func part1(rotations string) (int, error) {
	dial := 50
	passCount := 0
	for rotation := range strings.SplitSeq(rotations, "\n") {
		if len(rotation) < 2 || len(rotation) == 0 {
			continue
		}
		rotateDir := rotation[0]
		rotateDistance, err := strconv.Atoi(rotation[1:])
		if err != nil {
			return 0, err
		}
		if rotateDir == 'L' {
			dial -= rotateDistance
		}
		if rotateDir == 'R' {
			dial += rotateDistance
		}
		dial = dial % 100
		if dial < 0 {
			dial += 100
		}
		if dial == 0 {
			passCount += 1
		}
		// fmt.Printf("Dial: %v, Count: %v\n", dial, passCount)
	}
	return passCount, nil
}

func part2(rotations string) (int, error) {
	dial := 50
	passCount := 0
	for rotation := range strings.SplitSeq(rotations, "\n") {
		prevDial := dial
		if len(rotation) < 2 || len(rotation) == 0 {
			continue
		}
		rotateDir := rotation[0]
		rotateDistance, err := strconv.Atoi(rotation[1:])
		if err != nil {
			return 0, err
		}
		if rotateDir == 'L' {
			dial -= rotateDistance
		}
		if rotateDir == 'R' {
			dial += rotateDistance
		}
		if dial == 0 {
			passCount += 1
		} else if dial > 0 {
			passCount += dial / 100
		} else {
			passCount += -dial / 100
			if prevDial != 0 {
				passCount += 1
			}
		}
		dial = dial % 100
		if dial < 0 {
			dial += 100
		}
		// fmt.Printf("Dial: %v, prevDial: %v, Count: %v\n", dial, prevDial, passCount)
	}
	return passCount, nil
}
