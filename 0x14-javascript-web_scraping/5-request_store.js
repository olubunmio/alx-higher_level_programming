#!/usr/bin/node
/*  A script that gets the contents of a webpage and stores it in a file.

    The first argument is the URL to request
    The second argument the file path to store the body response
    The file must be UTF-8 encoded
    You must use the module request
*/
const request = require('request');
const fs = require('fs');

const myFunc1 = function (_err, _rsp, body) {
  if (_err) {
    console.log(_err);
  }
};

const myFunc2 = function (_err) {
  if (_err) {
    console.log(_err);
  }
};

request(process.argv[2], myFunc1).pipe(fs.FileWriteStream(process.argv[3], 'utf8', myFunc2));
