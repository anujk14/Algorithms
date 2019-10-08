/*
Problem: Given an integer n, write a function that will return the nth Fibonacci number.
 */

function findNthFib(n){
  if(n === 0) return 0;
  if(n === 1) return 1;

  var cache = [];

  cache[0] = 0;
  cache[1] = 1;

  return findNthFibCache(n, cache);
}

function findNthFibCache(n, cache) {
  if(cache[n] >= 0) return cache[n];

  cache[n] = findNthFibCache(n-1, cache) + findNthFibCache(n-2, cache);

  return cache[n];
}