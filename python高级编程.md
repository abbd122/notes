### `jupyter`使用

#### 安装

```shell
pip install notebook
```

#### 使用

```shell
ipython notebook
```

### 魔法函数

#### `__str__`和`__repr__`

```python
class Company:
    def __init__(self, employee_list):
        self.employee = employee_list
        
    def __str__(self):
        return 'str:' + ','.join(self.employee)
    
    def __repr__(self):
        return 'repr:' + ','.join(self.employee)
    
company = Company(['tom', 'bob', 'jane'])
print(company)
company

# 结果
str:tom,bob,jane
repr:tom,bob,jane
```

> print会调用`__str__`，解释器会默认调用`__repr__`，也就是`company = company.__repr__()`

#### `__add__`

```python
class MyVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other_instance):
        result = MyVector(self.x + other_instance.x, self.y + other_instance.y)
        return result
    
    def __repr__(self):
        return 'MyVector({},{})'.format(self.x, self.y)
    
myvector_1 = MyVector(1, 2)
myvector_2 = MyVector(3, 4)
result = myvector_1 + myvector_2
print(result)

# 结果
MyVector(4,6)
```

#### `__mro__`

> 查看类的继承顺序

```python
class D:
    pass

class C(D):
    pass

class B(D):
    pass

class A(B, C):
    pass

print(A.__mro__)

# 结果
(<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class 'object'>)
```

#### `__enter__`和`__exit__`

```python
class Sample:
    
    def __enter__(self):
        print('enter')
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
        
    def do_something(self):
        print('do something')
        
with Sample() as s:
    s.do_something()
    
# 结果
enter
do something
exit
```



### 鸭子模型

```python
class Cat:
    def say(self):
        print('I am a Cat')
        
class Dog:
    def say(self):
        print('I am a Dog')
        
class Duck:
    def say(self):
        print('I am a Duck')
        
animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()
 
# 结果
I am a Cat
I am a Dog
I am a Duck
```

> 例如: python中的可迭代对象，类型可以有list, tuple等很多，只要实现了`__getitem__`等方法就都能够被迭代，这就使用了鸭子模型

### 抽象基类

> 一般定义一个抽象基类，用于规定继承的类中必须实现某些方法，否则会抛出异常

```python
import abc

class CacheBase(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod  # 抽象方法
    def get(self, key):
        pass
    
    @abc.abstractmethod
    def set(self, key, value):
        pass
    
class RedisCache(CacheBase):
    pass

redis_cache = RedisCache()

# 结果
TypeError: Can't instantiate abstract class RedisCache with abstract methods get, set
```

> `collections.abc`有很多`python `内置的抽象基类，抽象基类只是帮助理解`python`的类继承，不推荐使用抽象基类

### `type`和`isinstance`

> `isinstance`会将继承链考虑在内，而`type`是判断是否指向同一个对象id，要尽量使用`isinstance`

```python
class A:
    pass

class B(A):
    pass

b = B()

isinstance(b, A)  # True
type(b) is A  # False
```

### 访问`python`的私有属性

```python
user = User()
print(user._User__birthday)
```

> 通过 `实例._classname__attr`来访问私有属性
>
> `dir()`能够列出对象的所有属性

### `contextlib`简化实现上下文管理器

```python
import contextlib

@contextlib.contextmanager
def file_open(file_path):
    print('before yield')
    yield
    print('after yield')
    
with file_open('a.txt'):
    print('file_start')
    
# 结果
before yield
file_start
after yield
```

### 可切片对象

```python
import numbers

class Group:
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        pass

    def __getitem__(self, item):
        cls = type(self)  # 当前实例的类
        if isinstance(item, slice):
            return cls(self.group_name, self.company_name, self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(self.group_name, self.company_name, [self.staffs[item]])

    def __len__(self):
        pass

    def __iter__(self):
        pass

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False

    def __repr__(self):
        return '<Group({},{},{})>'.format(self.group_name, self.company_name, self.staffs)


staffs = ['bobby1', 'bobby2']
group = Group(group_name='haha', company_name='华为', staffs=staffs)
ret = group[:1]
print(ret)

```

> 实现`__getitem__`可切片， 其中`type(self)`可以用来获得当前实例的类对象

### `bisect`处理已排序序列

> `bisect`使用二分查找法，效率很高

#### `insort`

> 插入数据自动排序

```python
import bisect

inter_list = []
bisect.insort(inter_list, 2)
bisect.insort(inter_list, 10)
bisect.insort(inter_list, 0)
print(inter_list)
# 结果
[0, 2, 10]
```

#### `bisect_right()`和`bisect_left()`

> 当序列中有重复数据时，插入到之前还是之后

```python
import bisect

inter_list = [0, 1, 2, 10]
ret = bisect.bisect(inter_list, 2)  # bisect即bisect_right
print(ret)

# 结果
3
```

