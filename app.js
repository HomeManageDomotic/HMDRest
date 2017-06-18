var express = require("express"),  
    app = express(),
    bodyParser  = require("body-parser"),
    methodOverride = require("method-override");

app.use(bodyParser.urlencoded({ extended: false }));  
app.use(bodyParser.json());  
app.use(methodOverride());

var router = express.Router();

router.get('/', function(req, res) {  
   res.send("Hello World!");
});

app.use(router);

app.listen(3000, function() {  
  console.log("GPIO Node Rest Server http://localhost:3000");
});



/*
#var PythonShell = require('python-shell');


#PythonShell.run('ledAction.py -pin '+pin, function (err) {
#  if (err) throw err;
#  console.log('finished');
#});
*/
