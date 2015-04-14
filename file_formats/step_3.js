var fs = require('fs');

// Read file
var a = JSON.parse(fs.readFileSync('v2.json'));

// Pretend we're doing real work
a.chair = "Randy Snurr";
a.languages.push("javascript");

// Write output
fs.writeFileSync('v3.json', JSON.stringify(a));
