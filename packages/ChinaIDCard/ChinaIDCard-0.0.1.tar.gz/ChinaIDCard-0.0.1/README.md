# 关于ChinaIDCard

这是一个进行身份证计算的ID库，主要应用场景为对身份证的合法性进行效验。

# 函数调用

目前版本，提供了下列函数：

```python
check_ID_Card(ID Card) # 验证18位身份证是否在算法意义上合法

calculation_17ID_Card_code18(ID Card) # 通过身份证前17位获取第18位

generate_ID_Card() # 随机获取一个合法的身份证
```

# 验证

我们是通过http://www.ip33.com/shenfenzheng.html进行验证的结果

算法也来自于此网站