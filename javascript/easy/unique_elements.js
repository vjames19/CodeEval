var fs  = require("fs");

function workIt(line) {
  var numbers = line.split(',');

  var size = numbers.length;
  var result = [];
  result.push(numbers[0]);
  for(var i=1; i < size; i++) {
    if(numbers[i-1] !== numbers[i]) {
      result.push(numbers[i]);
    }
  }

  console.log(result.join(','));
}
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line !== "") {
      workIt(line);
    }
});
