# My-Python-Learning-Journey
> 仓库目的：存放我本学期最满意的 Python 小程序，并记录学习心得与后续规划。
## 项目一：每日心情记录（mood_record）
**位置**：`program/mood_record.py  
**功能简介**：让使用者每天可以记录自己当天的心情，并且根据心情的指数给出相应的建议。程序先让用户输入心情指数，范围是1-5的整数，1代表很差，5代表很好。然后根据用户输入的不同分数，给出不同的建议.

**代码**：
```python
print("每日心情记录")
mood=input("请用1-5的数字来评价今天的心情吧（1：非常差，5：非常好）：")
#提示用户输入
mood_score=int(mood)
#将输入的字符串转换为整数
if mood_score == 5:
    print("太棒了！今天真是美好的一天！")
elif mood_score == 4:
    print("不错的一天！适合做一些自己喜欢的事情。")
elif mood_score == 3:
    print("心情平平淡淡才是最真。放松一下，听听音乐吧。")
elif mood_score == 2:
    print("有点小失落吗？试试做些运动，也许会好起来。")
elif mood_score == 1:
    print("心情不太好，记得与朋友或家人聊聊。")
else:
    print("请输入1-5之间的数字。")
#判断心情并给出建议
## 学习心得与规划
