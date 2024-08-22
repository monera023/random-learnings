package main

import (
	"fmt"
	"hello/hello"
	"os"
	"strings"
)

func main() {
	// fmt.Println(hello.Say(os.Args[1:]))
	// a := 2
	// b := 2.1

	// fmt.Printf("a: %T %[1]v\n", a)
	// fmt.Printf("b: %T %v\n", b, b)

	// a = int(b)
	// fmt.Printf("a: %T %[1]v\n", a)
	// var sum float64
	// var total_n int

	// for {
	// 	var val float64
	// 	_, err := fmt.Fscanln(os.Stdin, &val)
	// 	if err != nil {
	// 		break
	// 	}
	// 	sum += val
	// 	total_n += 1
	// }

	// if total_n == 0 {
	// 	fmt.Fprintln(os.Stderr, "no values")
	// 	os.Exit(-1)
	// }

	// fmt.Println("The average is: ", sum/float64(total_n))

	temp := "élite"
	fmt.Printf("temp: %T %v %v\n", temp, len(temp), temp)

	old := "a string"
	old = strings.ToUpper(old)
	fmt.Println("Old value::", old)

	if os.Args[1] == "class_04_strings" {
		hello.Class4Strings(os.Args)
	}

	if os.Args[1] == "class_05_ds" {
		hello.Class5DS(os.Args)
	}

}