### `array`

> 存放指定类型的数组，用`C`语言实现，效率很高

```python
import array
my_arr = array.array('i')
for i in range(100000):
    my_arr.append(i)
```

### 列表生成式、生成器表达式

> 1.列表生成式性能高于列表操作
>
> 2.尽量使用推导式和生成器表达式

### 垃圾回收

> 1. python中垃圾回收的算法是采用引用计数，当目标引用计数为0时，会默认启动垃圾回收
> 2. del 语句并不是删除目标，而是将其引用计数-1

```python
a = object()
b = a
del a
print(b)  # <object object at 0x7f39417ef0a0>
print(a)  # 报错
```



# 元类编程

## `property`动态属性

![](/home/wangzheng/文档/notes/image/python property动态属性.png)

## `__getattr__`和`__getattribute__`魔法函数

- `__getattr__`在查找不到属性的时候调用

![](/home/wangzheng/文档/notes/image/__getattr__.png)

- `__getattribute__`：查找属性就会调用此函数，在`__getattr__`之前

![](/home/wangzheng/文档/notes/image/__getattribute__.png)

## `__get__`, `__set__`, `__delete__`属性描述符

> 1. 只要实现了其中的任何一个，就是属性描述符
> 2. 可以约束属性赋值的类型

### 创建属性描述符

![](/home/wangzheng/文档/notes/image/创建属性描述符.png)

### 使用

![](/home/wangzheng/文档/notes/image/使用属性描述符1.png)

![](/home/wangzheng/文档/notes/image/使用属性描述符2.png)

### 数据描述符

> 实现`__get__`和`__set__`

![](/home/wangzheng/文档/notes/image/数据描述符.png)

### 非数据描述符

> 只实现了`__get__`

![](/home/wangzheng/文档/notes/image/非数据描述符.png)

### 属性查找顺序

![](/home/wangzheng/文档/notes/image/属性查找顺序.png)



## `__new__`和`__init__`区别

> 如果`__new__`方法不返回，则不会调用`__init__`



## 自定义元类

> 元类是创建类的类

### `type`动态创建类

> 参数1：类名， 参数2：所继承的基类， 参数3：属性方法

![](/home/wangzheng/文档/notes/image/type动态创建类.png)

### `metaclass`

![](/home/wangzheng/文档/notes/image/metaclass元类.png)



## 元类实现`ORM`

### 需求

![](/home/wangzheng/文档/notes/image/ORM.png)

### 初始化数据描述符

![](/home/wangzheng/文档/notes/image/IntField数据描述符.png)

增加验证逻辑

![](/home/wangzheng/文档/notes/image/IntField增加验证逻辑.png)

增加`db_column`参数

![](/home/wangzheng/文档/notes/image/db_column参数.png)

`__set__`增加验证逻辑

![](/home/wangzheng/文档/notes/image/__set__增加验证逻辑.png)

### 使用元类注入属性

![](/home/wangzheng/文档/notes/image/元类注入属性.png)

> `name`参数代表上述字段的数据描述符的类名，如果未定义`Meta.db_table`，则表名默认为类名小写

### 定义`BaseModel`

![](/home/wangzheng/文档/notes/image/定义BaseModel_1.png)

![](/home/wangzheng/文档/notes/image/定义BaseModel_2.png)



# 迭代器和生成器

## 迭代协议

> 1. 迭代器是访问集合内元素的一种方式，一般用来遍历数据
> 2. 迭代器和以下标访问的方式不一样，迭代器是不能返回的，提供了一种惰性数据的访问方式
> 3. 查看迭代器实现了哪些方法: `from collections.abc import Iterator`，`Iterator`就是迭代器
> 4. 可迭代类型和迭代器是不同的，只要实现了`__iter__`就是可迭代类型，而迭代器还必须要实现一个`__next__`方法

![](/home/wangzheng/文档/notes/image/Iterable 和 Iterator.png)

> `Iterable`代表可迭代类型，`Iterator`代表迭代器

## 迭代器和可迭代对象的区别

![](/home/wangzheng/文档/notes/image/iter_rator.png)

> 通过`iter()`生成迭代器

### `for`的实现

> 通过不断调用`next`来实现，`for`语句会监听`StopIteration`异常来停止

![](/home/wangzheng/文档/notes/image/迭代器实现原理.png)

### 自定义迭代器

![](/home/wangzheng/文档/notes/image/自定义迭代器.png)

> `for`语句可以处理`StopIteration`，但处理不了`IndexError`，所以要监听`IndexError`并抛出`StopIteration`

## 生成器函数

### `yield`模拟斐波那契数列

![](/home/wangzheng/文档/notes/image/yield.png)

## 生成器原理

![](/home/wangzheng/文档/notes/image/函数调用过程.png)

