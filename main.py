def on_button_pressed_a():
    global Re
    Re = 1
    basic.show_leds("""
        # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
    """)
    basic.show_leds("""
        # . . . #
                . # . # .
                . . . . .
                . # . # .
                # . . . #
    """)
    basic.show_leds("""
        # . . . #
                . . . . .
                . . . . .
                . . . . .
                # . . . #
    """)
    basic.pause(100)
    control.reset()
input.on_button_pressed(Button.A, on_button_pressed_a)

def score(Score: number, Winner: str):
    global 석진이
    if Score >= 1:
        basic.show_string("GG")
        basic.show_string("Winner is")
        basic.show_string(Winner)
        basic.pause(100)
        석진이 = "Finish"
    else:
        석진이 = "Non"
        basic.clear_screen()
Re = 0
석진이 = ""
# 시작
석진이 = "Non"
Player_1 = 0
Player_2 = 0
Re = 0
# 석진이
# Non
# Play
# Finish
# 점이 보이고 먼저 클릭하면 1점 추가
# 계속 반복

def on_forever():
    global 석진이, Player_1, Player_2
    while Re == 0:
        if 석진이 == "Non":
            basic.pause(randint(1000, 5000))
            # 랜덤으로 시간 설저
            led.plot(randint(0, 4), randint(0, 4))
            # 랜덤 좌표
            석진이 = "Play"
        if 석진이 == "Play":
            if input.pin_is_pressed(TouchPin.P1):
                # 1에 신호가 감지 되었을때(player a가 버튼을 눌렀을 때)
                score(Player_1, "A")
                Player_1 += 1
                basic.show_arrow(ArrowNames.WEST)
                basic.clear_screen()
                basic.pause(10)
            if input.pin_is_pressed(TouchPin.P2):
                # 2에 신호가 감지 되었을때(player b가 버튼을 눌렀을 때)
                score(Player_2, "B")
                Player_2 += 1
                basic.show_arrow(ArrowNames.EAST)
                basic.clear_screen()
                basic.pause(10)
        if 석진이 == "Finish":
            basic.show_string("Try again=A else=B")
            if input.button_is_pressed(Button.B):
                basic.show_icon(IconNames.SKULL)
                break
basic.forever(on_forever)