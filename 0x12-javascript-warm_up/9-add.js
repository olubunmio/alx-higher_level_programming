#!/usr/bin/node

function add (a, b) {
  console.log(a + b);
}
const a = Number(process.argv[2]);
const b = Number(process.argv[3]);
add(a, b);
