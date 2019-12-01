package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var totalOne int = 0
	var totalTwo int = 0

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		mass, err := strconv.Atoi(scanner.Text())
		if err != nil {
			// Error in string conversion on a particular line
			panic(err)
		}
		totalOne += calculateFuel(mass)
		totalTwo += calculateRealFuel(mass)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
		panic(err)
	}

	fmt.Println("Part 1:", totalOne)
	fmt.Println("Part 2:", totalTwo)
}

func calculateFuel(mass int) int {
	fuel := (mass / 3) - 2
	if fuel >= 0 {
		return fuel
	}
	// Mass requiring negative fuel is handled by wishing hard
	return 0
}

func calculateRealFuel(mass int) int {
	fuel := (mass / 3) - 2
	if fuel >= 0 {
		return fuel + calculateRealFuel(fuel)
	}
	return 0
}
