const { getDefaultConfig } = require('expo/metro-config');

const defaultConfig = getDefaultConfig(__dirname);

module.exports = {
  ...defaultConfig,
  web: {
    ...defaultConfig.web,
    bundler: 'webpack',
  },
};
