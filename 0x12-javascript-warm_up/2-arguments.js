#!/usr/bin/node
const argums = process.argv.length;
console.log(
  argums === 2
    ? 'No argument'
    : argums === 3
      ? 'Argument found'
      : 'Arguments found'
);
