/*
Problem: Given a 2D boolean array, find the largest square subarray of true values.
The return value should be the side length of the largest square subarray subarray.
 */

function squareSubMatrix(arr) {
  let cache = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]];
  let max = 0;

  for(let i = 0; i < arr.length; i++){
    for(let j = 0; j < arr[0].length; j++){
      if(i === 0 || j === 0) {
        cache[i][j] = arr[i][j] ? 1 : 0;
      }
      else if(arr[i][j]) {
        cache[i][j] = Math.min(Math.min(cache[i][j-1], cache[i-1][j]), cache[i-1][j-1]) + 1;
      }
      if (cache[i][j] > max) max = cache[i][j];
    }
  }

  return max;
}