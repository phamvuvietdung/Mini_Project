'''
Sử dụng tkinter
Phần mềm để quản lý sách có các chức năng
- Lưu file
- Độc file
- Hiển thị lên giao diện
- Tìm kiếm
- Sắp xếp
'''
from tkinter import *

'Viết các hàm xử lý file cần sử dụng'
filename = "thu_vien_sach.txt" # khai báo tên file để sử dụng
def savefile(filepath, data):
    'hàm để lưu dữ liệu, dùng try/except để tránh lỗi'
    try:
        openfile = open(filepath,'a',encoding='utf-8')
        openfile.writelines(data)
        openfile.writelines('\n')
        openfile.close()
    except:
        pass

def readfile(filepath):
    'Hàm dùng để đọc dữ liệu từ file'
    dataArray = []
    try:
        openfile=open(filepath,'r',encoding='utf-8')
        for line in openfile:
            data = line.strip().split('---') # strip để loại khoảng trắng, split để tạo ngăn cách giữa các dữ liệu
            dataArray.append(data)
        openfile.close()
    except:
        pass
    return dataArray

def addData():
    'Hàm để thêm dữ liệu vào file'
    data=[]
    data.extend((masach.get(),
                 tensach.get(),
                 namxuatban.get())) # dùng extend((giá trị cần thêm)) có thể thêm cùng lúc nhiều giá trị.
                                # dùng append mỗi lần chỉ thêm được 1 giá trị
    data = "---".join(data) # dùng join để nối dữ liệu cách nhau bằng ---
    savefile(filename,data) # lưu data vào file có tên là filename
    masach.delete(0,END)
    tensach.delete(0,END)
    namxuatban.delete(0,END)
    showData()

def showData():
    'Hàm để hiển thị thông tin trên list box'
    DanhmucSach = readfile(filename)
    listbox.delete(0,END)
    for sach in DanhmucSach:
        listbox.insert(END,sach) # insert (end, data) là chèn dữ liệu vào cuối
        
def sortData():
    DanhmucSach = readfile(filename)
    # DanhmucSach.sort() # dùng hàm này là sort theo mã sách
    
    'Sort theo năm, năm là phần tử thứ 2 trong list DanhmucSach'
    DanhmucSach=sorted(DanhmucSach,key= lambda x:x[2],reverse=TRUE) # hàm này phải đặt biến
                                    # reverse để xếp ngược từ nhỏ đến lớn
    'Tương tự sort theo tên sách'
    # DanhmucSach=sorted(DanhmucSach,key=lambda x: x[1])
    
    'cách thủ công'
    # for i in range(len(DanhmucSach)):
    #     for j in range(len(DanhmucSach)):
    #         nam1 = DanhmucSach[i]
    #         nam2 = DanhmucSach[j]
    #         if nam1[2]>nam2[2]: # vị trí số 2 là số năm XB
    #             DanhmucSach[i] = nam2
    #             DanhmucSach[j] = nam1
    listbox.delete(0,END)
    for sach in DanhmucSach:
        listbox.insert(END,sach)

def searchMasach():
    'Hàm để tìm theo mã sách, đơn giản nên phải gõ đúng hoàn toàn mã sách'
    DanhmucSach = readfile(filename)
    ma = masach.get()
    list_find = []
    for sach in DanhmucSach:
        if ma.lower() in ((sach[0]).lower()):
            list_find.append(sach)
    if len(list_find)==0:
        listbox.delete(0,END)
        listbox.insert(0,"Không tìm thấy nha")
    else:
        listbox.delete(0,END)
        listbox.insert(0,list_find)

'Thiết kế cửa sổ tkinter'
root=Tk()
root.title("Quản lý sách")
root.minsize(height=400,width=350)


'Tạo các widget trên cửa sổ tkinter'
Label(root,text='Ứng dụng quản lý sách',fg='blue',font=('Arial',16),justify=CENTER).grid(row=0,columnspan=2,pady=5)

listbox = Listbox(root,width=58)
listbox.grid(row=1,columnspan=2,pady=5)
showData() # hiển thị dữ liệu trên list box ngay khi mở

Label(root,text="Mã sách:").grid(row=2,column=0)
masach = Entry(root,width=30)
masach.grid(row=2,column=1,pady=5)

Label(root,text="Tên sách:").grid(row=3,column=0)
tensach = Entry(root,width=30)
tensach.grid(row=3,column=1,pady=5)

Label(root,text="Năm xuất bản:").grid(row=4,column=0)
namxuatban = Entry(root,width=30)
namxuatban.grid(row=4,column=1,pady=5)

'Tạo frame để gắn button'
frameButton = Frame(root)

themButton = Button(frameButton,text="Thêm",width=8,command=addData)
themButton.pack(side=LEFT,padx=3)

timButton = Button(frameButton,text="Tìm",width=8,command=searchMasach)
timButton.pack(side=LEFT,padx=3)

sortButton = Button(frameButton,text="Sắp xếp",width=8,command=sortData)
sortButton.pack(side=LEFT,padx=3)

thoatButton = Button(frameButton,text="Thoát",width=8,command=quit)
thoatButton.pack(side=LEFT,padx=3)



frameButton.grid(row=5,columnspan=2,pady=5)


root.mainloop()
