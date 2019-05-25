// https://www.hackerrank.com/challenges/the-birthday-bar/problem

function birthday(s, d, m) {
    let cnt = 0;
    for (let i = 0; i < s.length - m + 1; i++) {
        const age = s.slice(i, i + m).reduce((ac, j) => ac += j, 0);
        if (age === d) cnt++;
    }
    return cnt;
} 


function main(inputData) {
    const lines = inputData.split("\n");
    const n = parseInt(lines[0]);
    const ar = lines[1].split(' ').map(x => parseInt(x));
    const [d,m] = lines[2].split(' ').map(x => parseInt(x));
    console.log(birthday(ar, d, m));
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