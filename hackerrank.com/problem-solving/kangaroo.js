
// https://www.hackerrank.com/challenges/kangaroo/problem

function kangaroo(x1, v1, x2, v2) {
  if (v2 >= v1) return 'NO';
  const rem = (x2 - x1) % (v1 - v2)
  return rem === 0 ? 'YES' : 'NO'
}


function main(inputData) {
  const lines = inputData.split("\n");
  const inputs = lines[0].split(' ').map(x => parseInt(x));
  console.log(kangaroo(...inputs))
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