#!/usr/bin/node

if (!isNaN(process.argv[2])) {
  const occu = parseInt(process.argv[2]);
  let i;
  const y = 'x';
  const result = y.repeat(occu);
  for (i = 0; i < occu; i++) {
    console.log(result);
  }
} else {
  console.log('Missing size');
}
