# Problem
[Problem description](https://www.hackerrank.com/challenges/diagonal-difference/problem)

## Explanation:
The main idea of this puzzle is to do it in one iteration: O(n) only


### Python

```python
def diagonalDifference(arr):
    axs = [arr[i][i] - arr[i][-i -1] for i in range(len(arr))]
    return abs(sum(axs))

if __name__ == '__main__':
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(diagonalDifference(arr))
```
### JavaScript

```js
function diagonalDifference(arr) {
  const ax = arr.reduce((acc, line, ind) => acc - line[ind] + line[arr.length - 1 - ind], 0);
  
  return Math.abs(ax);
} 

function main(inputData) {
  const lines = inputData.split("\n");
  const N = parseInt(lines[0]);
  const arr = lines.slice(1, N + 1).map(line => line.split(' ').map(Number))
  console.log(diagonalDifference(arr))
}

process.stdin.resume();
process.stdin.setEncoding("utf-8");
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
import scala.io.StdIn._

object Solution {
  def main(args: Array[String]) {
    val n = readInt
    var ax1, ax2 = 0
    for (i <- 0 until n) {
      val values = readLine.split(" ").map(_.trim.toInt)
      ax1 += values(i)
      ax2 += values(n - i - 1)
    }

    println(Math.abs(ax1 - ax2))
  }
}
```