#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let aa = 0; aa < this.height; aa++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
