title:Hexo博客部署
---

    从2019-05-29开始，记录...
### 第二篇:Hexo

``` bash
  安装部署前提：  
              需要Node.js以及git
              安装node.js：curl https://raw.github.com/creationix/nvm/v0.33.11/insatll.sh | sh
              Wget -qo-  https://raw.github.com/creationix/nvm/v0.33.11/insatll.sh | sh
              重启终端执行：nvm install stable
              nvm是为了使用npm的命令
  
  安装hexo：
              npm install -g hexo-cli  安装hexo
              hexo init “mulu”      创建hexo目录
              cd “mlul”            进入hexo安装目录
              npm install          安装npm
              Npm install hexo-server --save   把hexo服务存在服务器
              Hexo s -p 端口号     
              启动服务指定端口号，默认的4000可能被占用，推荐修改，localhost为你的服务器ip
  
  生成器：
              Hexo generate
              Hexo能够监视文件的变动并立即重新生成静态文件，生成是比对SHA1 checksum，只有变动的文件才会写入
              Hexo generate --watch
              完成部署后输入命令自动比对
              Hexo g -d或者hexo d -g
  
  
  如何将hexo部署到git上
             cd hexo 的安装目录下
             vi编辑配置_config.yml的配置信息在deploy下配置type为git，配置repo为git远程的URL，
             配置branch所在的分支，然后再github把远程库的默认分支改为branch配置的分支，
             配置完成执行hexo clean && hexo deploy，
             前者清除站点文件，后者将站点文件推送到指定库的分支下
                   
                    
``` 


