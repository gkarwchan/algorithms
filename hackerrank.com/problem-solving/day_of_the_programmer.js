// https://www.hackerrank.com/challenges/day-of-the-programmer/problem

function dayOfProgrammer(year) {
  if (year === 1918) return '26.09.1918'
  if (year % 4 === 0 && ((year % 100 !== 0) || year % 400 === 0 || year < 1918))
    return `12.09.${year}`
  return `13.09.${year}`
}

function main(inputData) {
  const lines = inputData.split("\n");
  const year = parseInt(lines[0])
  console.log(dayOfProgrammer(year))
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