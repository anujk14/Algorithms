/*
Problem: Given an integer n, write a function that will return the nth Fibonacci number.
 */

function findNthFib(n) {
  if(n === 0) return 0;
  var cache = [];
  cache[0] = 0;
  cache[1] = 1;

  for(var i = 2; i <= n; i++){
    cache[i] = cache[i-1] + cache[i-2];
  }

  return cache[n];
}