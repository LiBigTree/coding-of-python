# python基础学习手册

记录我学习Python的路，不断修改，一方面是作为未来遗忘时的参考；另一方面给看到的人一个学习的参考。

## 零、编程与生活

首先，我们将生活中所有的问题称之为数据，那么理工科的研究在我看来便是研究不同数据的流通——数据本身或者数据之外。而编程之于解决现实问题，便是对数据的高级操作，将外界的数据以“规范”的形式输入计算机进行处理。这一点的理解有什么用呢？在学习庞杂的知识时，数据线便是我把握知识主干的脉络，在此基础上不断丰富知识库，锻炼逻辑思维能力。

回到Python语言本身，将基础知识打碎重组，有了下面内容。

## 一、Python中数据是如何组织起来的

### 数值、字符串

#### 数值

1、`+ - * / 常规用法`

2、括号用来分组

3、除法运算`/`返回浮点数类型。要返回整数类型用两个`//`

4、计算余数用`%`

5、使用`**`计算乘方

6、等号相当于给一个变量赋值

7、包含多种类型运算数结果以浮点数形式显示

8、交互模式下，上一次的表达时赋值给变量`_`

9、使用复数，后缀`j` 或者`J`表示虚数部分

#### 字符串

1、使用`'...' "..."`表达字符串

2、反斜杠`\`用来转义

3、不转义在字符串前面加r :

`r"..."`

4、三重引号不像让回车包含到字符串中，在行尾加一个`\`

```python
def doc_test():
    a = """\
    123 \
    456
    789
    """
    print(a)
```

5、字符串用`+`连接到一起，用`*`重复

6、相邻两个或多个字符串自动连在一起

```python
a= 'p''c'
a
Out[3]: 'pc'
```

用在把很长的字符串分开输入的场合

7、字符串可以被索引和切片，访问第一个索引的位置是0，以此类推。：索引是获取单个字符串，切片是获取子字符串。

8、切片开始被包括在结果中，结束不被包括。

9、切片中越界索引会被自动处理

```python
a = 'a123'
a[3:5]
Out[5]: '3'
```

10、字符串不能被修改，想要一个不同的字符串，方法是新建一个

11、使用内建函数`len()`返回一个字符串的长度

### 列表

#### 基本

1、通过方括号括起、逗号隔开的一组元素得到；

2、列表支持索引、切片、拼接

3、列表的切片返回一个新的列表

4、列表的内容可以改变

* 可以使用append方法添加新元素
* 赋值不同切片的`[]`可以改变元素大小或者清空列表

5、内置函数`len()`可以作用到列表上

6、列表内可以嵌套列表

```python
lst=[['a','b','c'], 3, 4]
lst[0][1]
Out[8]: 'b'
```

#### 方法

```markdown
list.append(x) 列表末尾添加一个元素
list.extend(iterable) 使用可迭代对象拓展列表
list.insert(i, x) 给定的位置插入一个元素
list.remove(x) 移除列表中第一个值为x的元素
list.pop([i]) 删除列表中指定位置的值并返回它，没有给位置默认是最后一个
list.clear() 移除列表中所有元素
list.index(x[,start[,end]]) 返回列表中值为x的索引，可选切片范围
list.count(x) 返回列表中x出现的次数
list.sort(*, key=None, reverse=False) 对列表元素进行排序，可自定义
list.reverse() 翻转列表中的元素
list.copy() 浅拷贝（关于深浅拷贝区别，浅拷贝是引用，当对于引用的值需要修改时，单独深拷贝。出现这种区别的原因在于资源的利用。举个例子，游戏开发中某一材质会被多个内容使用，但可能只有某一处需要修改材质参数值，这时候材质先都用浅拷贝，然后需要做出修改的部分用深拷贝。）
```

列表——>栈

添加用`append()`，取出用`pop()`

列表——>队列

使用`collections.deque`

#### 列表推导

一种创建列表更简单的方法

1、创建一个新的列表，例如平方

2、使用条件过滤一些元素，例如取出大于等于0的

3、对所有元素使用一个函数处理

```python
vec = [-4, -2, 0, 2, 4]
[x*2 for x in vec]
Out[3]: [-8, -4, 0, 4, 8]
[x for x in vec if x >= 0]
Out[4]: [0, 2, 4]
[abs(x) for x in vec]
Out[5]: [4, 2, 0, 2, 4]
```

4、 对每个元素使用方法

5、创建元组

6、改变数组的维度

```python
freshfruit = [' banana', ' loganberry ', 'passion fruit ']
[weapon.strip() for weapon in freshfruit]
Out[7]: ['banana', 'loganberry', 'passion fruit']

