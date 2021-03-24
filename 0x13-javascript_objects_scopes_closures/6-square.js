#!/usr/bin/node
const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let i;
      const result = c.repeat(this.height);
      for (i = 0; i < this.height; i++) {
        console.log(result);
      }
    }
  }
}
module.exports = Square;
