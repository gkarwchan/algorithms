// https://www.hackerrank.com/challenges/plus-minus/problem

function plusMinus(arr) {
  const plus = (arr.filter(x => x > 0).length / arr.length).toFixed(6).toString()
  const minus = (arr.filter(x => x < 0).length / arr.length).toFixed(6).toString()
  const zero = (arr.filter(x => x === 0).length / arr.length).toFixed(6).toString()
  console.log(plus)
  console.log(minus)
  console.log(zero)
} 

function main(inputData) {
  const lines = inputData.split("\n");
  const N = parseInt(lines[0]);
  const arr = lines[1].split(' ').map(val => parseInt(val))
  plusMinus(arr)
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