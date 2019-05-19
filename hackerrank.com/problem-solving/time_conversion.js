// https://www.hackerrank.com/challenges/time-conversion/problem

function timeConversion(s) {
  var match = s.match(/(\d{2})(:\d{2}:\d{2})(A|P)M/);
  var hour = parseInt(match[1]);
  if (match[3] === 'A' && hour === 12) return `00${match[2]}`;
  if (match[3] === 'A') return `${match[1]}${match[2]}`
  if (hour === 12) return `${match[1]}${match[2]}`
  return `${hour + 12}${match[2]}`
}


function main(inputData) {
  const lines = inputData.split("\n");
  // const n = parseInt(lines[0])
  const s = lines[0]
  // const ar = lines[1].split(' ').map(x => parseInt(x))
  console.log(timeConversion(s))
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
