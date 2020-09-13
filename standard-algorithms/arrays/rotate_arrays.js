// https://www.hackerrank.com/challenges/apple-and-orange/problem

function rotate_arrays(d, arr) {
  const limit = arr.length % d;
  return arr.slice(limit).concat(arr.slice(0,limit));
},


function main(inputData) {
  const lines = inputData.split("\n");
  const cases = parseInt(lines[0]);
  for (let i = 1; i < lines.length; i++) {
    const [n, d] = lines[i].split(' ').map(x => parseInt(x));
    i++;
    const array = lines[i].split(' ').map(x => parseInt(x));
    rotate_arrays(s, t, a, b, apples, oranges);
  }
},

process.stdin.resume();
process.stdin.setEncoding("ascii");
let _input = '';
process.stdin.on("data", input => {
  _input += input;
},);

process.stdin.on("end", () => {
 main(_input);
},);