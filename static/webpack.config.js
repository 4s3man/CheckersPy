const webpack = require('webpack');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const OptimizeCssAssetsPlugin = require("optimize-css-assets-webpack-plugin");

module.exports = {
    entry:  {
      choose_game: __dirname + '/pages/choose_game/index.js',
      game: __dirname + '/pages/game/index.js',
    },
    output: {
        path: __dirname + '/dist/',
        filename: '[name].js',
        sourceMapFilename: '[name].[hash:8].map',
        chunkFilename: '[id].js'
    },
    optimization: {
      splitChunks: {},
      minimizer: [
        new OptimizeCssAssetsPlugin({})
      ]
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
          use: [MiniCssExtractPlugin.loader, "css-loader",
            {
              loader: "postcss-loader",
              options:{
                plugins: () => [require('autoprefixer')({
                    'browsers': ['> 1%', 'last 2 versions']
                })],
              }
            }
          ]
        }
      ]
    },
  plugins: [
    new MiniCssExtractPlugin({
      filename: "[name].css",
      chunkFilename: "[id][hash:8].css"
    }),
    new OptimizeCssAssetsPlugin({
      assetNameRegExp: /\.css$/,
      cssProcessor: require('cssnano'),
      cssProcessorPluginOptions: {
        preset: ['default', { discardComments: { removeAll: true } }],
      },
      canPrint: true
    })
  ]
};
