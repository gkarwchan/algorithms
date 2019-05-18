// https://www.hackerrank.com/challenges/staircase/problem

function staircase(arr) {
  for (let i = 1; i <= n; i++) {
    console.log(`${'#'.repeat(i).padStart(n, ' ')}`)
  }
} 

function main(inputData) {
  const lines = inputData.split("\n");
  const N = parseInt(lines[0]);
  const arr = lines[1].split(' ').map(val => parseInt(val))
  staircase(arr)
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