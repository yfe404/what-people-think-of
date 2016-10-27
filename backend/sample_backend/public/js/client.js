// Draft
// TODO: Use babel-loader (ES6->ES5) ?

function search(query) {
  return new Promise(function(resolve, reject) {
    var client = new XMLHttpRequest();
    // ...
    client.onLoad = function () {};
    client.onerror = function () {};
  })
}
