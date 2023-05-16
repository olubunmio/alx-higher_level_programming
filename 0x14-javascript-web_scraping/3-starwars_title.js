#!/usr/bin/node
/* A  script that prints the title of a Star Wars movie where the episode
   number matches a given integer.

   The first argument is the movie ID
   You must use the Star wars API with the endpoint
   https://swapi-api.alx-tools.com/api/films/:id
   You must use the module request
*/
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;
request(url, function (_err, _res, body) {
  body = JSON.parse(body);
  console.log(body.title);
});
