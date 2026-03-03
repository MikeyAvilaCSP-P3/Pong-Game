# leaderboard.py

# return names in the leaderboard file
def get_names(file_name):
    try:
        leaderboard_file = open(file_name, "r")
        names = []
        for line in leaderboard_file:
            leader_name = ""
            index = 0
            while (index < len(line) and line[index] != ","):
                leader_name = leader_name + line[index]
                index = index + 1
            if leader_name:
                names.append(leader_name)
        leaderboard_file.close()
        return names
    except:
        return []

# return scores from the leaderboard file
def get_scores(file_name):
    try:
        leaderboard_file = open(file_name, "r")
        scores = []
        for line in leaderboard_file:
            leader_score = ""
            index = 0
            # Skip the name and comma
            while (index < len(line) and line[index] != ","):
                index = index + 1
            index = index + 1 # Move past the comma
            
            # Read the score
            while (index < len(line) and line[index] != "\n"):
                leader_score = leader_score + line[index]
                index = index + 1
            
            if leader_score:
                scores.append(int(leader_score))
        leaderboard_file.close()
        return scores
    except:
        return []

# update leaderboard by inserting the current player and score
def update_leaderboard(file_name, leader_names, leader_scores, player_name, player_score):
    index = 0
    for i in range(len(leader_scores)):
        if (player_score >= leader_scores[i]):
            break
        else:
            index = index + 1

    leader_names.insert(index, player_name)
    leader_scores.insert(index, player_score)

    # Keep only top 5
    if len(leader_names) > 5:
        leader_names.pop()
    if len(leader_scores) > 5:
        leader_scores.pop()

    leaderboard_file = open(file_name, "w")
    for i in range(len(leader_names)):
        leaderboard_file.write(leader_names[i] + "," + str(leader_scores[i]) + "\n")
    leaderboard_file.close()

# draw leaderboard and display a message to player
def draw_leaderboard(high_scorer, leader_names, leader_scores, turtle_object, player_score):
    font_setup = ("Arial", 20, "normal")
    turtle_object.clear()
    turtle_object.penup()
    turtle_object.hideturtle()
    
    # Title
    turtle_object.goto(-160, 150)
    turtle_object.write("LEADERBOARD", font=("Arial", 24, "bold"))

    # Draw entries
    for index in range(len(leader_names)):
        turtle_object.goto(-160, 100 - (index * 40))
        text = f"{index + 1}. {leader_names[index]}: {leader_scores[index]}"
        turtle_object.write(text, font=font_setup)

    # Message at bottom
    turtle_object.goto(-160, -150)
    if high_scorer:
        turtle_object.write("Congratulations! High Score!", font=font_setup)
    else:
        turtle_object.write("Nice try! Play again?", font=font_setup)