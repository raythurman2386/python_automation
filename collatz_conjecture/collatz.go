package main

import (
	"fmt"
)

func collatz(n uint64) []uint64 {
	if n <= 0 {
		panic(fmt.Sprintf("Please input a value greater than 0! You input %d", n))
	}

	sequence := []uint64{n}

	for n != 1 {
		if n%2 == 0 {
			n /= 2
		} else {
			n = 3*n + 1
		}
		sequence = append(sequence, n)
	}

	return sequence
}

func main() {
	n := uint64(6)
	result := collatz(n)
	fmt.Printf("Collatz sequence for %d: %v\n", n, result)
}
