package main

import (
    "fmt"
    "encoding/json"
)

type t struct {
    Value int
    Labels map[string]string
}

func main() {
    var s []t

    if s == nil {
        fmt.Println("Slice is empty")
    }
    s = append(s, t{})
    fmt.Println(s)
    b, err := json.Marshal(s)
    fmt.Println(b)
    fmt.Println(string(b))
    fmt.Println(err)
}
