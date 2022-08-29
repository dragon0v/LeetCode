[[python]] [[字典]]
LeetCode 150 逆波兰表达式

好处是可以通过用户输入值执行对应的函数，不使用的话需要用if-else判断，比较占篇幅而且可能降低代码复用性，产生冗余代码


```
op_to_binary_fn = {
	"+": lambda x,y: x+y,
	"-": lambda x,y: x-y,
	"*": lambda x,y: x*y,
	"/": lambda x, y: int(x / y),
	"myint": int
	# 可以是lambda定义的匿名函数，也可以是之前定义过的函数名不加括号
}

print(type(op_to_binary_fn))
# <class 'dict'>

num2 = stack.pop()
num1 = stack.pop()
# 用法
num = op_to_binary_fn[token](num1, num2)

```