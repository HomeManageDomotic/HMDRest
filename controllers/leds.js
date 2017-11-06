//var mongoose = require('mongoose');  
//var TVShow  = mongoose.model('TVShow');
var cmd = require('node-cmd');
var PY_SCRIPTS = "pyScripts/";
var PYTHON = "python ";
var LED_SCRIPT = 'ledAction.py';
/*PythonShell.run('pyScripts/ledAction.py'+option, function (err) {
  if (err) throw err;
  console.log('finished');
});
*/

//POST - Insert a new TVShow in the DB
exports.actionOnLed = function(req, res) {  
    console.log('POST');
    console.log(req.body);
    run=PYTHON+PY_SCRIPTS+LED_SCRIPT+" -pin "+ req.body.gpio + " -a "+ req.body.value

    if(req.body.type != undefined && req.body.type != null && req.body.type != 0){
	run = run + " -board "
    }

    cmd.get(run, (err, data, stderr) => {
	if(err){
	  console.log("Error Trace: "+err+" \nSTDERR: "+stderr);
          res.status(500).send(err);
	}
	res.status(200).send("OK: "+data);
	
    });	
};

//GET - Return a TVShow with specified ID
exports.getLedStatus = function(req, res) {  
    console.log("GET STATUS");
    console.log(req.params)
    run = PYTHON+PY_SCRIPTS+LED_SCRIPT+" -get -pin "+req.params.pin;

    if(req.params.type != undefined && req.params.type != null && req.params.type != 0){
	run = run + " -board";
    }

    cmd.get(run, (err, data, stderr)=>{
	if(err){
	  console.log("Error Trace: "+err+" \nSTDERR: "+stderr);
          res.status(500).send(err);
	}
	console.log("Response:" + data);
	res.status(200).send(data);
    });
};
