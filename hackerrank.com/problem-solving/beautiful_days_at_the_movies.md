
# Problem
[Problem description](https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem)

## Explanation:
The main ideas of this puzzle are:

1. reverse a string
    * python: str[::-1]
    * js: array.reverse
    

### Python

```python
def beautifulDays(i, j, k):
    return sum ([1 for i in range(i, j + 1) if (int(str(i)[::-1]) - i) % k == 0])

if __name__ == '__main__':
    i, j, k = map(int, input().split())
    print(beautifulDays(i, j, k))
```
### JavaScript

```js

function beautifulDays(i, j, k) {
    let days = 0;
    for (let ind = i; ind <= j ; ind++) {
        days += (ind - Number(ind.toString().split('').reverse().join(''))) % k === 0 ? 1 : 0;
    }
    return days;
}


function main(inputData) {
    const [i, j, k] = inputData.split(' ').map(Number);

    console.log(beautifulDays(i, j, k));
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