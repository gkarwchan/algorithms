// https://www.hackerrank.com/challenges/compare-the-triplets/problem

function compareTriplets(a, b) {
  res = a.map((val, ind) => (val - b[ind]))
  console.log(res)
  alice = res.filter(x => x > 0).length
  bob = res.filter(x => x < 0).length
  console.log(alice, bob)
}

function main(inputData) {
  const lines = inputData.split("\n");
  const a = lines[0].split(' ').map(x => parseInt(x))
  const b = lines[1].split(' ').map(x => parseInt(x))
  compareTriplets(a,b)
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