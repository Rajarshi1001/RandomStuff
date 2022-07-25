const express = require('express');
const mongoose = require('mongoose');

const app = express();

app.set('view engine', 'ejs');

app.use(express.urlencoded({ extended: false }));

mongoose
  .connect(
    'mongodb://mongo:27017/express_try',
    { useNewUrlParser: true }
  )
  .then(() => console.log('MongoDB Connected'))
  .catch(err => console.log(err));

const User = require('./models/users.js')

app.get('/', (req, res) => {
  User.find()
    .then(users => res.render('index', { users }))
    .catch(err => res.status(404).json({ msg: 'No items found' }));
});

app.post('/item/add', (req, res) => {
  const newUser = new User({
    firstname: req.body.firstname,
    lastname: req.body.lastname
  });

  newUser.save().then(user => res.redirect('/'));
});

const PORT = 3000;
app.listen(PORT, () => console.log(`Server started running on port ${PORT}`));
