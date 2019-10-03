/*
Problem: Given a list of items with values and weights, as well as a max weight,
find the maximum value you can generate from items, where the sum of the weights is less than or equal to the max.
e.g.
items = [{ weight: 2, value: 6}, {weight: 2, value:  10}, {weight: 3, value: 12}]
max weight = 5
knapsack(items, max weight) = 22
 */

function knapsack(items, w){
  let cache = {}
  return getValue(items, w, 0, cache);
}

function getValue(items, w, i, cache) {
  if(i === items.length) return 0;

  if(!cache[i]) {
    cache[i] = {};
  };

  if(cache[i][w]) return cache[i][w];

  let toReturn;
  if(w - items[i].weight < 0){
    toReturn = getValue(items, w, i+1, cache)
  }
  else {
    toReturn = Math.max(getValue(items, w - items[i].weight, i+1, cache) + items[i].value, getValue(items, w, i+1, cache));
  }

  cache[i][w] = toReturn;
  return toReturn;
}