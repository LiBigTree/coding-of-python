# python基础学习手册

记录我学习Python的路，不断修改，一方面是作为未来遗忘时的参考；另一方面给看到的人一个学习的参考。

## 零、编程与生活

首先，我们将生活中所有的问题称之为数据，那么理工科的研究在我看来便是研究不同数据的流通——数据本身或者数据之外。而编程之于解决现实问题，便是对数据的高级操作，将外界的数据以“规范”的形式输入计算机进行处理。这一点的理解有什么用呢？在学习庞杂的知识时，数据线便是我把握知识主干的脉络，在此基础上不断丰富知识库，锻炼逻辑思维能力。

回到Python语言本身，将基础知识打碎重组，有了下面内容。

## 一、Python中数据是如何组织起来的

### 字符串、数值

### 列表

#### 索引

推导式

#### 方法

### 元组

#### 索引

#### 方法

#### 生成器表达式

语法类似与列表推导式，外层为圆括号。

```python
# 生成器表达式
print("使用生成器表达式：", sum(i*i for i in range(10)))
```

### 字典

#### 索引

#### 方法

### 函数

#### 最简单的定义与调用

定义函数

```python
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()  # 空行
```

调用函数

```python
if __name__ == '__main__':
    fib(100)
```

#### 关于调用

定义：

```python
# 对一个或多个参数指定默认值
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
```

调用：

```python
if __name__ == '__main__':
    # ask_ok函数的调用方法
    # ask_ok('Do you really want to quit?')  # 只给出必需的参数
    # ask_ok('OK to overwrite the file?', 2)  # 给出一个可选的参数
    ask_ok('OK to overwrite the file?', 2, reminder='Come on, only yes or no!')  # 给出所有的参数
```

**默认值是在函数定义处计算的**

```
i = 5


def f(arg=i):
    print(arg)
    
i = 6
f()
```

**默认值只会执行一次**

```python
def f2(a, one=[]):
    # 测试默认值执行的次数
    one.append(a)
    return one


def f3(a, eli_one=None):
    if eli_one is None:
        eli_one = []
    eli_one.append(a)
    return eli_one


if __name__ == '__main__': 
   # 测试默认值参数调用次数
    print(f2(1))
    print(f2(2))
    print(f2(3))

    print(f3(1))
    print(f3(2))
    print(f3(3))
    
运行结果：    
[1]
[1, 2]
[1, 2, 3]
[1]
[2]
[3]
```

#### 关键字参数

关键字参数跟随在位置参数的后面

```python
def parrot(voltage, state='a stiff', action='vcom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    
    
if __name__ == '__main__':     
    # 关键字参数的学习
    parrot(1000)  # 1 positional argument
    print()
    parrot(voltage=2000)  # 1 keyword argument
    print()
    parrot(voltage=1000, action='VOOOOOM')  # 2 keyword arguments
    print()
    parrot(action='VOOOOOM', voltage=1000) # 2 keyword arguments
    print()
    parrot('a million', 'bereft of life', 'jump')  # 3 positional arguments
    print()
    parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
    
结果：
-- This parrot wouldn't vcom if you put 1000 volts through it.
-- Lovely plumage, the Norwegian Blue
-- It's a stiff !

-- This parrot wouldn't vcom if you put 2000 volts through it.
-- Lovely plumage, the Norwegian Blue
-- It's a stiff !

-- This parrot wouldn't VOOOOOM if you put 1000 volts through it.
-- Lovely plumage, the Norwegian Blue
-- It's a stiff !

-- This parrot wouldn't VOOOOOM if you put 1000 volts through it.
-- Lovely plumage, the Norwegian Blue
-- It's a stiff !

-- This parrot wouldn't jump if you put a million volts through it.
-- Lovely plumage, the Norwegian Blue
-- It's bereft of life !

-- This parrot wouldn't vcom if you put a thousand volts through it.
-- Lovely plumage, the Norwegian Blue
-- It's pushing up the daisies !


```

剩余的形参中，位置参数用*收集，关键字参数用**收集。

```python
def cheese_shop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
        
if __name__ == '__main__':
    # 剩余参数的收集
    cheese_shop("Limburger", "It's very runny, sir.",
                "It's really very, VERY runny, sir.",
                shopkeep="Michael Pallin",
                client="John Cleese",
                sketch="Cheese Shop Sketch")
结果：
-- Do you have any Limburger ?
-- I'm sorry, we're all out of Limburger
It's very runny, sir.
It's really very, VERY runny, sir.
----------------------------------------
shopkeep : Michael Pallin
client : John Cleese
sketch : Cheese Shop Sketch
```

