# Problem
[Problem description](https://www.hackerrank.com/challenges/compare-the-triplets/problem)

## Explanation:
The main ideas of this puzzle are:

1. get the sign of number
    * python: math.copysign(1, n)
    * js: array.reverse
    
### Python

```python
from operator import sub
from math import copysign

def compareTriplets(a, b):
    scores = [copysign(1, sub(i, j)) for i, j in zip(a, b) if sub(i, j) != 0]
    return [scores.count(1), scores.count(-1)]

if __name__ == '__main__':
    a = tuple(map(int, input().split()))
    b = tuple(map(int, input().split()))
    scores = compareTriplets(a, b)
    print(' '.join(map(str, scores)))
```

### JavaScript

```js

function compareTriplets(a, b) {
  v = a.reduce((a, c, i) => {
    if (c - b[i] > 0) a.alice++;
    if (c - b[i] < 0) a.bob++;
    return a;
  }, { alice: 0, bob: 0});
  return [v.alice, v.bob];
}

function main(inputData) {
  const lines = inputData.split("\n");
  const a = lines[0].split(' ').map(Number)
  const b = lines[1].split(' ').map(Number)
  console.log(compareTriplets(a,b).join(' '))
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
let _input = '';
process.stdin.on("data", input => {
  _input += input;
});

process.stdin.on("end", () => {
 main(_input);
});
```
### Scala

```scala
object Solution extends App {
  val a = StdIn.readLine.split(" ").map(_.trim.toInt)
  val b = StdIn.readLine.split(" ").map(_.trim.toInt)

  val total = a.zip(b).fold((0,0)){ case (acc, pair) =>
    if(pair._1 > pair._2)
      (acc._1+1, acc._2)
    else if(pair._1 < pair._2)
      (acc._1, acc._2+1)
    else
      acc
  }
  println(s"${total._1} ${total._2}")
}
```