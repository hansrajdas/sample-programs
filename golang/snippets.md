### Loop over slice
```go
for idx, n := range nums {
    ...
}
```

### Loop on range of numbers
```go
for i := 0; i < n; i++ {
    ...
}
```

### Declare 2d slice without size
```go
res := [][]int{{1}}
```

### Declare 2d slice with size
```go
m, n := len(s), len(t)
var dp [][]int

for i := 0; i < m + 1; i++ {
    dp = append(dp, make([]int, n + 1))
}

```
### Sort 2d slice w.r.t first element
```go
sort.Slice(mySlice, func(i, j int) bool {
    return mySlice[i][0] < mySlice[j][0]
})
```

### Recursive functions
```go
var F func(int, int) int

F = func(x, y int) int {
    ...
    v := F(a, b)
    ...
}
```

### Slice as stack
```go
stack = append(stack, c)  // Push

n := len(stack)
item = stack[n-1]  // Get top item
stack = stack[:n-1]  // Pop
```

### Implement stack
```go
type stack []int

func (s *stack) push(n int) {
    *s = append(*s, n)
}
func (s *stack) pop() int {
    val := (*s)[len(*s) - 1]
    *s = (*s)[:len(*s) - 1]
    return val
}
func (s *stack) top() int {
    return (*s)[len(*s) - 1]
}
func (s *stack) isEmpty() bool {
    return len(*s) == 0
}

// Usage
var s stack
if s.isEmpty() { ...}
s.pop()
s.push(9)
```
