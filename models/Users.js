let mongoose = require('mongoose');
var userSchema = new mongoose.Schema({
  name: String,
  email: { type: String, unique: true, required: true },
  bio: String,
  registered: { type: Date, default: Date.now }
});

userSchema.methods.speak = function() {
  var greeting = this.name ? 'My name is ' + this.name : 'I dont have a name';
  console.log(greeting);
};

var User = mongoose.model('User', userSchema);
module.exports = User;
