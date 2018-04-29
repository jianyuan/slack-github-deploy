const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    mode: 'development',
    context: __dirname,
    entry: './slack_github_deploy/assets/js/index',
    output: {
        path: path.resolve('./slack_github_deploy/assets/bundles/'),
        filename: '[name]-[hash].js'
    },
    plugins: [
        new BundleTracker({filename: './webpack-stats.json'})
    ],
    module: {
        rules: [
            {
                test: /\.jsx?$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['es2015', 'react'],
                    },
                },
            },
        ],
    },
    resolve: {
        modules: ['node_modules'],
        extensions: ['.js', '.jsx'],
    },
};
