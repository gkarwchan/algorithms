// https://www.hackerrank.com/challenges/grading/problem

function gradingStudents(grades) {
    return grades.map(x => x < 38 ? x : (x % 5 > 2 ? x + 5 - x % 5 : x));
} 


function main(inputData) {
    const lines = inputData.split("\n");
    const n = parseInt(lines[0])
    const ar = lines.slice(1, n + 1).map(x => parseInt(x))
    console.log(gradingStudents(ar).join('\n'))
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