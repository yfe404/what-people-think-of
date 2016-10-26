module.exports = {
    entry: "./js/main.js",
    output: {
        path: __dirname + "/build",
        filename: "bundle.js"
    },
    module: {
        loaders: [{
            test: /\.css$/,
            loader: "style!css"
        }, {
            test: /\.(woff|woff2)$/,
            loader: "url-loader?limit=10000&mimetype=application/font-woff"
        }, {
            test: /\.ttf$/,
            loader: "file-loader"
        }, {
            test: /\.eot$/,
            loader: "file-loader"
        }, {
            test: /\.svg$/,
            loader: "file-loader"
        }]
    }
};
