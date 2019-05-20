// https://www.hackerrank.com/challenges/apple-and-orange/problem

function countApplesAndOranges(s, t, a, b, apples, oranges) {
  const applePoint = apples.map(app => a + app).filter(app => app >= s && app <= t)
  const orang = oranges.map(org => b + org).filter(org => org >= s && org <= t)

  console.log(applePoint.length)
  console.log(orang.length)
}


function main(inputData) {
  const lines = inputData.split("\n");
  const [s, t] = lines[0].split(' ').map(x => parseInt(x));
  const [a, b] = lines[1].split(' ').map(x => parseInt(x));
  const [m, n] = lines[2].split(' ').map(x => parseInt(x));
  const apples = lines[3].split(' ').map(x => parseInt(x));
  const oranges = lines[4].split(' ').map(x => parseInt(x));
  
  countApplesAndOranges(s, t, a, b, apples, oranges);
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