#!/usr/bin/node
/* A script that prints all characters of a Star Wars movie:

   The first argument is the Movie ID - example: 3 = “Return of the Jedi”
   Display one character name by line
   You must use the Star wars API
   You must use the module request
   https://swapi-api.alx-tools.com/api/films/3/
*/
const request = require('request');

const myFunc1 = function (_err, _res, body) {
  body = JSON.parse(body);
  const charactersLinks = body.characters;
  for (const personUrl of charactersLinks) {
    request(personUrl, myFunc2);
  }
};

const myFunc2 = function (_err, _res, body) {
  body = JSON.parse(body);
  console.log(body.name);
};

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;
request(url, myFunc1);
