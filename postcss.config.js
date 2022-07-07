const tailwindcss = require("tailwindcss");
const pimport = require('postcss-import');
// const postcssPresetEnv = require("postcss-preset-env");
const nesting = require('postcss-nested');
const prefixer = require('autoprefixer');

module.exports = {
  plugins: [
    pimport(),
    tailwindcss(),
    // postcssPresetEnv(),
    nesting(),
    prefixer(),
  ],
};
