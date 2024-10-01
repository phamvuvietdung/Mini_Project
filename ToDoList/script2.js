// Tạo liện kết từ doom đến HTML
var input = document.querySelector('input')
var ul = document.querySelector(".listTodo")
var buttonAdd = document.querySelector(".buttonAdd")

// Viết hàm add để tạo list các note
function addTodo() {
    // Tạo các mảng để chứa giá trị
    var arrTodolist = [...ul.children]
    var textTodo =[]    
    var li= document.createElement('li')

    li.innerHTML = input.value
    // Chỗ này do thêm nhiều dòng nên phải dùng dấu `. để tránh trùng dấu ""
    // Do add thêm thông ti HTML nên dùng +=
    li.innerHTML += `<div class="icon">
                    <i class="fa-solid fa-check"></i>
                    <i class="fa-solid fa-pen"></i>
                    <i class="fa-solid fa-trash"></i>
                    </div>`
    // Kiểm tra dữ liệu trống
    if (input.value.trim() == ""){
        alert("Bạn chưa nhập dữ liệu")
        input.focus()
    }

    // chỗ này chạy lần đầu, để tạo mảng các li
    else if (arrTodolist.length==0) {
        ul.appendChild(li)
        input.value = ""
        input.focus()
    }

    // Kiểm tra xem có trùng dữ liệu
    else {
        // Thêm các note vào 1 mảng mới
        for(var i=0; i<arrTodolist.length; i++){
            textTodo.push(arrTodolist[i].innerText.replace("\n","").trim())
        }
        // Tạo cờ
        var check = true
        for (text of textTodo){
            if(text == input.value.trim()){
                check = false
                break
            }
        }        
        if(!check){
            alert("Dữ liệu đã tồn tại")
            input.value = ""
            input.focus()
        }
        else{
            ul.appendChild(li)
            input.value = ""
            input.focus()
        }
    }
}

// Thêm sự kiện cho nút buttonAdd
buttonAdd.addEventListener("click", addTodo)
