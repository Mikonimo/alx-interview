#!/usr/bin/node

const axios = require('axios');
const process = require('process');

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.error("Usage: ./0-starwars_characters.js <Movie ID>");
  process.exit(1);
}

// URL for the Star Wars API films endpoint
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Fetch the movie details
axios.get(url)
  .then(response => {
    const characters = response.data.characters;
    const characterPromises = characters.map(characterUrl => axios.get(characterUrl));

    // Fetch all character names in order
    return Promise.all(characterPromises);
  })
  .then(responses => {
    responses.forEach(response => {
      console.log(response.data.name);
    });
  })
  .catch(error => {
    console.error("Error fetching data:", error.message);
  });
