## Golang difference with C language
- Golang only has one looping construct `for` which serves all purpose
- Golang switch case doesn't need break in each case, it executes only matching case. In C all cases after matching case gets executed if we don't break
- Golang doesn't support pointer arithematic as supported in C
- Using struct pointers, golang permits accessing members using dot `p.x` or `(*p).x` and in C arrow notation is used access members `p->x`
- Methods with pointer receivers take either a value or a pointer as the receiver when they are called: https://tour.golang.org/methods/6
- Methods with value receivers take either a value or a pointer as the receiver when they are called: https://tour.golang.org/methods/7
- Unlike in C, it's perfectly OK to return the address of a local variable in Go; the storage associated with the variable survives after the function returns.

## Go mod and sum file
https://golangbyexample.com/go-mod-sum-module/
- `go.mod`: It defines both project's dependencies requirement and also locks them to their correct version.
- `go.sum`: This file lists down the checksum of direct and indirect dependency required along with the version. The checksum present in go.sum file is used to validate the checksum of each of direct and indirect dependency to confirm that none of them has been modified.

## Golang tour
https://tour.golang.org
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
https://exercism.org/tracks/go
- Revisit
  - https://exercism.org/tracks/go/concepts/runes

## How to write Go code
https://go.dev/doc/code
- Go programs are organized into __packages__. A package is a collection of source files in the same directory that are compiled together.
- A repository contains one or more __modules__. A module is a collection of related Go packages that are released together. A Go repository typically contains only one module, located at the root of the repository.

```shell
go install <module-path>
# This command builds the hello command, producing an executable binary. It then installs that binary as $HOME/go/bin/hello
# The install directory is controlled by the GOPATH and GOBIN environment variables.
```
- The `go mod tidy` command adds missing module requirements for imported packages and removes requirements on modules that aren't used anymore.

## Effective Go
https://golang.org/doc/effective_go
- Indentation: We use tabs for indentation and gofmt emits them by default. Use spaces only if you must.
- Line length: Go has no line length limit. Don't worry about overflowing a punched card. If a line feels too long, wrap it and indent with an extra tab.
- Allocation with new: `new(T)` allocates zeroed storage for a new item of type T and returns its address, a value of type `*T`. In Go terminology, it returns a pointer to a newly allocated zero value of type T.
- Allocation with make: The built-in function `make(T, args)`. It creates slices, maps, and channels only, and it returns an initialized (not zeroed) value of type T (not `*T`).

## Pending
- https://golangbyexample.com/golang-comprehensive-tutorial/
