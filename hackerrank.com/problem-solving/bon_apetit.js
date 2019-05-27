// https://www.hackerrank.com/challenges/bon-appetit/problem

function bonAppetit(bill, k, b) {
  bill.splice(k, 1)
  const sum = bill.reduce((acc, x) => acc + x, 0)
  let owning = b - sum / 2
  let msg = owning === 0 ? 'Bon Appetit' : owning.toString()
  console.log(msg)
}

function main(inputData) {
  const lines = inputData.split("\n");
  const [n,k] = lines[0].split(' ').map(x => parseInt(x))
  const bill = lines[1].split(' ').map(x => parseInt(x))
  const b = parseInt(lines[2])
  bonAppetit(bill, k, b)
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