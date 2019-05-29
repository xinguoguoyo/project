---
title: 笔记
---
     从2019-05-29开始，记录自己的测试生涯中遇到的问题以及学习进步的过程，丰富工作中的技能....


### 第一篇：git的搭建以及远程库的安装

``` bash
   centos下安装git:
                   'yun install curl-devel expat-devel gttext-devel'
                   'yun -y install git-core'
                   'git --version'  #查看版本
                   
   配置用户信息:
                   'git config --global uesr.name + <username> '
                   'git config --global user.email + <email>'
   
   查看配置信息:
                   'git config --list'
    
```

More info: [Writing](https://hexo.io/docs/writing.html)

### Run server

``` bash
$ hexo server
```

More info: [Server](https://hexo.io/docs/server.html)

### Generate static files

``` bash
$ hexo generate
```

More info: [Generating](https://hexo.io/docs/generating.html)

### Deploy to remote sites

``` bash
$ hexo deploy
```

More info: [Deployment](https://hexo.io/docs/deployment.html)
