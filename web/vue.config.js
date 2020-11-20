const config = {
  lintOnSave: false,
  configureWebpack: {
      resolve: {
          alias: {
              'assets': '@/assets',
              'components': '@/components',
              'network': '@/network',
              'views': '@/views'
          }
      }
  }
}

exports ;
