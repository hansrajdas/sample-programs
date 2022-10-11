/*
 * Date: 2022-10-11
 *
 * Description:
 * Demo program to show concurrency and synchronization in golang using go channels.
 *
 * Reference:
 * https://www.josephbuiteweg.com/blog/ping-pong-concurrency/
 */

package main

import (
    "fmt"
    "sync"
)

func pingPong() {
    numTimes := 5
    var wg sync.WaitGroup
    theChannel := make(chan string)

    wg.Add(2)
    go func(n int) {
        defer wg.Done()
        for i := 0; i < n; i++ {
            fmt.Println(<-theChannel)
            theChannel <- "pong"
        }
    }(numTimes)

    go func(n int) {
        defer wg.Done()
        for i := 0; i < n; i++ {
            theChannel <- "ping"
            fmt.Println(<-theChannel)
        }
    }(numTimes)

    wg.Wait()
}

func main() {
    pingPong()
}
