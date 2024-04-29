```shell
git add . & git commit -m "update" & git push
```

>   关于主题

放置在`node_modules`文件夹中而不是`themes`文件夹

>   关于hexo新建文章或其他菜单栏

~~~shell
新建文章，会放置在source文件夹
hexo new "HelloWorld"

新建about等菜单栏页面
hexo new page --path about（这样会创建一个index.html页面）
hexo new page --path about/me

在theme的config配置文件中修改相应的配置
~~~

参考：[hexo指令](https://hexo.io/zh-cn/docs/commands)
参考：[fluid配置指南](https://hexo.fluid-dev.com/docs/guide/#%E6%87%92%E5%8A%A0%E8%BD%BD)
