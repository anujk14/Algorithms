/*
Problem: Given a 2D boolean array, find the largest square subarray of true values.
The return value should be the side length of the largest square subarray subarray.
 */

function squareSubMatrix(arr) {
  let max = 0;
  for(let i = 0; i < arr.length; i++){
    for(let j = 0; j < arr[0].length; j++){
      if(arr[i][j])
        max = Math.max(max, findSquareSubmatrix(arr, i, j))
    }
  }
  return max;
}

function findSquareSubmatrix(arr, i, j) {
  if(i === arr.length || j === arr[0].length)
    return 0;
  if(!arr[i][j]) return 0;

  return 1 + Math.min(Math.min(findSquareSubmatrix(arr, i, j+1), findSquareSubmatrix(arr, i+1, j)), findSquareSubmatrix(arr, i+1, j+1));
}