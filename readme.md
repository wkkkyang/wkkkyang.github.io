>   关于主题

放置在`node_modules`文件夹中和`themes`文件夹中都是一样的！

`主题中的source`文件夹和`博客中的source`文件夹中的资源会融合到一块，并***优先***使用`博客中的source`文件夹的资源

>   关于hexo新建文章或其他菜单栏

~~~shell
新建文章，会放置在source/_post文件夹
hexo new [post/page] <title>
hexo new [post] "HelloWorld"
post:文章
page:自定义页面

自定义页面,会在source下生成一个about文件夹和index.md,如果是about页面，文章中的头部设置中的layout: about
hexo new page about

自定义页面,会在source下生成一个test文件夹和index.md
hexo new page test

~~~

参考：[hexo指令](https://hexo.io/zh-cn/docs/commands)
参考：[fluid配置指南](https://hexo.fluid-dev.com/docs/guide/#%E6%87%92%E5%8A%A0%E8%BD%BD)
