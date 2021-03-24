#!/usr/bin/node
const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let y;
    y = c;
    if (c === undefined) {
      y = 'X';
    }
    let i;
    const result = y.repeat(this.size);
    for (i = 0; i < this.size; i++) {
      console.log(result);
    }
  }
}
module.exports = Square;
