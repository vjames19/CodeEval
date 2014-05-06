var fs  = require("fs");

function workIt(line) {
  line = line.toLowerCase();
  var map = {};
  var length = line.length;
  for(var i=0; i < length; i++) {
    var character = line.charAt(i);
    if(character >= 'a' && character <= 'z') {
      map[character] = map[character] ? map[character] + 1: 1;
    }
  }

  var counts = [];
  for(var k in map) {
    counts.push(map[k]);
  }
  counts.sort(function(a, b) {
    return b - a;
  });

  var value = 26;
  console.log(counts.reduce(function(a, b) {
    b = b * value;
    value--;
    return a + b;
  }, 0));
}
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line !== "") {
      workIt(line);
    }
});
