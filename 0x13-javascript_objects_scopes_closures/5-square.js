#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size);
    this.size = size;
  }
  charPrint(c){
    if(c){
      const y = c;
    }
    else{
      const y = 'X';
    }
    let i;
    const result = y.repeat(this.width);
    for (i = 0; i < this.height; i++) {
      console.log(result);
    }
  }
}
module.exports = Square;
