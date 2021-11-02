### Golang difference with C language
- Golang only has one looping construct `for` which serves all purpose
- Golang switch case doesn't need break in each case, it executes only matching case. In C all cases after matching case gets executed if we don't break
- Golang doesn't support pointer arithematic as supported in C
- Methods with pointer receivers take either a value or a pointer as the receiver when they are called: https://tour.golang.org/methods/6
- methods with value receivers take either a value or a pointer as the receiver when they are called: https://tour.golang.org/methods/7

### Revisit [golang tour](https://tour.golang.org)
- Slices are like references to arrays
- Slice length and capacity
- Interfaces
  - https://tour.golang.org/methods/9
  - https://tour.golang.org/methods/10
  - ...
  - https://tour.golang.org/methods/14 - Empty interface, for holding any type of data
- Type switches: https://tour.golang.org/methods/16
- Stringers: https://tour.golang.org/methods/17 - this is like __str__ in python
- Errors: https://tour.golang.org/methods/19

### References
- https://tour.golang.org/welcome/1
- https://golang.org/doc/effective_go
