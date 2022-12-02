import time
from pynput.keyboard import Key,Controller

# def hongzha(number,text):
#     time.sleep(3)
#     for i in range(number):
#         key_cl().type(text)
#         key_cl.press(Key.enter)
#         key_cl().release(Key.enter)
#         time.sleep(0.2)
#
# hongzha(20,"hhhhh")

keyboard = Controller()
a = input("输入内容：")
b = eval(input("输入循环次数："))

print("数据已接收！将光标移动到会话框")
time.sleep(1)
for i in range(3):
    print(r'距离程序运行还剩下%d秒'%(3-i))
    time.sleep(1)

for i in range(b):
    keyboard.type(a)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.2)

print("消息已经发送完成")



