#!/usr/bin/node
// A script that reads and prints the content of a file.
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
});