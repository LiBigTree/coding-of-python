# 时间线

>2020/3/18 目录调整为学习python基础的大纲
>添加知识细节
>
>2020/2/17 实践python，创建文件夹basic 和 exercise
> 
>2020/2/8 更新：迭代器、模块
>
>阶段结束说的几句话：
>至此，关于python本身的学习就告一段落了，还有文件、交互、
>更多有趣的模块等等，将在未来的实践中一点点探索，回顾一路学习，
>深感前人思想之浩瀚，编程世界之精彩，个人能力之不足，
>也希望自己在接下来多多努力，不忘初心，砥砺前行，奥利给！
>
> 2020/2/7  更新：异常、特殊方法
>
>2020/02/06 更新：类
>
>2020/02/03 更新：语句
>
>2020/02/02 添加参考书籍
>
> 2020/1/31 对python学习内容做出一些变更
>
> 2020/1/27 制定python基础学习计划
>
> 2020/1/26 start: for python fundamental study

# 基础学习大纲

## 一、标准数据类型
### 1、五种数据类型概述
1.1 数字和字符串
### 逻辑线 定义>>通用的性质>>特有的性质>>应用：本身和与其他事物联系

* 数字：整型int（> bool型）、浮点型float、复数complex

* 字符串 str
认识 type（）、类型之间转换

1.2 相关基础概念铺设：
1）变量赋值、赋值的方法： 链式赋值、增强赋值

2）运算>>算数运算符号，比较运算符号，逻辑运算符号

3） 注释

### 2、理解序列
可修改：列表，不可修改：元组、字符串

2.1 定义及性质

list，tuple，str

2.2 通用性质： 索引、切片、相乘（重复）、相加（链接）、成员资格检查；长度、最大值、最小值

2.3 特有性质： 

1）列表

修改：赋值、删除；

方法：增加、清空、复制、计数、拓展、
查找索引、插入对象、删除一个元素、删除第一个指定元素、排序。

2）元组

3）字符串
单、双、三引号

格式设置： 

a. 用%插入变量；

b. Format理解占位与格式，

设置替换字段名字：数字显示的相关设置（正负号、位数、对齐方式）。
方法：填充、查找、合并、拆分、大小写、替换、指定字符的替换、删除空白

### 3、字典

1）定义：映射

2）通用性质

3）特有性质研究：添加、删除、修改

方法：删除字典项、复制、创建新字典、访问字典、访问字典可添加、
字典视图（用于迭代）：键视图/值视图/键值视图、删除键值对、更新字典

## 二、控制语句
### 1、相关铺垫：

1）序列解包(*收集多余的值)；

2）代码块（一组语句）。

### 2、条件：
1） 使用规则

2）应用相关：布尔值、运算符。

### 3、循环：

1）规则
While
For

2）应用相关：
迭代，range生成器、字典迭代、zip、enumerate、反向和排序迭代

3）跳出循环：break、continue

4） 简单推导

5） pass

## 三、函数

### 1、定义函数
给函数写文档
返回值
### 2、参数（关键字参数、收集参数）

变量空间

匿名函数

## 四、类

### 1、定义

多态、封装、继承

### 2、命名空间

### 3、构造函数
Super

## 五、异常
定义及使用

## 六、模块、包
定义

导入模块的方法

探索模块学习技巧help(xxx)、dir（xxx）

标准库学习：sys、random、time、
## 七、文件
文件路径的表示

读取与写入文件

os模块、
pickle模块
 
 
# 参考：
> 
>书籍：python基础教程（第三版） 
>
>[挪] Magnus Lie Hetland(著) 袁国忠（译）
>
> 网站：
>https://docs.python.org/3.7/