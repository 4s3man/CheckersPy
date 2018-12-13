const webpack = require('webpack');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

const config = {
    entry:  __dirname + '/src/js/index.js',
    output: {
        path: __dirname + '/dist/',
        filename: 'checkersGame.js',
    },
    resolve: {
        extensions: ['.js', '.jsx', '.css']
    },
    module: {
      rules: [
        {
          test: /\.jsx?/,
          exclude: /node_modules/,
          use: 'babel-loader'
        },
        {
          test: /\.css$/,
          use: [MiniCssExtractPlugin.loader, "css-loader"]
        }
      ]
    },
  plugins: [
    new MiniCssExtractPlugin({
      filename: "main.css",
      chunkFilename: "chunkFileName.css"
    })
  ]
};

module.exports = config;
