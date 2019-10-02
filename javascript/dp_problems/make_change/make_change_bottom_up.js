/*
Problem: Given an integer representing a given amount of change, write a function to compute the total number of coins
required to make that amount of change. You can assume that there is always a 1¢ coin.
 */
const coins = [1, 5, 10, 25];

function makeChange(amount) {
  if (amount === 0) return 0;
  var cache = [0];

  for (var i = 1; i <= amount; i++) {
    var minCoins = Number.MAX_VALUE;

    for (var j = 0; j < coins.length; j++) {
      if (i - coins[j] >= 0) {
        var currentMinCoins = cache[i - coins[j]] + 1;
        if (currentMinCoins < minCoins){
          minCoins = currentMinCoins;
        }
      }
    }
    cache[i] = minCoins;
  }
  return cache[amount];
}