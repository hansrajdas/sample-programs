## Golang difference with C language
- Golang only has one looping construct `for` which serves all purpose
- Golang switch case doesn't need break in each case, it executes only matching case. In C all cases after matching case gets executed if we don't break
- Golang doesn't support pointer arithematic as supported in C
- Using struct pointers, golang permits accessing members using dot `p.x` or `(*p).x` and in C arrow notation is used access members `p->x`
- Methods with pointer receivers take either a value or a pointer as the receiver when they are called: https://tour.golang.org/methods/6
- Methods with value receivers take either a value or a pointer as the receiver when they are called: https://tour.golang.org/methods/7

## Golang tour
- https://tour.golang.org
- Important points
  - Slices are like references to arrays
  - Slice length and capacity
  - Interfaces
    - https://tour.golang.org/methods/9
    - https://tour.golang.org/methods/10
    - ...
    - Empty interface, for holding any type of data: https://tour.golang.org/methods/14
  - Type switches: https://tour.golang.org/methods/16
  - Stringers(this is like __str__ in python): https://tour.golang.org/methods/17
  - Errors: https://tour.golang.org/methods/19
  - Channels
    - Channels are thread-safe and using channels is the official way of communicating b/w goroutines
    - Secondaly, channels are unbuffered meaning both producers and consumers block until a value is put into or removed from the channel, respectively
    - https://tour.golang.org/concurrency/2
    - https://tour.golang.org/concurrency/3
    - https://tour.golang.org/concurrency/4
  - Select
    - https://tour.golang.org/concurrency/5
    - https://tour.golang.org/concurrency/6
  - sync.Mutex: https://tour.golang.org/concurrency/9
  - Various links: https://tour.golang.org/concurrency/11

## Exercism golang track
- https://exercism.org/tracks/go
- Revisit below concepts
    - https://exercism.org/tracks/go/concepts/runes

## Pending
- https://go.dev/doc/code
- https://golang.org/doc/effective_go