> 1. `python.exe`会用一个叫做`PyEval_EvalFramEx(C语言函数)`去执行`python`中的函数，首先会创建一个栈帧(`stack frame`)，相当于一个上下文
> 2. 堆内存不会自动释放，因此栈帧可以独立存在

![](/home/wangzheng/文档/notes/image/生成器原理.png)

> 1. 生成器是在代码的字节码(`PyFrameObject`和`PyCodeObject`)上又封装了一层(`PyGenObject`)
> 2. 变量保存在最近一次调用的位置，因栈帧可以独立存在，所以每次调用生成器就重新生成了一个当前函数执行位置的栈帧上下文

![](/home/wangzheng/文档/notes/image/gi_frame.png)

进行`next`调用

![](/home/wangzheng/文档/notes/image/进行next调用.png)



## 读取大文件

> 按大小读取文件，以指定分隔符作为标记`yield`

![](/home/wangzheng/文档/notes/image/生成器读取大文件.png)



# `Socket`编程

![](/home/wangzheng/文档/notes/image/五层常用网络模型.png)

> `Socket`是操作系统提供的能和`TCP/UDP`协议打交道的工具，可以用来实现基于`TCP/UDP`协议的上层协议工具，如聊天协议

## `client`和`server`通信

![](/home/wangzheng/文档/notes/image/Socket编程.png)

### `Server`

![](/home/wangzheng/文档/notes/image/Server端.png)

### `Client`

![](/home/wangzheng/文档/notes/image/Client端.png)

## 实现聊天功能

![](/home/wangzheng/文档/notes/image/多线程socket.png)

## `Socket`模拟`HTTP`请求

> `request`基于`urlib`，`urlib`基于`socket`

![](/home/wangzheng/文档/notes/image/socket处理http请求.png)

去掉请求头部信息

![](/home/wangzheng/文档/notes/image/去掉头部信息.png)



# 多线程、多进程和线程池

## `GIL`

> 全局解释器锁
>
> 1. `python`一个线程对应`c`语言一个线程
> 2. `gil`使得同一时刻只有一个线程在一个`cpu`上执行字节码，无法将多个线程映射到多个`cpu`上执行

`python`中查看字节码

![](/home/wangzheng/文档/notes/image/dis字节码.png)

### `gil`是会释放的(并不绝对安全)

> 1. 会根据执行的字节码行数以及时间片释放`gil`
> 2. 会在遇到`io`操作的时候主动释放

![](/home/wangzheng/文档/notes/image/gil释放的情况.png)

## 多线程编程

> 对于`io`来说，多线程和多进程性能差别不大

### `pycharm`在`debug`中查看线程

![](/home/wangzheng/文档/notes/image/debug查看线程.png)

### `setDaemon`: 主线程退出，子线程kill掉

![](/home/wangzheng/文档/notes/image/setDaemon.png)

### `join`: 等待子线程执行完成，主线程才会继续往下执行

![](/home/wangzheng/文档/notes/image/join.png)

> 在此期间，线程是并行运行的，并不是顺序运行的

### `Thread`通过继承来简化代码

![](/home/wangzheng/文档/notes/image/Thread.png)

## 线程间通信

### `queue`进行线程间同步

> 1. `queue`是线程安全的，因为内部实现使用双端队列`deque`，而`deque`本身是线程安全的
> 2. 线程间通信用`queue`来代替`list`或`set`

![](/home/wangzheng/文档/notes/image/queue.png)

- 其他常用方法: 

1. `qsize`: 获得队列的长度

2. `empty`: 队列是否为空
3. `full`: 队列是否已满
4. `get`, `put`: 获取、存储数据，默认`block=True`阻塞，会等待获取(或存储)结束才执行下一步
5. `put_nowait`, `get_nowait`: 操作时不等待，异步执行
6. `join`, `task_done`: 队列阻塞，知道接收到`task_done`指令才退出

![](/home/wangzheng/文档/notes/image/join&task_done.png)

## 线程同步

### `threading.Lock`

![](/home/wangzheng/文档/notes/image/threading.Lock.png)

### `threading.RLock`

> 可重入的锁
>
> - 在同一个线程里面，可以连续调用多次`aquire`，一定注意`aquire`和`release`的次数要相等

![](/home/wangzheng/文档/notes/image/threading.RLock.png)

### `threading.Condition`

> 条件变量，用于复杂的线程间同步

#### `wait` & `notify`

> `condition`有两层锁，一把底层锁会在线程调用了`wait`方法的时候释放，上面的锁会在每次调用`wait`的时候分配一把并放入到`condition`的等待队列中，等待`nodify`方法的唤醒

![](/home/wangzheng/文档/notes/image/threading.Condition.png)

![](/home/wangzheng/文档/notes/image/wait&notify.png)

