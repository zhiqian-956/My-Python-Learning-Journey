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
