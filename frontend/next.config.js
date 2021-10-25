/** @type {import('next').NextConfig} */
const path = require("path");

module.exports = {
  reactStrictMode: true,
  assetPrefix: process.env.BASEPATH || "",
  publicRuntimeConfig: {
    basePath: process.env.BASEPATH || ""
  },
  webpack(config, options) {
    config.resolve.alias["@component"] = path.join(
      __dirname,
      "src",
      "component"
    );
    config.resolve.alias["@libs"] = path.join(__dirname, "src", "libs");
    config.resolve.alias["@components"] = path.join(__dirname, "src", "components")
    config.resolve.alias["@hooks"] = path.join(__dirname, "src", "hooks")
    return config;
  },
}