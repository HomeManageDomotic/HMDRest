var cmd = require("node-cmd");
pin = "17";
cmd.get("python pyScripts/ledAction.py -pin 17", 
    (err, data, stderr)=>{
	
	console.log(data, err);
    }	
);
