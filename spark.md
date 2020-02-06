## 环境搭建

### `jdk`安装

1. 下载: `https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html`

2. 解压
3. `sudo apt-get install libc6-i386`

4. 测试: 切换到`jdk`的`bin`目录下，执行`./java -version`
5. 加入环境变量: `vim ~/.bashrc`, 添加

```shell
export JAVA_HOME=/home/wang/jdk1.8.0_241
export PATH=$JAVA_HOME/bin:$PATH
```

执行`source ~/.bashrc`

### `scala`安装

1. 下载: `wget https://downloads.lightbend.com/scala/2.13.1/scala-2.13.1.tgz`

2. 解压
3. 加入环境变量: `vim ~/.bashrc`，添加:

```shell
export SCALA_HOME=/home/wang/scala-2.13.1
export PATH=$SCALA_HOME/bin:$PATH
```

执行`source ~/.bashrc`

### `hadoop`安装

1. `apache`镜像地址找到`hadoop`最新版并下载: 

   `wget http://mirrors.hust.edu.cn/apache/hadoop/core/stable/hadoop-3.2.1.tar.gz `

2. 解压
3. 加入环境变量(同上)
4. 修改配置文件

```shell
# hadoop-env.sh文件中添加JAVA_HOME
export JAVA_HOME=/home/wang/jdk1.8.0_241

# core-site.xml文件
`06:30`
```

