var merge = function(left, right){
  var result = [], 
    il = 0,
    ir = 0;
  while(il < left.length && ir < right.length) {
    if(left[il] < right[ir]) {
      result.push(left[il++]); // {9}
    } else{
      result.push(right[ir++]); // {10}
    }
  }
  while (il < left.length){
    result.push(left[il++]);
  }
  while (ir < right.length){
    result.push(right[ir++]);
  }
  return result;
}

var mergeSort = function(array){
  var length = array.length;
  // if(length === 1) {
  //   return array;
  // }
  if (length === 1) return array;
  var mid = Math.floor(length / 2),
    left = array.slice(0, mid),
    right = array.slice(mid, length); //{5}
  return merge(mergeSort(left), mergeSort(right)); //{6}
};

console.log(mergeSort([2, 5, 1, 3, 7, 2, 3, 8, 6, 3]))