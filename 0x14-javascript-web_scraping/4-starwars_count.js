#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterId = '18';

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    let count = 0;
    data.results.forEach((film) => {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
        count += 1;
      }
    });
    console.log(count);
  }
});
