---
title: git的搭建以及远程库的安装
---
---
    

### 第一篇

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
                   
                   
   这里会遇到一个问题:
                    当你执行克隆仓库时会提示你需要仓库的密码，这里的密码是设置的用户组的密码，
                    初始密码不知道，所以需要执行命令来更改密码：
                    'sudo passwd git'
                    #更改git的密码
                    更改完密码后，执行克隆命令会发现报错，报错已存在当前目录，
                    我们需要rm -rf删除先前克隆的目录，再执行克隆密令，这时候就成功，git服务器搭建完成
                    
                    
   github远程库的链接:
                    首先获取密钥:'ssh-keygen -t rsa -C <youremail@examlp.com>'
                    #此处的email是注册git的email
                    密令执行完毕后，会提示你生成文件需要的的操作，一直默认回车就好
                    注意会在root下面生成隐藏的密钥文件，需要vi到文件内获取复制ssh密钥的keys
                    文件存放的路径会在提示操作的时候生成
                    'vi /root/.ssh/id_rsa.pub/' 复制文件的key（查看公钥cat ~/.ssh/id_rsa.pub）
                    回到github上，进入Account里面打开settings 把SSH keys粘贴上
                    这时候远程仓库就建立成功了
                    'ssh -T git@github.com'
                    #验证链接是否成功
        
        
   创建第一个commit:
                   push文件代码到github上
                   'echo “#内容” >> README.md'  #直接创建文件并书写内容
                   'git init'  #初始化
                   'git add README.md'  #添加文件
                   'git commit -m “备注”'  #提交文件并备注
                   'git remote add origin git@github.com:yourusername/yourmulu.git' 
                   #这里可能存在一个问题就是发现你的远程来源已经存在，所以你需要干掉他
                   'git remote rm origin'  #干掉origin再执行上条命令
                   'git push -u origin master'  
                   #把origin  push到master  
                   
                    
``` 



