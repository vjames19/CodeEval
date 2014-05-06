var fs  = require("fs");

function workIt(line) {
  var w = line.split(',');

  var numbers = [], words = [];
  w.forEach(function(wordOrNumber) {
    var n = parseInt(wordOrNumber, 10);
    if(isNaN(n)) {
      words.push(wordOrNumber);
    } else {
      numbers.push(wordOrNumber);
    }
  });

  if(words.length > 0 && numbers.length > 0) {
    console.log('%s|%s', words.join(','), numbers.join(','));
  } else {
    console.log(words.length > 0 ? words.join(',') : numbers.join(','));
  }
}

fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  line = line.trim();
  if(line !== "" ) {
    workIt(line.trim());
  }
});