### `threading.Semaphore`

> 信号量，用于控制进入数量的锁

![](/home/wangzheng/文档/notes/image/threading.Semaphore.png)

## `concurrent.futures`线程池

> 1. 兼顾Semaphore(控制执行数量)的功能和自动执行`start`功能
> 2. 主线程中可以获取某一个线程的状态或某一个任务的状态，以及返回值
> 3. 可以让多线程和多进程编码接口一致

### `ThreadPoolExecutor`

![](/home/wangzheng/文档/notes/image/ThreadPoolExecutor.png)

![](/home/wangzheng/文档/notes/image/dong&result&cancel.png)

> `submit`: 立即返回，非阻塞
>
> `done`: 判定该线程是否执行成功，此时为False
>
> `result`: 得到执行的返回结果
>
> `cancel`: 取消掉某个任务，注意：执行中或执行完成的任务取消不掉

### `concurrent.futures.as_completed`

> 1. 获取已经成功的`task`的返回值
>
> 2. 返回顺序: 谁先完成返回谁

`from concurrent.futures import as_completed`

![](/home/wangzheng/文档/notes/image/as_completed.png)

### `ThreadPoolExecutor.map`

> 1. 获取已经成功的`task`返回值
> 2. 返回顺序: 和传入的参数数组顺序一致

`executor = ThreadPoolExecutor(max_works=2)`

![](/home/wangzheng/文档/notes/image/ThreadPoolExecutor.map.png)

### `concurrent.futures.wait`

> - 使主线程阻塞，作用: 指定某一些`task`执行完成才继续往下执行
>
> `return_when`: 当什么时候不用等待
>
> `FIRST_COMPLETED`: `from concurrent.futures import FIRST_COMPLETED`，当第一个线程执行完返回

![](/home/wangzheng/文档/notes/image/concurrent.futures.wait.png)

### 多线程、多进程特点

> 1. 耗`cpu`的操作使用多进程(计算，如数学计算、图形处理)，`io`操作使用多线程，因为进程切换代价高于线程
> 2. 对于操作系统来说，开60个线程很轻松，但开60个进程很吃力

#### `with ThreadPoolExecutor`

![](/home/wangzheng/文档/notes/image/ThreadPoolExecutor with.png)

#### `with ProcessPoolExecutor`

![](/home/wangzheng/文档/notes/image/ProcessPoolExecutor with.png)

### `multiprocessing`多进程编程

![](/home/wangzheng/文档/notes/image/multiprocessing.png)

#### 进程池

![](/home/wangzheng/文档/notes/image/multiprocessing.Pool.png)

- `imap`

![](/home/wangzheng/文档/notes/image/Pool.imap.png)

## 进程间通信

> 1. 多进程不能使用`queue.Queue`，而要使用`multiprocessing.Queue`
>
> 2. 共享全局变量不适用于多进程，相互独立

![](/home/wangzheng/文档/notes/image/multiprocessing.Queue.png)

### `Manager().Queue`进程池间通信

>  `multiprocessing.Queue`不能用于`Pool`进程池

![](/home/wangzheng/文档/notes/image/Manager.queue.png)

### `Pipe`通信

> 1. `pipe`只能适用于两个进程间通信
> 2. `pipe`的性能高于`queue`，在只有两个子进程时可以使用

![](/home/wangzheng/文档/notes/image/Pipe.png)

### `Manager.dict()`

![](/home/wangzheng/文档/notes/image/Manager.dct.png)



# 协程和异步`io`

## 并发、并行、同步、异步、阻塞、非阻塞

![](/home/wangzheng/文档/notes/image/并发、并行.png)

![](/home/wangzheng/文档/notes/image/同步、异步.png)

![](/home/wangzheng/文档/notes/image/阻塞、非阻塞.png)

> 同步、异步是消息间的一种通信方式，阻塞和非阻塞是函数调用的一种机制

## `C10k`问题和`io`多路复用

![](/home/wangzheng/文档/notes/image/io.png)

### `I/O`复用

![](/home/wangzheng/文档/notes/image/io复用.png)

> 1. `select`可以同时监听多个`socket`的状态，而while循环只能监听一个

### 异步`I/O`

> 目前很多高并发框架并没有使用`aio`异步，仅仅使用了`I/O`多路复用

![](/home/wangzheng/文档/notes/image/异步io.png)

### `select`, `poll`, `epoll`

![](/home/wangzheng/文档/notes/image/select、poll、epoll.png)

> `epoll`并不代表一定比`select`好
>
> - 在并发高的情况下，连接活跃度不是很高，`epoll`比`select`好
> - 并发性不高，同时连接很活跃(例如游戏连接，连接后不会断掉)，`select`比`epoll`好

## `select`+回调+事件循环

### `DefaultSelector`

`from selector import DefaultSelector`

