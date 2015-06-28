/**
 * Webpack development configuration
 */
/*globals __dirname:false */
var path = require("path");
var webpack = require("webpack");
var base = require("./webpack.config");
// var CleanPlugin = require("clean-webpack-plugin");
var BundleTracker = require('webpack-bundle-tracker');

var bundles_path = path.join(__dirname, "bundles");

module.exports = {
  cache: true,
  context: base.context,
  entry: base.entry,
  output: {
    path: bundles_path,
    filename: "bundle.js",
    publicPath: "http://127.0.0.1:2992/js"
  },
  module: base.module,
  resolve: base.resolve,
  devtool: "eval-source-map",
  stylus: base.stylus,
  plugins: [
    // ignore all moment locals
    // new webpack.IgnorePlugin(/^\.\/locale$/, /moment$/),

    new BundleTracker({filename: path.join(__dirname, 'webpack-stats.json')}),
    // Clean
    // new CleanPlugin(["dist"]),
    // if an asset errors during compiling don't include it.
    // new webpack.NoErrorsPlugin()
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: JSON.stringify(process.env.NODE_ENV)
      }
    })
  ]
};
