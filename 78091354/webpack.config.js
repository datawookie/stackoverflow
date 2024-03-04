const path = require('path');

module.exports = {
  entry: './src/index.js', // Your source entry file
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'main.js', // The output file
  },
  mode: 'production',
};
