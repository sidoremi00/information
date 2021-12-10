function score(Score: number, Winner: string) {
    
    if (Score >= 5) {
        석진이 = "Finish"
        basic.showString("Game over")
        basic.showString("Winner is")
        basic.showString(Winner)
    } else {
        석진이 = "Non"
        basic.clearScreen()
    }
    
}

//  시작
let 석진이 = "Non"
let Player_1 = 0
let Player_2 = 0
//  석진이
//  Non 
//  Play 
//  Finish 
//  점이 보이고 먼저 클릭하면 1점 추가
//  계속 반복 
basic.forever(function on_forever() {
    
    if (석진이 == "Non") {
        basic.pause(randint(1000, 5000))
        //  랜덤으로 시간 설저
        led.plot(randint(0, 4), randint(0, 4))
        //  랜덤 좌표
        석진이 = "Play"
    }
    
    if (석진이 == "Play") {
        if (input.pinIsPressed(TouchPin.P1)) {
            //  1에 신호가 감지 되었을때(player a가 버튼을 눌렀을 때)
            score(Player_1, "A")
            Player_1 += 1
            basic.showArrow(ArrowNames.West)
            basic.clearScreen()
            basic.pause(10)
        }
        
        if (input.pinIsPressed(TouchPin.P2)) {
            //  2에 신호가 감지 되었을때(player b가 버튼을 눌렀을 때)
            score(Player_2, "B")
            Player_2 += 1
            basic.showArrow(ArrowNames.East)
            basic.clearScreen()
            basic.pause(10)
        }
        
    }
    
})
