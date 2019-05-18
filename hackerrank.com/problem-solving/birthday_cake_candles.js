// https://www.hackerrank.com/challenges/birthday-cake-candles/problem

function birthdayCakeCandles(ar) {
  ar = ar.sort((a, b) => b - a)
  a = 0
  while (ar[++a] === ar[0] && a < ar.length) { }
  return a
}

function birthdayCakeCandles2(ar) {
  var max = Math.max(...ar)
  return ar.filter(x => x === max).length
}


function main(inputData) {
  const lines = inputData.split("\n");
  const n = parseInt(lines[0])
  const ar = lines[1].split(' ').map(x => parseInt(x))
  console.log(birthdayCakeCandles2(ar))
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