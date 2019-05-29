---
title: 笔记
---
     从2019-05-29开始，记录自己的测试生涯中遇到的问题以及学习进步的过程，丰富工作中的技能....


### 第一篇：git的搭建以及远程库的安装

``` bash
   centos下安装git:
                   'yun install curl-devel expat-devel gttext-devel'
                   'yun -y install git-core'
                   'git --version'  
                   #安装git和查看版本
                   
   配置用户信息:
                   'git config --global uesr.name + <username> '
                   'git config --global user.email + <email>'
                   #配置用户名及邮箱
   
   查看配置信息:
                   'git config --list'
    
   
   
   
   git服务器的搭建:
                   'groupadd git' 
                   'useradd git -g git'
                   #创建用户组
                   'cd /git的安装目录下'
                   'mkdir <directory>.ssh'
                   'chmod 755 <directory>.ssh'
                   'touch <directory>.ssh/authorized_keys'
                   'chmod 644 <directory>.ssh/authorized_keys'
                   #创建目录并赋予权限，在目录下创建keys，并对keys赋予权限
                   'cd /home'
                   'mkdir <directory>'
                   'chown git:git <directory>'
                   'cd <directoyr>'
                   'git init --bare name.git'
                   'chown -R git:git name.git'
                   'git clone git@localhos：/home/<directory>/name.git
                   #创建仓库所在目录，并创建一个git的空库，把仓库的所属用户改为git,再克隆一个库
                  
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
