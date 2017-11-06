var mongoose = require('mongoose'),
	Scehema = mongoose.Schema;

var ledSchema = new Schema({
	title: String,
	gpio:	Number,
	mode:	{type:String, enum:["BCM,""BOARD"]}
	value: Number
});

module.exports = mongoose.model("Led", ledSchema);
