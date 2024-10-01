'''
Tạo một app để giải một phương trình bậc 1
Dùng TKinter 
'''
from tkinter import *
from fractions import Fraction # import hàm tạo phân số


'tạo hàm tieptuc'
def tieptuc():
    'Hàm để clear các entry'
    HeSoA.delete(0,END)
    HeSoB.delete(0,END)
    KetQua.delete(0,END)
    phanso.delete(0,END)

def giaiPT():
    'Hàm để giải phương trình bậc 1'
    try: # dùng try, except để tránh trường hợp nhập sai
        a=float(HeSoA.get()) # lấy giá trị của entry hệ số a
        b=float(HeSoB.get()) # nếu để float thì không hiển thị dạng phân số nếu kết quả là số vô hạn
                            # để float thì thêm limit_denominator(100) ở hàm fraction()
                            # để 10 thì không có số lẻ, 100 là 1 số lẻ
        if a == 0 and b==0:
            phanso.delete(0,END)
            KetQua.delete(0,END) # thêm này để nếu nhấn lại không bị trùng dữ liệu
            KetQua.insert(0,'Vô số nghiệm') # dùng insert để đưa giá trị mặc định vào entry
        elif a == 0 and b !=0:
            phanso.delete(0,END)
            KetQua.delete(0,END)
            KetQua.insert(0,'Vô nghiệm')
        else:
            c=-b/a
            nghiem=Fraction(c).limit_denominator(1000) # trong trường hợp các số chia vô hạn tuần hoàn ví dụ 2/3
                                    # hàm limit.denominator(10) sẽ chỉ giới hạn ở số thập phân (không có số lẻ)
                                    # hàm limit.denominator(100) sẽ chỉ giới hạn 1 số lẻ
            KetQua.delete(0,END)
            phanso.delete(0,END)
            KetQua.insert(0,c)
            phanso.insert(0,nghiem)           
    except:
        phanso.delete(0,END)
        KetQua.delete(0,END)
        KetQua.insert(0,'Dữ liệu chưa đúng. Xin nhập lại')

root = Tk()
root.title("Giải phương trình bậc 1")
root.minsize(height=150,width=250)
root.resizable(height=TRUE, width=TRUE)

Label(root,text="Phương trình bậc 1:\n ax + b = 0",fg="red",font=('Arial',16),justify=CENTER).grid(row=0,columnspan=2) # dùng phương thức grid để gắn label lên cửa sổ
                                                                                                         # columnspan sẽ kéo dài qua 2 cột   
Label(root,text="Hệ số a:").grid(row=1,column=0)
HeSoA = Entry(root,width=30)
HeSoA.grid(row=1,column=1)

Label(root,text="Hệ số b:").grid(row=2,column=0)
HeSoB=Entry(root,width=30)
HeSoB.grid(row=2,column=1)

'có nhiều nút nằm trên 1 dòng. Nên dùng frame và gắn nút vào frame'
frame_button = Frame(root)
Button(frame_button,text="Giải",command=giaiPT).pack(side=LEFT,padx=5,pady=2)
Button(frame_button,text="Tiếp",command=tieptuc).pack(side=LEFT,padx=5,pady=2)
Button(frame_button,text="Thoát",command=root.quit).pack(side=LEFT,padx=5,pady=2)

frame_button.grid(row=3,columnspan=2)

Label(root,text="Kết quả:").grid(row=4,column=0)
KetQua=Entry(root,width=30)
KetQua.grid(row=4,column=1)

Label(root,text="Phân số:").grid(row=5,column=0)
phanso=Entry(root,width=30)
phanso.grid(row=5,column=1)

root.mainloop()