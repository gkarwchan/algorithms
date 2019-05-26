'use strict'

// https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

function divisibleSumPairs(n, k, ar) {
  let res = new Array(k);
  res.fill(0,0,k);
  ar.reduce((acc, i) => { res[i % k]++; return res;}, res);
  let count = 0;
  for (let i = 1; i < Math.floor((k - 1) / 2) + 1; i++) {
    count += res[i] * res[k-i];
  }
  let selfSum = k % 2 === 0 ? [0, k / 2] : [0];
  count = selfSum.reduce((acc, i) => { acc += res[i] * (res[i] - 1) / 2; return acc; }, count);
  return count;
}


function main(inputData) {
  const lines = inputData.split("\n");
  const [n, k] = lines[0].split(' ').map(x => parseInt(x));
  const ar = lines[1].split(' ').map(x => parseInt(x));
  console.log(divisibleSumPairs(n, k, ar))
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