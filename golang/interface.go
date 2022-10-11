package main

import (
    "encoding/json"
    "fmt"
    "reflect"
)

type other struct {
    OtherValue interface{}
}

type s1 struct {
    V1 string
}

type s2 struct {
    V2 string
}

func myjson(data interface{}) {
    var b []byte
    if reflect.TypeOf(data).Kind() == reflect.String {
        b, _ = json.Marshal(&other{OtherValue: data})
    } else {
        b, _ = json.Marshal(data)
    }
    fmt.Println(string(b))
}

func main() {
    d1 := &s1{
        V1: "value1",
    }
    myjson(d1)

    d2 := &s2{
        V2: "value2",
    }
    myjson(d2)
    myjson("hello")
}
