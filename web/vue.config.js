module.exports = {
        publicPath: './', //本地路径
        configureWebpack: {
            resolve: {
                alias: {
                    'assets': '@/assets',
                    'components': '@/components',
                    'views': '@/views',
                }
            }
        },
    };