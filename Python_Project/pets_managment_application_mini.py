'''
ứng dụng nhỏ để quản lý thú nuôi có các chức năng
1. In danh sách thú nuôi
2. Thêm/ xoá danh sách thú nuôi
3. Chuyển thú nuôi đi
4. Truy cập vào vị trí thú nuôi
Đây là ứng dụng nhỏ, chỉ lưu vào list khi chạy app. sau khi chạy lại thì sẽ in lại danh sách cũ ban đầu, không nhớ được
'''

# Tạo 1 list các 
so_thu=['hươu cao cổ','cừu','nhím','heo',
        'lạc đà','bò sữa','mèo']
# print(so_thu)

# Dùng vòng lặp while để đưa thông tin
while True: # dùng boolean While True để tạo vòng lặp vĩnh cửu khi hết câu lệnh sẽ quay lại
    print('Chào quản lý vườn thú.Tôi có thể giúp gì cho bạn:\n',
        '1. In danh sách \n',
        '2. Truy cập vị trí thú nuôi\n',
        '3. Thêm thú nuôi\n',
        '4. Thay thế thú nuôi\n',
        '5. Chuyển thú nuôi đi nơi khác\n',
        '6. Thoát') # dùng ký tự \n để xuống dòng
    option = int(input('Nhập chức năng cần thực hiện:'))
    if option==1:
        print('Danh sách thú bao gồm:')
        print(*(thu+'\n' for thu in so_thu)) # dùng \n để xuống dòng cho mỗi con thú trong so_thu
    elif option==2:
        pos=int(input('Nhập vị trí chuồng để xem thú nuôi:'))
        if 0<pos<len(so_thu):
            print('Vị trí thú trong chuồng {} là '.format(pos),so_thu[pos-1])
        else:
            print("Không có thú ở vị trí này")
    elif option==3:
        new_pet=input('Thú nuôi cần thêm vào là: ')
        so_thu.append(new_pet)
        print('Đã thêm {} vào sở thú. Danh sách thú nuôi hiện giờ là'.format(new_pet),so_thu)
    elif option==4:
        change_pet = int(input('Vị trí chuồng thú muốn thay thế:'))
        print('Vị trí này là',so_thu[change_pet-1])
        new_pet=input('Nhập tên thú muốn đổi:')
        so_thu[change_pet-1] = new_pet
        print("Đã thay đổi, sở thú hiện giờ là", so_thu)
    elif option==5:
        move_pet=input('Tên thú nuôi muốn di chuyển:')
        for pets in so_thu:
            if move_pet.strip().lower() == pets.strip().lower():
                so_thu.remove(pets)
                print('Đã chuyển {} đi.'.format(pets),'Danh sách thú hiện giờ là: ',so_thu)
        else: # vòng lặp for/else nếu chọn thú không có trong vườn thú thì sẽ trả là không có thú nào và làm lại từ đầu
            print('Không có thú này trong vườn thú. chọn lại nhé')
    elif option==6:
        break
    else:
        print('Không có chức năng này. Vui lòng chọn lại')
        pass
        
        