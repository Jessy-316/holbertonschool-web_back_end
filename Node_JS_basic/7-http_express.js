const express = require('express');

const args = process.argv.slice(2);
const countStudents = require('./3-read_file_async');

const DATABASE = args[0];

const app = express();
const port = 1245;

app.get('/', (request, response) => {
  response.send('Hello Holberton School!');
});

app.get('/students', async (request, response) => {
  const msg = 'This is the list of our students\n';
  try {
    const students = await countStudents(DATABASE);
    response.send(`${msg}${students.join('\n')}`);
  } catch (error) {
    response.send(`${msg}${error.message}`);
  }
});

app.listen(port, () => {
});

module.exports = app;
