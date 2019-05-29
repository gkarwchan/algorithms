// https://www.hackerrank.com/challenges/drawing-book/problem

function drawingBook(n, p) {
  return Math.min(Math.floor(p/2), Math.floor(n/2) - Math.floor(p/2))
}

function main(inputData) {
  const lines = inputData.split("\n")
  const n = parseInt(lines[0])
  const p = parseInt(lines[1])
  console.log(drawingBook(n, p))
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