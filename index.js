let express = require('express');
let mongoose = require('mongoose');
let app = express();
var port = process.env.PORT || 8080;
let User = require('./models/Users');
let path = require('path');
var bodyParser = require('body-parser');
// create application/json parser
var jsonParser = bodyParser.json();

// create application/x-www-form-urlencoded parser
var urlencodedParser = bodyParser.urlencoded({ extended: false });

mongoose.connect(
  'mongodb+srv://elliot-eisenberg:0mgJdNMP1q3GJfTg@testdb-runjj.mongodb.net/test?retryWrites=true&w=majority',
  { useNewUrlParser: true }
);

//First middleware before response is sent
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '/public/index.html'));
  //res.sendFile();
  // var newUser = new User({
  //   name: 'Elliot',
  //   email: 'elliotei@usc.edu',
  //   bio: 'This is my bio'
  // });
  // newUser.speak();

  // res.send('Hello ' + newUser.name);
});

app.post('/newUser', urlencodedParser, (req, res) => {
  var newUser = new User({
    name: req.body.name,
    email: req.body.email,
    bio: req.body.bio
  });

  newUser.save(err => {
    if (err) {
      return res.send(err);
    }
    res.send(
      'User was created! Click <a href="localhost:8080/listUsers">here</a> to view all users'
    );
  });
});

app.get('/listUsers', (req, res) => {
  User.find((err, users) => {
    if (err) {
      return res.send(err);
    }

    var output = '';
    users.forEach(item => {
      output += `<h1>${item.name}</h1><p>${item.email}</p><p>${
        item.bio
      }</p><br /><br /><br />`;
    });

    if (output == '') {
      output = 'There are no users';
    }

    res.send(output);
  });
});

app.listen(port);
