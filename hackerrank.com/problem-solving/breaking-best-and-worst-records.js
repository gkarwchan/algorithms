// https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

function breakingRecords(scores) {
    const minMax = scores.reduce((minMax, i) => {
        if (i < minMax.minScore) {
            minMax.minScore = i;
            minMax.minBreak++;
        } else if (i > minMax.maxScore) {
            minMax.maxScore = i;
            minMax.maxBreak++;
        }
        return minMax;
    }, { minBreak: 0, maxBreak: 0, minScore: scores[0], maxScore: scores[0]});
    return [minMax.maxBreak, minMax.minBreak];
} 


function main(inputData) {
    const lines = inputData.split("\n");
    const n = parseInt(lines[0])
    const ar = lines[1].split(' ').map(x => parseInt(x))
    console.log(...breakingRecords(ar))
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