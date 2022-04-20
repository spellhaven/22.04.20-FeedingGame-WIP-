import turtle as t
import random #먹이의 위치 생성은 랜덤값이어야 그게 재밌는 게임이지.
import os


#환경설정
t.setup(800,600) #캔버스 사이즈 지정
t.bgcolor('DodgerBlue4') #난 오늘도 찾는다. 간지나는 파랑을...
t.up() #그림 그리지 마
t.ht() #거북이 숨겨


#변수선언
player_speed = 1 #플레이어 초기 속도는 1로 설정.
score = 0 #점수
game_over = False #Bool로 만든 게임 종료 변수. True일 시 종료


#플레이어, 해초, 독초 만들기
player = t.Turtle() #플레이어는 Turtle()의 한 인스턴스.
player.shape('turtle')
player.up() #그림 그리지 마
player.color('gold1') #https://cs111.wellesley.edu/labs/lab02/colors 멋있는 색깔을 찾아 떠난다. 나는 오늘도.
player.shapesize(3) #플레이어(거북이) 크기.
player.speed(0) #거북이의 초기 속도

#키 조정 - 사용자 함수
def turn_left():
    player.left(40) #꼭 40도가 아니어도 된다. 적절한 각도를 찾아 보자.
    
def turn_right():
    player.right(40)
    
t.onkeypress(turn_left, "Left") #onkeypress는 이미 있는 메소드다. 이걸로 우리 사용자 함수를 호출해 보자 ㅋ.
t.onkeypress(turn_right, "Right")
t.listen() #거북이가내말을들어준다니... "정가람보다 낫다"

# 랜덤 위치 - 사용자 함수. 소스 코드에는 rend_pos()로 오타 내셨는데 나중에 문제 생기면 그건지 보셈.
def rand_pos():
     x_cor = random.randint(-350, 350)
     y_cor = random.randint(-250, 250)
     return x_cor, y_cor
    
# 거북이 먹이. food.
food = t.Turtle() #오. 플레이어뿐만 아니라 얘도 터틀 인스턴스로 지정하는구나
food.ht() #(객체 설정하는 동안엔?) 먹이 보여주지마
food.shape('triangle') #카와이하게 삼각형 모양 먹이를 먹어볼게요
food.up()
food.color('green')
food.setheading(90) #이걸 설정해야 멋있는 모양으로 먹이가 나온다.
food.st() #먹이 보여줘

# 독초 badfood.
badfood = t.Turtle()
badfood.ht() #(객체 설정하는 동안엔?) 독초 보여주지마
badfood.shape('triangle')
badfood.up()
badfood.color('red') # 딱 봐도 위험한 색깔이다. 국민의힘 색. 고려대학교 색.
badfood.setheading(90)
badfood.st() #독초 보여줘

# 점수 표시
t.goto(10,250) #점수가 표시될 위치
t.color('pink')
t.write(f"score : {score}", False, "center", ("", 20)) #이건 몰라. 모르지만 그냥 쓰자. 큰 그림을 잡는 게 중요한 거니까...

#이건 뭔 기능이냐?
#time.sleep(100)

while not game_over:
    player.forward(player_speed)

    #벽에 닿을 경우 반동. (플레이 공간에서 벗어나지 않게. 마치 집착광수처럼... https://bit.ly/3MlBPYz)
    if (player.xcor() > 350 or player.xcor() < -350 or player.ycor() > 250 or player.ycor() < -250):
    #play area가 800*600이고, 정가운데가 원점이다. 그걸 고려해서 왜 이 숫자가 이런지 생각 ㄱㄱ.
        player.right(100)
































