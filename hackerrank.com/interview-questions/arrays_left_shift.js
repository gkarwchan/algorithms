//  https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

function rotLeft(arr, b) {
  const f = b % arr.length;
  return [...arr.slice(f), ...arr.slice(0,f)].join(' ');
}


function main(inputData) {
  const lines = inputData.split("\n");
  const [a, b] = lines[0].split(' ').map(x => parseInt(x));
  const arr = lines[1].split(' ');

  console.log(rotLeft(arr, b));
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