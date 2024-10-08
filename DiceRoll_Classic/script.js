var playButton = document.querySelector('button');

function rollingDice() {   
    // Dùng hàm math rand để lấy số ngẫu nhiên 0.0 - 1.0.
    // Nhân 6 để ra được số ngẫu nhiên 0-5.9. 
    // Dùng hàm math floor để làm tròn xuống. do đó +1 để ra số 1-6
    var randNumber = Math.floor(Math.random()*6)+1
    
    // chọn hình ảnh xúc xắc
    var imgDice = document.querySelector(".imgDice")

    // Dùng thuộc tính setAtrribute cho src để đổi hình
    // Do tên các hình là "dice"+số+".png"
    imgDice.setAttribute("src","./asset/dice" + randNumber + ".png")
}

playButton.addEventListener('click',rollingDice)

// gắn vào nút enter cho body. nếu là button thì không cần gắn phím enter
// playButton.addEventListener("keyup",function(e){
//     if(e.key == "enter"){
//         rollingDice()
//     }
// })