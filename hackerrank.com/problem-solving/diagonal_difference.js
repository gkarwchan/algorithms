// https://www.hackerrank.com/challenges/diagonal-difference/problem

function diagonalDifference(arr) {
  const ax1 = arr.reduce((acc, line, ind) => {
    acc += line[ind]
    return acc
  }, 0);
  const ax2 = arr.reduce((acc, line, ind) => {
    acc += line[arr.length - 1 - ind]
    return acc
  }, 0);
  return Math.abs(ax1 - ax2)
} 

function main(inputData) {
  const lines = inputData.split("\n");
  const N = parseInt(lines[0]);
  const arr = lines.slice(1, N + 1).map(line => line.split(' ').map(val => parseInt(val)))
  console.log(diagonalDifference(arr))
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