#!/usr/bin/node
// Searches the second biggest integer in the list of arguments

const listInt = process.argv.slice(2).map(Number);

if (listInt.length <= 1) {
  console.log(0);
} else {
  listInt.sort((aa, ab) => ab - aa);
  console.log(listInt[1]);
}
