# main.py
import turtle as trtl
import time
import Pong_leaderboard as lb # Import your custom file

# screen setup
wn = trtl.Screen()
wn.title("One Player Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# paddle
paddle = trtl.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(-350, 0)

# ball
ball = trtl.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 4
ball.dy = 4

# score
score = 0
score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.color("white")
score_writer.penup()
score_writer.goto(0, 260)
score_writer.write("Score: 0", align="center", font=("Arial", 24, "normal"))

# movement functions
def paddle_up():
    y = paddle.ycor()
    if y < 250:
        paddle.sety(y + 20)

def paddle_down():
    y = paddle.ycor()
    if y > -250:
        paddle.sety(y - 20)

wn.listen()
wn.onkeypress(paddle_up, "Up")
wn.onkeypress(paddle_down, "Down")

# Main Game Loop
while True:
    wn.update()
    time.sleep(0.01)

    # move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # top and bottom bounce
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # right wall bounce
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
    
    # paddle collision
    if (ball.xcor() < -340 and ball.xcor() > -360 and 
        ball.ycor() < paddle.ycor() + 50 and ball.ycor() > paddle.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        score += 1
        score_writer.clear()
        score_writer.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))
    
    # missed ball / GAME OVER
    if ball.xcor() < -410:
        ball.hideturtle()
        
        # Leaderboard Logic
        file_name = "leaderboard.txt"
        player_name = wn.textinput("Game Over", "Enter your name for the leaderboard:")
        
        if player_name is None: # Handle if user clicks 'cancel'
            player_name = "Player"

        # 1. Read existing data
        names_list = lb.get_names(file_name)
        scores_list = lb.get_scores(file_name)

        # 2. Check if it's a high score
        is_high_scorer = False
        if len(scores_list) < 5 or score > min(scores_list):
            is_high_scorer = True

        # 3. Update and Save
        lb.update_leaderboard(file_name, names_list, scores_list, player_name, score)

        # 4. Display results
        wn.clearscreen()
        wn.bgcolor("black")
        lb.draw_leaderboard(is_high_scorer, names_list, scores_list, score_writer, score)
        
        break

wn.mainloop()