/*
Problem: Given an integer n, write a function that will return the nth Fibonacci number.
 */

function findNthFib(n) {
  if(n < 2) return n;

  return findNthFib(n-1) + findNthFib(n-2);
}