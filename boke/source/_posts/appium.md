---
title: appium的环境搭建
---
---
    2019-05-30
### 第三篇:准备环境


``` bash
1.安装Node.js:
              访问 https://nodejs.org/en/download/，下载node.js，
              根据操作系统下载对应的安装包，这里选择Windows 64位的，
              下载完成直接安装，一路默认就行。
              安装完成后，会自动把路径加到环境变量中，在命令行中运行node -v，
              出现版本号表示安装正常。


2.安装JDK:
              地址：https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html，
              下载后安装默认路径安装，安装jdk的同时也会安装jre。
              
              
3.配置java环境变量:
              在环境变量中新建JAVA_HOME,对应变量值为jdk的安装目录，
              再加一个变量名为CLASSPATH，变量值为：%JAVA_HOME%\lib、tools.jar
              %JAVA_HOME%\lib\dt.jar
              在path系统变量中加两个路径：%JAVA_HOME%\bin;%JAVA_HOME%\jre\bin
              配置好变量后，打开命令行窗口，输入java_version，出现jdk的版本，表示配置成功。
              
              
4.安装Android SDK:
              Android  SDK是Google提供的Android开发工具包，在开发Android应用时会用到，
              需要通过引入工具包来调用Android的API，我们拿来的目的是为使用adb的相关密令，
              以及配置SDK来实现appium的调用。
              下载地址：http://tools.android-studio.org/index.php/sdk。
              选择installer_r24.4.1-windows.exe进行下载。
              
              
5.安装API版本和对应的工具包:
              进入SDK安装路径，打开SDK Manage.exe，选择需要的API版本和对应的工具包进行安装，
              SDK Tools 必须
              SDK Platform-tools 必须
              SDK Platform必须至少安装一个版本
              System Image建议安装
              Android Support建议安装
              SDK Samples建议安装
              安装完成后目录结构发生变化
              
              
              
6.SKD环境配置:
              新建环境变量ANDROID_HOME，变量值为sdk的安装路径，
              path下增加两个路径：%ANDROID_HOME%\platform-tools;%ANDROID_HOME%\tools
              环境配置好后，进入命令行窗口输入adb -version，出现信息表示安装成功。
              
              
              
7.安装python:
             下载地址：https://www.python.org/downloads/，
             可以选择Python2.7或者Python3.x版本，我这里选择的是Python2.7的版本。
             下载的是一个exe安装文件，下载完直接安装即可，我的安装目录是C:\Python27，
             安装好以后将Python安装目录配置到环境变量Path中，然后在cmd中运行python命令
             
             
             
             
8.安装appium:
            下载地址：https://github.com/appium/appium-desktop/releases，
            下载appium-desktop-Setup-1.5.0-ia32.exe安装包。
            双击进行安装，安装完成生成一个快捷图标，运行appium。
            
            
            
9.下载Appium-Python-Client:
            下载链接：https://pypi.python.org/pypi/Appium-Python-Client/,
            在命令行中运行pip install Appium-Python-Client
            安装完成后，进入python命令行环境，输入from appium import webdriver         
``` 