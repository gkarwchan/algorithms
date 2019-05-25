// https://www.hackerrank.com/challenges/between-two-sets/problem

const gcd = (a, b) => {
    if (b === 0) return a;
    return gcd(b, a%b)
}

const lcm = (a, b) => parseInt((a*b) / gcd(a,b))


function getTotalX(a, b) {
  const lcm_a = a.reduce((acc, x) => lcm(acc, x));
  const gcd_b = b.reduce((acc, x) => gcd(acc, x));
  let count = 0;
  for (i = 1; i < parseInt(gcd_b / lcm_a) + 1; i++) {
    if (gcd_b % (lcm_a * i) === 0) count++;
  }
  return count;
}


function main(inputData) {
  const lines = inputData.split("\n");
  const [n, m] = lines[0].split(' ').map(x => parseInt(x));
  const a = lines[1].split(' ').map(x => parseInt(x));
  const b = lines[2].split(' ').map(x => parseInt(x));
  console.log(getTotalX(a, b))
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