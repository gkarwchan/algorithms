// https://www.hackerrank.com/challenges/mini-max-sum/problem

function miniMaxSum(arr) {
  arr.sort((a,b) => a -b);
  let min = arr.slice(0, 4).reduce((acc, val) => acc + val, 0)
  let max = arr.slice(1, 5).reduce((acc, val) => acc + val, 0)
  
  console.log(`${min} ${max}`)
} 

function main(inputData) {
  const lines = inputData.split("\n");
  const arr = lines[0].split(' ').map(x => parseInt(x));

  miniMaxSum(arr);
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