#### 限制参数调用方式

正斜杠之前放置限制位置参数，*之后仅限关键字参数，二者之间随意

```python
def standard_arg(arg):
    print(arg)


def pos_only_arg(arg, /):
    print(arg)


def kwd_only_arg(*, arg):
    print(arg)


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


if __name__ == '__main__':
    # 不同调用方式比对
    standard_arg(2)
    pos_only_arg(1)  # 希望形参名称对用户不可用时使用、对API，防止形参名称修改时造成破坏性的API变动
    kwd_only_arg(arg=2)  # 形参有实际意义、防止过度依赖传入参数的位置时
    combined_example(1, 2, kwd_only=3)
```

**使用仅限位置参数，对API，可以防止形参名称被修改时造成的破坏性的API变动**

**当然，若形参有实际意义、防止过度依赖传入参数的位置时，使用仅限关键字参数

### 解包参数列表

调用函数时用，解析参数传递

```python
def unpack_para():
    args = [3, 6]
    show = list(range(*args))
    print(show)
    
if __name__ == '__main__':
    # 将元组里的参数**解包**分别传递给调用的函数
    unpack_para()
```

### lambda表达式

两个作用：一是返回一个函数；二是传递一个小函数作为参数

```python
def lambda_test(n):
    return lambda x: x + n
    
if __name__ == '__main__':    
    f = lambda_test(42)
    print(f(8))
```

```python
def transport():
    pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    pairs.sort(key=lambda pair: pair[1])
    print(pairs)

    
if __name__ == '__main__':
    # 传递小函数作为参数
    transport()
```



### 类

#### 理解命名空间和作用域

* 命名空间：名字到对象的映射
* 作用域：一个命名空间可直接访问的python程序的文本区域

global：将变量关联到全局作用域

```
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("after local: ", spam)
    do_nonlocal()
    print("after nonlocal: ", spam)
    do_global()
    print("after global: ", spam)


if __name__ == '__main__':
    # 理解作用域与命名空间，一个命名空间下的多个作用域
    scope_test()
    print("In global scope: ", spam)
```

#### 类和实例：属性引用

（1）类的属性引用

* 属性引用：返回内容或者函数对象

```python
class MyClass:
    """A simple class"""
    i = 12345

    def f(self):
        return 'hello world'


if __name__ == '__main__':
    # 属性引用
    # MyClass.i = 'changed' 类的属性可以被赋值，可以通过赋值来更改值
    print(MyClass.i)  # 返回一个整数
    print(MyClass.__doc__)
    print(MyClass.f)  # 返回一个函数对象
```

（2）实例的属性引用

> 可以视之为不带参数的函数，常常包含一个名为```__init__()```的特殊方法

self即是类本身，初始化方法的使用：

```python
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


if __name__ == '__main__':
    # 实例化2
    x2 = Complex(3.0, -4.5)
    print('实数部分：%.1f；虚数部分：%.1f' % (x2.r, x2.i))
```

* ##### 数据属性

  赋值时产生，实例化时的专有名词，对应类时的变量

```python
    # 实例化的属性引用: 数据属性
    x.counter = 1
    while x < 10:
        x.counter = x.counter * 2
    print(x.counter)

    del x.counter
```



* ##### 方法

类的属性引用叫做函数对象>>>实例化之后的引用叫做方法

方法可以在绑定后被立即调用，也可以被保存起来以后再调用

```python
    # 方法 类的属性引用叫做函数对象 实例化之后的引用叫做方法
    xf = x.f # 注意这里！！！ x.f:绑定，不立即调用； x.f():绑定后立即调用
    print(xf())
```

方法：实例对象会作为函数的第一个参数被传入，调用```x.f() ```相当于```MyClass.f(x)```

#### 类和实例中的“变量”

实例中的实例变量是**每个实例的唯一数据**，类中的变量是**所有实例共享的属性和方法**。

```python
class Dog:
    kind = 'canine'  # class variable shared by all instance

    def __init__(self, name):
        self.name = name  # instance variable unique to each variable


if __name__ == '__main__':
    # 类和实例变量
    d = Dog('Fido')
    e = Dog('Buddy')
    print("=== shared by all variable ===")
    print(d.kind)
    print(e.kind)
    print("=== unique by each variable ===")
    print(d.name)
    print(e.name)

```

！注意：类中的变量会共享给所有实例，要想使得某个变量被独享，应该放在初始化方法中

**反例: **

