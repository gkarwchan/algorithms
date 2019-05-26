// https://www.hackerrank.com/challenges/migratory-birds/problem

// this if for only 5 types

function migratoryBirds1(arr) {
  let c = new Array(5)
  c.fill(0)
  arr.forEach(x => c[x - 1]++)
  const max = c.reduce((a, b) => Math.max(a, b))
  return c.findIndex(x => x === max) + 1
}

/* this is for unllimited types */
function migratoryBirds(arr) {
  const count = arr.reduce((acc, i) => {
    if (acc.has(i))
      acc.set(i, acc.get(i) + 1)
    else
      acc.set(i, 1)
    return acc }, new Map());
  const a = Array.from(count);
  a.sort((a, b) => {
    if (a[1] === b[1]) {
      return a[0] - b[0]
    } else {
      return b[1] - a[1]
    }
  })
  
  return a.filter(x => x[1] === a[0][1])[0][0]
}


function main(inputData) {
  const lines = inputData.split("\n");
  const n = lines[0].split(' ').map(x => parseInt(x));
  const ar = lines[1].split(' ').map(x => parseInt(x));
  console.log(migratoryBirds(ar))
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