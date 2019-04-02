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

const stepCounter = '8';
const stepsText = 'UDDDUDUU';
const n = parseInt(stepCounter, 10);

let result = countingValleys(n, stepsText);

console.log(result);