属性引用被映射到了公共区域，若是想要独享，只要映射在实例特有区域便可

```python
class Dog:
    kind = 'canine'  # class variable shared by all instance

    tricks = []

    def __init__(self, name):
        self.name = name  # instance variable unique to each variable

    def add_tricks(self, trick):
        self.tricks.append(trick)


class Dog2:

    def __init__(self, name):
        self.name = name  # instance variable unique to each variable
        self.tricks = []

    def add_tricks(self, trick):
        self.tricks.append(trick)


if __name__ == '__main__':
    # 共享范围对比
    print("=== 这是放在类的共享区域里： ===")
    d = Dog('Fido')
    e = Dog('Buddy')
    d.add_tricks('roll over')  
    e.add_tricks('play dead')
    print(d.tricks)

    print("=== 这是利用初始化，为每个实例创建的空间： ===")
    d2 = Dog2('Fido')
    e2 = Dog2('Buddy')
    d2.add_tricks('roll over')  # 换言之，实例将属性引用映射到了不同的位置：查找时一般时先映射到共享的类的位置，再是映射到每个实例下。
    e2.add_tricks('play dead')
    print(d2.tricks)
    print(e2.tricks)
```

#### 属性查找优先级

同样的属性名称同时出现在类和实例中，则属性查找会**优先选择实例**。

```python
class Warehouse:
    purpose = 'storage'
    region = 'west'


if __name__ == '__main__':
    w1 = Warehouse()
    print(w1.purpose, w1.region)
    print("=====前后对比=====")
    w2 = Warehouse()
    w2.region = 'east'
    print(w2.purpose, w2.region)
```

方法可以引用全局名称，比如模块、函数。

#### 继承

派生类：```DerivedClassName(BaseName):```

当构造类对象时，基类会被记住，用来解析属性引用：

请求的属性在当前类中找不到，上一级去基类中找。再找不到，如果有基类的基类，就继续递归式地查找。

* 派生类可能重载基类的方法
* 两个内置函数可以被用于继承机制：

```python
isinstance() 检查一个实例的类型
issubclass() 检查类的继承关系
```

#### 私有变量、一些说明

下划线的名称改写

#### 迭代器

```__next__```方法

#### 生成器

用于创建迭代器的工具，使用```yield```语句



### 模块和包

模块就是一个.py文件，模块之间可以互相引用，在实际编程，以主模块为核心，编写各种功能模块。

> 通过.\_\_name\_\_获得当前模块名称

#### 制作模块

```python
# 学习模块的使用，构建更大项目
# 函数放在主函数之外的其他地方

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```

#### 使用模块

```python
import fibo


if __name__ == '__main__':
    # 访问做好的模块
    fibo.fib(1000)
    print(fibo.fib2(100))
    # 当前模块的名称
    print(fibo.__name__)
```

* 技巧：如果经常使用某一函数，可以赋值到一个变量上。

```python
# 导入模块，赋值简化方便后续使用
    fib = fibo.fib
    fib(500)
```

#### 更多关于模块

（1）函数定义和可执行语句在第一次导入时被执行，用来初始化模块。

（2）每个模块都有一个私有符号表：

* 主模块的全局变量不会和其他模块发生冲突

* 可以用访问函数的方法去访问一个模块的全局变量

* 同样，可以指定导入模块的对应私有符号变量而不去导入模块本身

* 使用*符号导入除了以下划线开头的名称之外的所有名称（通常情况不要这样做，因为可能会导入一些未知的函数覆盖调自己定义的东西）

* 可以用as指定别名

  ```python
  from fibo import fib, fib2
  fib(500)
  ```

（3）每个模块在解释器中执行一次，更改了模块的内容得重启。

在交互测试中可以这样做：

```python
import importlib
importlib.reload(modulename)
```

#### 执行模块

使用脚本传入参数执行模块

```python
python module.py <arguments>


# =======
if __name__ == '__main__':
    # 脚本方式执行模块
    import sys

    fib(int(sys.argv[1]))
```

* 技巧：添加main，只有在主模块执行时下面的内容才被调用，经常用于提供一个很方便的用户接口或者用于测试

#### 模块搜索路径

当一个模块被导入，解释器寻找次序为：

（1）具有该名称的内置模块；

（2）从```sys.path```变量给出的目录里面找module.py的文件

> sys.path的初始路径：输入脚本的目录（未指定文件时为当前目录）、PYTHONPATH（一个包含目录名称的列表）、取决于安装的默认位置