[(x, x**2) for x in range(6)]
Out[8]: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
    
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[num for elem in vec for num in elem]
Out[10]: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

列表推导式可以使用复杂的表达式和嵌套函数

```python
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# 将列表交换其行和列
[[row[i] for row in matrix] for i in range(4)]
Out[14]: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
list(zip(*matrix))
Out[15]: [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```

del语句

可以按照给定的索引移除一个元素，也可以删除整个变量。

### 元组

1、0个元素的元组直接`()`

2、1个元素的元组加`,`

3、元组可以打包和解包

```python
t = 1, 2, 3
x, y, z = t
t
Out[18]: (1, 2, 3)
x
Out[19]: 1
y
Out[20]: 2
z
Out[21]: 3

```

4、元组与生成器表达式

```python
# 生成器表达式
print("使用生成器表达式：", sum(i*i for i in range(10)))
```

### 字典

1、字典是键:值对的集合

2、字典的主要操作是使用关键字储存和解析值

3、对字典使用`list()`可以返回包含该字典中所有键的列表

4、循环中对字典使用`items()`方法可以将关键字和对应的值同时取出

### 函数

#### 定义

1、用关键字`def`引入函数定义

2、第一个语句是文档字符串是一个很好的做法

3、函数的执行：引入一个用于函数局部变量的新符号表；变量引用首先在局部符号中寻找，然后在外层函数的局部符号表，再然后是全局符号表，最后是内置名称的符号表。

4、使用`return`从函数内部返回一个值。不指定返回值默认返回`None`。

*定义函数*

```python
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()  # 空行
```

*调用函数*

```python
if __name__ == '__main__':
    fib(100)
```

#### 位置参数

> 定义时的值叫做形式参数，调用时的值叫做实际参数。

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

1、函数的默认值是在函数**定义处**计算的

```python
i = 5

def f(arg=i):
    print(arg)
    
i = 6
f()
会打印5
```

2、默认定义的形参值被调用时只执行一次，如果想要执行多次，定义在函数内部。

```python
def f2(a, one=[]):
    # one被执行了一次
    one.append(a)
    return one


def f3(a, eli_one=None):
    # 想要执行多次的做法
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

1、在调用中，关键字参数必须跟随在位置参数的后面。

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

2、剩余的形参中，位置参数用`*`收集，关键字参数用`**`收集。

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

#### 如何限制参数调用

1、`/`之前的参数调用仅限位置参数，`*`之后的调用仅限关键字参数，二者之间随意

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

2、使用仅限位置参数，对API，可以防止形参名称被修改时造成的破坏性的API变动

3、当然，若形参有实际意义、防止过度依赖传入参数的位置时，使用仅限关键字参数

#### 打包与解包参数

定义函数时，我们使用`*`或`**`**打包**剩余的位置参数或关键字参数供函数执行使用。

调用函数时，使用它们来**解包**参数传递给函数调用。

```python
def unpack_para():
    args = [3, 6]
    show = list(range(*args))
    print(show)
    
if __name__ == '__main__':
    # 将元组里的参数**解包**分别传递给调用的函数
    unpack_para()
```

#### lambda表达式

创建一个匿名函数，在需要函数对象的任何地方使用。

可以用来返回一个函数或者传递一个小函数作为参数

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

### while语句

只要条件为真就一直执行，非零整数为真，零为假。

标准比较操作符有：`<（小于） >（大于） ==（等于） <=（小于等于） >=（大于等于） !=（不等于）`

```python
def whl_t():
    a, b = 0, 1
    while a < 10:
        print(a, end=',')
        a, b = b, a + b


