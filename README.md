# Python基础与脚本开发
## 数据类型

Python有五个标准的数据类型：

- Numbers（数字）
- String（字符串）
- List（列表）
- Tuple（元组）
- Dictionary（字典）

### 数字

Python支持四种不同的数字类型：

- int（有符号整型）

- ~~long（长整型，也可以代表八进制和十六进制）~~

  *Python2.X 版本中，在 2.2 以后的版本中，int 类型数据溢出后会自动转为long类型。在 Python3.X 版本中 long 类型被移除，使用 int 替代。*

- float（浮点型）

- complex（复数）

### 字符串

用来定义文本数据

python的字串列表可以从左往右读取，也可以从右往左

- 从左到右索引默认0开始的，最大范围是字符串长度少1
- 从右到左索引默认-1开始的，最大范围是字符串开头

```python
str = ('jaycehe')
print(str[1:5])
print(str[-6:5])
```

![image-20230313164830374](https://oss.jayce.icu/markdown/image-20230313164830374.png)

```python
print str[0]        # 输出字符串中的第一个字符 
print str[2:5]      # 输出字符串中第三个至第六个之间的字符串 
print str[2:]       # 输出从第三个字符开始的字符串 
print str * 2       # 输出字符串两次 
print str + "TEST"  # 输出连接的字符串
print(str[0:7:1])   #输出字符串中第一个至第八个之间的字符串，步长为2
```

 

### 列表

列表用 **[ ]** 标识，是 python 最通用的复合数据类型

```python
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print (list)     # 输出完整列表
print (list[0])   # 输出列表的第一个元素
print (list[1:3])  # 输出第二个至第三个元素 
print (list[0:5:2]) # 输出第一个至第六个元素,步长为2
print (list[2:])  # 输出从第三个开始至列表末尾的所有元素
print (tinylist * 2) # 输出列表两次
print (list + tinylist)  # 打印组合的列表
```





### 元组

元组用 **()** 标识。内部元素用逗号隔开。**但是元组不能二次赋值，相当于只读列表**





### 字典
