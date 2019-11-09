#设置小海龟的形状和颜色
import turtle as T
#定义重复函数
def drawstar(x,y,color):
    
    T.up()
    T.goto(x,y)
    T.down()
    T.color(color)
    T.begin_fill()     
    for i in [0, 1, 2, 3, 4]:
        T.right(144)
        T.forward(100)
    T.end_fill()


drawstar(-200,200,"blue")
drawstar(-200,-200,"red")
drawstar(300,200,"green")
drawstar(300,-200,"yellow")
        

#将小海龟移动到原处
T.up()
T.home()
