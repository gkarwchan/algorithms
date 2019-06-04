// /https://www.hackerrank.com/challenges/electronics-shop/problem

function getMoneySpent(keyboards, drives, b) {
  keyboards = keyboards.sort((a, b) => b - a);
  drives = drives.sort((a, b) => b - a);
  if (keyboards[keyboards.length -1] + drives[drives.length - 1] > b) return -1;
  if (keyboards[0] + drives[0] <= b) return keyboards[0] + drives[0];
  let maxVal = 0;
  for (let i = 0; i < keyboards.length; i++) {
    for (let j = 0; j < drives.length; j++) {
      const cost = keyboards[i] + drives[j]
      if (cost === b)
        return b
      else {
        if (cost < b) {
          maxVal = Math.max(maxVal, cost)
          break;
        }
      }
    }
  }
  return maxVal;
}

function main(inputData) {
  const lines = inputData.split("\n")
  const [b, n, m] = lines[0].split(' ').map(x => parseInt(x))
  const keyboards = lines[1].split(' ').map(x => parseInt(x))
  const drives = lines[2].split(' ').map(x => parseInt(x))
  console.log(getMoneySpent(keyboards, drives, b))
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