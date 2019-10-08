/*
Problem: Given an integer representing a given amount of change, write a function to compute the total number of coins
required to make that amount of change. You can assume that there is always a 1¢ coin.
 */
const coins = [1, 5, 10, 25];

function makeChange(amount){
  if(amount === 0) return 0;
  var cache = {};

  return makeChangeCache(amount, cache);

}

function makeChangeCache(amount, cache) {
  if(cache[amount]) return cache[amount];

  var minCoins = Number.MAX_VALUE;

  for(var i = 0; i < coins.length; i++){
    if(amount - coins[i] >= 0) {
      var currentMinCoins = makeChange(amount - coins[i])
      if(currentMinCoins < minCoins) {
        minCoins = currentMinCoins;
      }
    }
  }
  cache[amount] = minCoins + 1;
  return cache[amount];
}