！在初始化之后可以更改```sys.path```，包含正在运行的脚本的文件目录将被放在搜索路径的开头，在标准库路径之前。所以，不要让文件和标准库重名了。

#### 关于编译过的python文件

在```__pycache__```缓存```.pyc```文件，会让载入速度变快但并不对执行起作用。

两种情况不检查缓存：（1）命令行载入的；（2）没有源模块。

* \- O 编译时去除断言，\- OO编译时去除断言和```__doc__```字符串
* compileall模块可以为一个目录下的所有模块创建.pyc文件

#### dir()函数

（1）查看模块定义的名称，返回字符串列表

默认返回当前定义的名称，会列出所有类型的名称

（2）要查看内置函数和变量名称：

```python
import builtins
dir(builtins)
```

#### 包

（1）模块的集合，分层的文件系统，```__init.py```是标志。

导入方法类似上述的模块（第2点）

（2）关于```__init.py```文件：

可以只是一个空文件，也可以是执行包的初始化代码或设置```__all__```变量：

包中导入*时，可能会产生不必要的副作用，所以此时可以提供一个包的显式索引，即：

```
from package import *
设置：
__all__ = ['moduleA','moduleB']
如果没有设置__all__:
不会导入包中的任何子模块，只确保 导入当前的模块和运行任何在__init.py__中的代码，然后导入包中定义的任何名称

总结：
建议使用from package import specific_submodule
```

（3）包除了绝对导入外，还可以相对导入：“子包参考”



## 二、将数据引入处理

文件打开

## 三、数据的流通

循环、选择、占位、终止、断言

错误、异常、预定义字句

> 两种可区分的错误：错误和异常

### 语法错误

Syntax Error：解析时发现的错误

### 异常

程序执行时检测到的错误：

> 错误的最后一行，遇到了什么类型的错误；
>
> 错误的前一部分，以堆栈回溯的形式显示发生异常时的上下文

#### 处理异常

* 异常测试：执行try语句，正常情况跳过except；出现异常去检测except中匹配的部分并执行，（没有时报错），执行完继续try语句。

```python
def except_test():
    while True:
        try:
            x = int(input("please input a number: "))
            break
        except ValueError:
            print("Oops! That was no valid number. Try again...")


if __name__ == '__main__':
    # 异常测试：执行try语句，正常情况跳过except；出现异常去检测except中匹配的部分并执行，（没有时报错），执行完继续try语句
    except_test()
```

##### 多个异常

一个except语句可以用元组包含多个异常

```python
...
except (RuntimeError, TypeError, NameError):
    pass
```

##### 执行顺序

> 异常执行时，基类可以起到派生类的作用，假如将基类放在前面，则出发基类。

> **异常类的兼容问题: 基类兼容派生类。但是派生类不兼容基类**

```python
class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


if __name__ == '__main__':
    # 异常类的兼容问题: 基类兼容派生类。但是派生类不兼容基类
    for cls in [B, C, D]:
        try:
            raise cls()
        except D:
            print("D")
        except C:
            print("C")
        except B:
            print("B")
```

反例：

```python
...
# 异常覆盖
for cls in [B, C, D]:
    try:
        raise cls()
    except B:
        print("B")
    except D:
        print("D")
    except C:
        print("C")
```

##### 通配符

> except后没有任何东西时，作通配符

**这种方式可能会掩盖真正的编程错误**

```python
def no_except():
    try:
        f = open('myfile.txt')
        s = f.readline()
        i = int(s.strip())
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise


if __name__ == '__main__':
    # 省略异常以用作通配符
    no_except()
```

##### else子句(可选)

try...except...既是捕获异常，也是对一段代码的保护。而使用else语句可以避免意外捕获try-except语句保护的代码引发的异常。——>就是把try执行代码分开了，针对性地处理

```python
def else_test():
    for arg in sys.argv[1:]:
        try:
            f = open(arg, 'r')
            print('here...')
        except OSError:
            print('cannot open', arg)
        else:
            print(arg, 'has', len(f.readlines()), 'lines')
            f.close()
            
# else子句测试
 else_test()
```

##### except关联到实例

> except可以在异常后面指定一个变量关联到实例

```python
def connect_except():
    try:
        raise Exception('spam', 'eggs')
    except Exception as inst:
        print(type(inst))
        print(inst.args)
        print(inst)

        x, y = inst.args  # unpack args
        print('x = ', x)
        print('y = ', y)

# except可以在异常后面指定一个变量关联到实例
# connect_except()
```

##### 函数内部

> 处理try子句中函数内部发生的异常

