package hello

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func Class5DS(args []string) {
	fmt.Println("Class 05 Arrays, Slices, Maps")

	p := map[string]int{}
	fmt.Println(p)

	a := p["the"]
	fmt.Println(a)

	b, ok := p["the"]
	fmt.Println("Was it present in map.. ", ok, b)

	p["the"]++

	if w, ok := p["the"]; ok {
		fmt.Println("Key present in map..", w)
	}

	var arr = [3]int{0, 0, 0}

	fmt.Println(arr)

	var a_slice = []int{1, 2}

	fmt.Println("Slice", a_slice)

	a_slice = append(a_slice, 3) // Here we assign a new backing arr for a_slice and then assign it back to a_slice
	fmt.Println("Slice .. append", a_slice)

	b_slice := a_slice

	b_slice[0] = 3

	fmt.Println(a_slice[0] == b_slice[0], "Value is=", b_slice[0])

	fmt.Println("//////////////////////////")

	t := []byte("string")

	fmt.Println(len(t), t)
	fmt.Println(t[2])
	fmt.Println(t[2:])

	fmt.Println("//////////////////////////")

	scan := bufio.NewScanner(os.Stdin)

	words := make(map[string]int)

	scan.Split(bufio.ScanWords)

	for scan.Scan() {
		words[scan.Text()] += 1
	}

	fmt.Println(len(words), "unique words..")

	type kv struct {
		key string
		val int
	}

	var kv_slice []kv

	for k, v := range words {
		kv_slice = append(kv_slice, kv{k, v})
	}

	sort.Slice(kv_slice, func(i, j int) bool {
		return kv_slice[i].val > kv_slice[j].val
	})

	for _, s := range kv_slice[:3] {
		fmt.Println(s.key, "appears", s.val, " # of times..")
	}

}
