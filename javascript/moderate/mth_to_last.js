var fs  = require("fs");

function workIt(line) {
  var elements = line.split(' ');
  var index = elements.pop();
  var size = elements.length;
  if(index <= size) {
    console.log(elements[size - index]);
  }
}

fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line !== "") {
      workIt(line);
    }
});
