[[整除]] [[取整]] [[python]]
int和// 对正数都一样
math.floor() 永远向下取整
math.ceil() 永远向上取整

**对于负数：**
```
res = int(20/-6)

# res = -3

res = 20//-6

# res = -4
# // 运算永远相当于math.floor?

res = math.floor(20/-6)
# 向下取整
# res = -4

res = math.ceil(20/-6)
# 向上取整
# res = -3

```