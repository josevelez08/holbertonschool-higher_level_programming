#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    let i;
    const result = c.repeat(this.size);
    for (i = 0; i < this.size; i++) {
      console.log(result);
    }
  }
}
module.exports = Square;
