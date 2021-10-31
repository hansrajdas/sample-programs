### Golang difference with C language
- Golang only has one looping construct `for` which serves all purpose
- Golang switch case doesn't need break in each case, it executes only matching case. In C all cases after matching case gets executed if we don't break
- Golang doesn't support pointer arithematic as supported in C
- Methods with pointer receivers take either a value or a pointer as the receiver when they are called: https://tour.golang.org/methods/6

### Revisit [golang tour]
- Slices are like references to arrays
- Slice length and capacity

### References
- https://tour.golang.org/welcome/1
- https://golang.org/doc/effective_go
