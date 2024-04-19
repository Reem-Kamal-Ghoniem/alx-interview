#!/usr/bin/node

const request = require('request');

request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2],
  function (err, res, body) {
    if (err) throw err;
    const actors = JSON.parse(body).characters;
    printing(actors, 0);
  });

const printing = (actors, x) => {
  if (x === actors.length) return;
  request(actors[x], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    printing(actors, x + 1);
  });
};
