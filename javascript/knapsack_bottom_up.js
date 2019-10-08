/*
Problem: Given a list of items with values and weights, as well as a max weight,
find the maximum value you can generate from items, where the sum of the weights is less than or equal to the max.
e.g.
items = [{ weight: 2, value: 6}, {weight: 2, value:  10}, {weight: 3, value: 12}]
max weight = 5
knapsack(items, max weight) = 22
 */

function knapsack(items, w) {
  let cache = {};

  items.forEach(i => {
    let newCache = {};
    for (let j = 0; j <= w; j++) {
      if (i.weight > j) newCache[j] = cache[j] ||0;
      else newCache[j] = Math.max(cache[j], cache[j - i.weight] + i.value) || 0;
    }
    cache = newCache;
  })
  return cache[w]
}

