// https://www.hackerrank.com/challenges/counting-valleys/problem

function countingValleys(n, s) {
  let acc = 0
  const r = s.split('').map(x => x === 'U' ? 1 : -1).map(y => { acc += y; return acc; })
  const rslt = r.reduce((acc, i) => acc.prv === -1 && i === 0 ? {prv: i, val: ++acc.val} : {prv: i, val: acc.val}, {prv: 0, val: 0})
  return rslt.val
}

function countingValleys(n, s) {
  const steps = s.split('');
  const tracker = steps.reduce((elevationTracker, step) => {
    const previousElevation = elevationTracker.currentElevation;
    if (step === 'U') {
        elevationTracker.currentElevation++
    } else {
        elevationTracker.currentElevation--
    }
    if (elevationTracker.currentElevation === -1 && previousElevation === 0) {
        elevationTracker.valleys++
    }
    return elevationTracker;
  }, {currentElevation: 0, valleys: 0});
  return tracker.valleys;
}

function main(inputData) {
  const lines = inputData.split("\n")
  const n = parseInt(lines[0])
  const s = lines[1]
  console.log(countingValleys(n, s))
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