```python
def inner_test():
    try:
        this_fails()
    except ZeroDivisionError as err:
        print('Handing run-time error:', err)


if __name__ == '__main__':
    # 程序可以处理try子句中函数内部发生的异常
    inner_test()
```

#### 抛出异常

raise语句：强制发生指定的异常

唯一的参数就是指定的异常

```python
raise NameError

Traceback (most recent call last):
  File "D:/coding/python/python_learn/basic/error_expectation06.py", line 78, in <module>
    raise NameError
NameError
```

重新出发异常：确定异常是否被引发但不处理

```python
def raise_again():
    try:
        raise NameError('HiThere')
    except NameError:
        print('An exception flew by!')
        raise  # 这个raise重新触发了Name Error 打印出来后面的内容


if __name__ == '__main__':
    # 重新引发异常
    raise_again()
```

> 用户可以从Exception派生类自定义自己的异常

#### 定义清理操作

finally子句：定义必须在所有的情况下执行的清理操作

```python
def finally_test():
    try:
        raise KeyboardInterrupt
    finally:
        print('Goodbye, world!')
        
        
if __name__ == '__main__':
    # 定义必须在所有的情况下执行的清理操作
    finally_test()
```

finally子句的优先级是最高的，比except、try都高：

* except的异常（try中、except中、else中）在finally执行完毕后才被触发
* try中的break、continue或return在finally之后被执行
* try和finally中都有return时，以finally中的为准

```python
def bool_return():
    try:
        return True
    finally:
        return False


if __name__ == '__main__':
    # finally拥有最高的优先级
    x = bool_return()
    print(x)
```

> 实际应用程序中，finally子句对于是否释放外部资源（例如文件或者网络连接）非常有用，无论是否成功使用资源。

### 预定义清理子句

在代码执行完毕后及时地清理

```python
def with_test():
    with open("myfile.txt", encoding='utf-8') as f:
        for line in f:
            print(line, end="")


if __name__ == '__main__':
    # with子句预定义清理操作
    with_test()
```



## 四、数据的呈现与储存

### 关于文档标注

标注参数、返回值的属性

```python
def annotations_test(ham: str, eggs: str = 'eggs') -> str:
    """
    函数标注的使用例子：其中分别有对位置参数、关键字参数、返回值的标注
    """
    print("Annotations:", annotations_test.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs
    
if __name__ == '__main__':
    # 函数标注（和文档字符串一起学习的）
    result = annotations_test('spam')
    print(fibonacci.__annotations__)
    print(result)
```

### 表达式语句

格式化输出法：一是格式化字符串面值；

```python
def format_one():
    year = 2021
    event = 'Referendum'
    print(f'Results of the {year} {event}')


if __name__ == '__main__':
    format_one()
```

### format方法

~~~python
print('格式化是这样使唤的：{a}。。。{b}'.format(a='没错，你使唤对了',b='对了2'))
格式化是这样使唤的：没错，你使唤对了。。。对了2
~~~

### 切片和连接操作

> 只想要快速调试时，可以使用repr()函数和str()函数

文件保存

## 五、数据使用



参数解析器

JSON说明



## *Reference*

[1]python 3.8 官方文档：https://docs.python.org/3.8/

## *Time line*

2021年1月24日：知识打碎重构

>2020/12/05 去除杂乱，重构python知识体系，定位为python笔记——记录疑难重点
>
>2020/8/6 用python学习数据结构与算法，
>计划，基础巩固（以练习为主）——> 数据结构理论
>
>2020/4/18 增加基础练习项目：
>     信息管理系统
>
>2020/4/4 简化大纲，去芜存菁，编写思维导图
>
>2020/3/18 目录调整为学习python基础的大纲
>添加知识细节
>
>2020/2/17 实践python，创建文件夹basic 和 exercise
>
>2020/2/8 更新：迭代器、模块
>
>&emsp;&emsp;阶段结束的几句话：
>
>至此，关于python本身的学习就告一段落了，
>
>还有更多有趣、有挑战的模块内容，
>在未来的实践中一点点去探索！
>
>回顾一路学习，
>深感前人思想之浩瀚，编程世界之精彩，个人能力之不足，
>
>也希望自己在接下来多多努力，不忘初心，砥砺前行，奥利给！
>
>2020/2/7  更新：异常、特殊方法
>
>2020/02/06 更新：类
>
>2020/02/03 更新：语句
>
>2020/02/02 添加参考书籍
>
>2020/1/31 对python学习内容做出一些变更
>
>2020/1/27 制定python基础学习计划
>
>2020/1/26 start: for python fundamental study
