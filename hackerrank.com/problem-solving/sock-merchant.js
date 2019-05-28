'use strict';
// https://www.hackerrank.com/challenges/sock-merchant/problem

function sockMerchant(n, ar) {
    const counts = ar.reduce((acc, i) => {
      acc[i] = acc[i] ? ++acc[i] : 1
      return acc
    }, {})
    return Object.values(counts).reduce((acc, i) => acc + Math.floor(i/2), 0)
  }
  
  function main(inputData) {
    const lines = inputData.split("\n")
    const n = parseInt(lines[0])
    const ar = lines[1].split(' ').map(x => parseInt(x))
    console.log(sockMerchant(n, ar))
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