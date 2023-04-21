package main

/*
 * Date: 2023-04-21
 *
 * Description:
 * Implement Set in golang.
 */

type void struct{}

func main() {
    // Set to hold string values. This void (struct{}) won't take
    // any space, if we have bool as payload, it will use one bit.
    set := make(map[string]void)
    var nullValue void

    set["string-1"] = nullValue
    set["string-2"] = nullValue
    set["string-3"] = nullValue
    // ...
}
