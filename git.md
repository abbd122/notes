### 分支

#### 新建分支

```shell
git checkout -b branchname
```

> 新建并切换到分支

#### 查看分支

```shell
查看本地
git branch

查看全部
git branch -a
```

#### 切换分支

```shell
git checkout branchname
```

#### 推送至远程

```shell
git push origin branchname
```

#### 删除分支

```shell
删除本地
git branch -d branchname

删除远程
git push origin --delete branchname
```

#### 合并分支

```shell
1.切换到master
git checkout master

2.将远程分支合并到本地master
git merge origin/index-swiper

3.推送master
git push
```

#### 版本回退

```shell
git reset --hard + 版本号
```

### 本地初始化 --> 远程

1. 初始化

```shell
git init .
```

2. 提交暂存区

```shell
git add .
git commit -m 'xxx'
```

3. 提交至远程

```shell
git remote add origin git@github.com:abbd122/ArticleSpider.git
git push -u origin master
```

