var fs  = require("fs");

function workIt(line) {
  var a = 'a'.charCodeAt(0);
  var j = 'j'.charCodeAt(0);
  var zero = 48, nine = 57;
  var digits = [];
  for(var i=0; i < line.length; i++) {
    var code = line.charCodeAt(i);
    if(code >= a && code <= j)  {
      digits.push(code - a);
    } else if(code >= zero && code <= nine) {
      digits.push(code - zero);
    }
  }

  console.log(digits.length > 0 ? digits.join('') : 'NONE');
}

fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line != "") {
    workIt(line);
  }
});
