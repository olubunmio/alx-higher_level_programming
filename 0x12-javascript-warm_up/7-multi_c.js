#!/usr/bin/node

if (process.argv[2]) {
  let x = Number(process.argv[2]);
  if (x > 0) {
    while (x) {
      console.log('C is fun');
      x--;
    }
  }
} else {
  console.log('Missing number of occurrences');
}
