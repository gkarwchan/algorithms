/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
  let len = nums.length;
  if(!len){
      return 0
  }
  if(len == 1){
      return nums[0];
  } 
  
  if(len == 2){
      return Math.max(nums[0], nums[1])
  }
  if(len == 3){
      return Math.max(nums[1], nums[0] + nums[2])
  }
  let dp = [];
  dp[0] = nums[0];
  dp[1] = Math.max(nums[0], nums[1]);
  dp[2] = Math.max(nums[1], nums[0] + nums[2]);
  let max = Math.max(dp[0], dp[1], dp[2]);
  for(let i=3;i<nums.length;i++){
      dp[i] = Math.max(dp[i-2] + nums[i], dp[i-3] + nums[i])
      max = Math.max(dp[i], max)
  }
  return max
};

var rob = function(nums) {
  let currentMax = 0;
  let prevMax = 0;

  for(let i = 0; i < nums.length; i++) {
    let currentHouse = nums[i];
    let newMax = Math.max(currentMax, prevMax + currentHouse)
    prevMax = currentMax;
    currentMax = newMax;
  }

  return currentMax;
};

var rob = function(nums) {
  if(nums.length === 0) return 0;
  let prevMax = 0;
  let lastMax = nums[0];

  for(let i = 1; i < nums.length; i++){
    const currHouse = nums[i];
    const currMax = Math.max(lastMax, currHouse+prevMax);
    prevMax = lastMax;
    lastMax = currMax;
  }

  return lastMax
};

var rob = function(nums) {
  const dp = new Array(nums.length+1).fill().map(_ => new Array(2).fill(0))
  // [0] would be rob
  // [1] would be not rob
  dp[0][0] = 0
  dp[0][1] = 0
  
  for(let i=0; i<nums.length; i++) {
      dp[i+1][0] = dp[i][1] + nums[i]
      dp[i+1][1] = Math.max(dp[i][0], dp[i][1])
  }
  return Math.max(...dp[dp.length-1])
};
