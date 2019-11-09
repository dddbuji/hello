#请输入年份
x=input("请输入年份：")
x=eval(x)
if((x%400==0) | ((x%4==0) & (x%100 != 0))):#判断是否为闰年
    print("{}为闰年". format(x))
else:
    print("{}不为闰年". format(x))
