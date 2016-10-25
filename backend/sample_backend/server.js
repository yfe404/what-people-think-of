'use strict';

const express = require('express');
const twitter = require('twitter');

// Constants
const PORT = 5000;


// twitter auth
var config = {
  consumer_key: 'OjAzkahPASwai41V9lr6VyVSd',
  consumer_secret: '1mxscunVopsL84rrgT8i6u07Q9MTYngUFuZv24iMJOOlKPyUf5',
  access_token_key: '2915847196-xclPchSaEmR9qCixUCTTrHRHWl1d6obDR83ZnQk',
  access_token_secret: 'l3YkCtl3vxvBO8MhPrkWYV48Z4UBZpTIogVbCCK2VUsCO'
};



// App
const app = express();
app.get('/', function (req, res) {
  res.send('Hello world\n');
});


// routes will go here
app.get('/twitter', function(req, res) {
  var hashtag = req.param('hashtag');

  // make a client
  var twitterClient = new twitter(config);
  // make a client
  var twitterClient = new twitter(config);
  console.log(twitterClient)
  // pass in the search string, an options object, and a callback
  twitterClient.get('search/tweets', {q: '#' +  hashtag}, function(error, tweets, response) {
    console.log(tweets);
  });
  res.send('Hashtag : ' + hashtag);
});


app.listen(PORT);
console.log('Running on http://localhost:' + PORT);
