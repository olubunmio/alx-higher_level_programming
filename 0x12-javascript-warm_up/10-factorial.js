#!/usr/bin/node

function fact (x) {
  if (x === 1 || isNaN(x)) {
    return (1);
  }
  return x * fact(x - 1);
}
const num = Number(process.argv[2]);
console.log(fact(num));
