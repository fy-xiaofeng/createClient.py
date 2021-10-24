
import base64
import tkinter
import tkinter.messagebox as messagebox
from tkinter import *
from icon import img
import psutil
from socket import AddressFamily

local_addrs = []


def ip():
    for name, info in psutil.net_if_addrs().items():
        # print ("xxx   ",name)
        for addr in info:
            # 只放入IPv4的地址
            if AddressFamily.AF_INET == addr.family:
                local_addrs.append(addr.address)
    return local_addrs


def find_ip(class_ip):
    box = []
    ip_all = ip()
    for ip_3 in ip_all:
        if ip_3[0:3] == class_ip:
            box.append(ip_3)
    with open("fuwuqi.wb", "w") as fuwuqi:
        fuwuqi.write(box[0] + ":545")
    return box[0]


def hello():
    messagebox.showinfo("Hello Python", "Hello 枫云网络工作室")


# def waitGet():
#     key1 = input1.get()
#     print(key1)


def cc():
    input1.delete(0, END)
    ikey = 0


root = tkinter.Tk()
root.title("枫云网络工作室")
wm_1, hm_1 = root.maxsize()
w = int(wm_1 / 5)
h = int((hm_1 / 1) - w / 2)
root.geometry(f'{w}x{h}')
print(w)
print(h)

frm = tkinter.Frame(root)
frm.pack()

frm1 = tkinter.Frame(frm)
input1 = tkinter.Entry(root, show="")


def show(ikey):
    show_info = Label(root, text=f'您选择的是{ikey}')
    show_info.pack(pady=40)


def cmd1():
    cc()
    ikey = find_ip('192')
    input1.insert(0, f'{ikey}')
    print(ikey)


def cmd2():
    cc()
    ikey = find_ip('172')
    input1.insert(0, f'{ikey}')
    print(ikey)


def cmd3():
    cc()
    ikey = find_ip('10.')
    input1.insert(0, f'{ikey}')
    print(ikey)


def cmd4():
    try:
        cc()
        ikey = find_ip("192")
        input1.insert(0, f'{ikey}')
    except IndexError as e:
        try:
            cc()
            ikey = find_ip("172")
            input1.insert(0, f'{ikey}')
        except IndexError as e:
            try:
                cc()
                ikey = find_ip("10.")
                input1.insert(0, f'{ikey}')
            except IndexError as e:
                cc()
                print("自行查看ipv4地址，改为ipv4+:545格式")
                input1.insert(0, "自行查看ipv4地址，改为ipv4+:545格式")


input1.pack()

b1 = Radiobutton(root, text='使用198号段', relief=FLAT, value=1, command=cmd1)
b1.pack()
b2 = Radiobutton(root, text='使用172号段', relief=FLAT, value=2, command=cmd2)
b2.pack()
b3 = Radiobutton(root, text='使用  10号段', relief=FLAT, value=3, command=cmd3)
b3.pack()
b4 = Radiobutton(root, text='使用顺序查找', relief=FLAT, value=4, command=cmd4)
b4.pack()

button_1 = Button(root, text='确定!', relief=GROOVE, command=root.quit)
button_1.pack(pady=50)
button_2 = Button(root, text='清空!', relief=GROOVE, command=cc)
button_2.pack(pady=5)
frm1.pack(pady=30)
output2 = tkinter.Label(root, text="TIPS:\n如果不能联通教师端\n请自行编辑fuwuqi.wb文件\n格式为\n教师机ipv4地址:545\n")
output2.pack(side=BOTTOM)
with open('icon.ico', 'wb+') as f:
    f.write(base64.b64decode(img))
root.iconbitmap("./icon.ico")
root.mainloop()
