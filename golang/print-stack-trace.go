package main

import (
	"fmt"
	"runtime"
)

func printStackTrace() {
	// Get the stack trace
	buf := make([]byte, 1<<16)

	// Set second arg to `true` for stacktrace of all goroutines.
	stackSize := runtime.Stack(buf, false)

	// Print the stack trace
	fmt.Println("=== BEGIN STACK TRACE ===")
	fmt.Println(string(buf[:stackSize]))
	fmt.Println("=== END STACK TRACE ===")
}

func main() {
	printStackTrace()
}
