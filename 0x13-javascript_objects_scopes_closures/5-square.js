#!/usr/bin/node

// Writes a class Square that defines a square and inherits from Rectangle of 4-rectangle.js

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor(sqrSize) {
    super(sqrSize, sqrSize);
  }
}

module.exports = Square;
