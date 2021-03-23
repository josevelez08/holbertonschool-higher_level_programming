#!/usr/bin/node

function some () {
  if (!isNaN(process.argv[2])) {
    const occu = parseInt(process.argv[2]);
    let i;
    for (i = 0; i < occu; i++) {
      console.log('C is fun');
    }
  } else {
    console.log('Missing number of occurrences');
  }
}
some();