if __name__ == '__main__':
    whl_t()
```

### if语句

可以有零个或多个`elif`部分以及一个可选的`else`部分

```python
def if_t():
    x = int(input("Please input an integer: "))
    if x < 0:
        x = 0
        print('Negative changed to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')
```

**关键字`elif`适合用于避免过多的缩进**

### for语句

对任意序列进行迭代，条目的迭代顺序与它们在序列中出现的顺序一致。

```python
def for_t():
    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print(w, len(w))
```

**遍历集合时如果要做修改，做法是循环该集合的副本或者创建新集合**

直接修改： `# RuntimeError: dictionary changed size during iteration`

```python
def for_change_error():
    users = {'a': 'active', 'window': 'inactive', 'defenestrate': 'active'}
    for user, status in users.items():  # RuntimeError: dictionary changed size during iteration
        if status == 'inactive':
            del users[user]
```

做法:

```python
def for_change():
    users = {'a': 'active', 'window': 'inactive', 'defenestrate': 'active'}
    for user, status in users.copy().items():  # RuntimeError: dictionary changed size during iteration
        if status == 'inactive':
            del users[user]
    print(users.keys())
```

```python
def for_change2():
    active_users = {}
    users = {'a': 'active', 'window': 'inactive', 'defenestrate': 'active'}
    for user, status in users.items():  # RuntimeError: dictionary changed size during iteration
        if status == 'active':
            active_users[user] = status
    print(active_users.keys())
```

### range和enumerate函数

返回的都是可迭代对象：

`range`可以用来迭代由算术级数组成的序列；

`enumerate()`可以用来迭代序列的索引位置和其对应的值

### zip函数

将序列之间的元素一一匹配

```python
def zip_t():
    a = [1, 2, 3]
    b = ['one', 'two', 'three']
    for m, n in zip(a, b):
        print('{0}的英文是{1}'.format(m, n))
     
1的英文是one
2的英文是two
3的英文是three
```

### break/continue/for...else.../while...else...

1、`break`可以跳出最近的`for`或`while`循环

2、`for`或`while`循环带有`else`子句时，在for耗尽可迭代对象、while变为假值时执行，**break终止时不执行else**。

3、`continue`表示继续循环中下一次迭代

```python
def break_t():
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')
          
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3       
```

```python
def continue_t():
    for num in range(2, 10):
        if num % 2 == 0:
            print("Found an even number", num)
            continue
        print("Found an odd number", num)
```

### pass语句

什么也不做，语法上需要这么一个东西，但不需要执行什么的时候用。

```python
def pass_t():
    while True:
        pass  # Busy-wait for keyboard interrupt


class MyEmptyClass:
    pass


def initlog(*args):
    pass  # Remember to implement this!
```

错误分为语法错误和异常

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

## 四、数据的呈现

### 文档字符串

1、文档字符串的书写：缩进是根据第一个非引号行确定的；

2、第一部分：对象目的的简述。

3、第二部分：空白，在视觉上与其余描述分开。

4、第三部分：对象的调用约定、它的副作用等。

### 函数标注的使用方法

形参的标注是后面加上`:`，返回值的标注是括号后面、冒号前面加上`->`。

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

## 五、数据使用

### 文件

1、处理文件对象使用`with`关键字

2、文件中读取行使用循环遍历文件对象

### JSON说明

序列化和反序列化治之间对数据或文件高效地利用，JSON格式通常被现代应用程序用于允许数据交换

## *Reference*

[1]python 3.8 官方文档：https://docs.python.org/3.8/

## *Time line*

2021年1月24日：知识打碎重构

>2021/2/4 学习手册v1.0 
>
>2020/12/05 去除杂乱，重构python知识体系，定位为python笔记——记录疑难重点
>
>2020/8/6 用python学习数据结构与算法，
>计划，基础巩固（以练习为主）——> 数据结构理论
>
>2020/4/18 增加基础练习项目：
>信息管理系统
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
