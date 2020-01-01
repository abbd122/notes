### 启动`elasticsearch`准备

1.在`/etc/security/limits.conf`文件中添加:

```shell
es-user soft nofile 65536
es-user hard nofile 65536
es-user soft nproc 4048
es-user hard nproc 4096
```

2.修改最大进程数`sudo sysctl -w vm.max_map_count=262144`

> ```undefined
> max_map_count文件包含限制一个进程可以拥有的VMA(虚拟内存区域)的数量。虚拟内存区域是一个连续的虚拟地址空间区域。在进程的生命周期中，每当程序尝试在内存中映射文件，链接到共享内存段，或者分配堆空间的时候，这些区域将被创建。调优这个值将限制进程可拥有VMA的数量。限制一个进程拥有VMA的总数可能导致应用程序出错，因为当进程达到了VMA上线但又只能释放少量的内存给其他的内核进程使用时，操作系统会抛出内存不足的错误。如果你的操作系统在NORMAL区域仅占用少量的内存，那么调低这个值可以帮助释放内存给内核用。
> ```

### `elasticsearch`和`kibana`进行`docker`间通信

1.`elasticsearch`启动命令:

```shell
sudo docker run -e "discovery.type=single-node" -p 9200:9200 -p 5601:5601 --name myes + es镜像id
```

2.`kibana`启动命令:

```shell
sudo docker run -it --name mykibana --network=container:myes + kibana镜像 /bin/bash
```

> 进入容器内部执行3

3.修改`config/kibana.yml`配置:

```shell
# 增加
server.port: 5601
# 修改
server.host: "0.0.0.0"
elasticsearch.hosts: [ "http://127.0.0.1:9200" ]
```

4.后台运行`bin/kibana`:

```
nohup ./kibana &
```

> 成功启动后退出容器，目前没发现直接运行`kibana`容器的方法，每次都需要进入到容器内容运行后再退出容器

