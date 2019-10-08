/*
Problem: Given a 2D boolean array, find the largest square subarray of true values.
The return value should be the side length of the largest square subarray subarray.
input - [[0, 1, 0, 0], [1, ,1, 1, 1], [0, 1, 1, 0]]
 */

function squareSubMatrix(arr) {
  let cache = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]];
  let max = 0;
  for(let i = 0; i < arr.length; i++){
    for(let j = 0; j < arr[0].length; j++){
      if(arr[i][j])
        max = Math.max(max, findSquareSubmatrix(arr, i, j, cache))
    }
  }
  return max;
}

function findSquareSubmatrix(arr, i, j, cache) {
  if(i === arr.length || j === arr[0].length)
    return 0;
  if(!arr[i][j]) return 0;

  if(cache[i] && cache[i][j] > 0) return cache[i][j];

  cache[i][j]  = 1 + Math.min(Math.min(findSquareSubmatrix(arr, i, j+1, cache), findSquareSubmatrix(arr, i+1, j, cache)), findSquareSubmatrix(arr, i+1, j+1, cache));

  return cache[i][j];
}
