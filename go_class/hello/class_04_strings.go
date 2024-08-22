package hello

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func Class4Strings(args []string) {
	fmt.Println("Starting Go Class: 04 Strings...")

	old_s, new_s := os.Args[2], os.Args[3]
	scan := bufio.NewScanner(os.Stdin)

	for scan.Scan() {
		s := strings.Split(scan.Text(), old_s)
		t := strings.Join(s, new_s)
		fmt.Println(t)
	}

}
