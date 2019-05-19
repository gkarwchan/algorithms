# Loop

Traverse:
```scala
for (i <- 0 until 10)
  println(i)

for (i <- range)

0 until 10
0 until (10, 2)

(0 until 10).reverse

// where a is an array or sequence

for (elem <- a)
  println(elem)

for (elem <- a if a % 2 == 0)
```

## Transforming Arrays

```scala
val a = Array(2,3,4,5,7, 11)
val result = for (elem <- a) yield 2 * elem
```

# Arrays

## Array Methods

#### Create array

```scala
// new with one argument, the length of the array
val nums = new Array[Int](10)
// without new it is initialize
val numData = Array(4, 6, 7, 4)
```

#### max

```scala
var ar [Array:Int] = Array(1, 3, 4, 5)
ar.max
```

#### filter
```scala
a.filter(_ % 2 == 0)
a filter { _ % 2 == 0 }

// or 

for (elem <- a if a % 2 == 0)
```

#### map
```scala
a.map(2 * _)
a map { 2 * _ }

// or 

for (elem <- a ) yield 2 * elem
```


##### example: filter and map
```scala
a.filter(_ % 2 == 0).map(2 * _)
a filter { _ % 2 == 0 } map { 2 * _ }

// or 

for (elem <- a if a % 2 == 0) yield 2 * elem
```

#### sorted
```scala
val b = ArrayBuffer(1, 7, 2, 9)
val bSorted = b.sroted(_ < _)

val a = Array(1, 7, 2, 9)
scala.util.Sorting.quickSort(a)
```