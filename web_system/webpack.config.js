const clientConfig = {
    target : 'web',
    entry  : './src/index.js',
    mode   : 'production',

    output : { filename : 'bundle-front.js' },
    
    module : {
        rules: [
            {
                test    : /\.(js|jsx)$/,
                exclude : /node_modules/,
                use : { loader : 'babel-loader' }
            },

            {
                test : /\.css$/i,
                use  : ['style-loader', 'css-loader']
            },

            {
                test : /\.svg$/,
                use  : { loader : 'svg-inline-loader' }
            },

            {
                test : /\.(png|jpe?g|gif)$/i,
                use  : { loader : 'file-loader' }
            }
        ]
    }
}

module.exports = [clientConfig]
