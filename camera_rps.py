import cv2
from keras.models import load_model
import random
import numpy as np
import time
import threading

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
labels = open("labels.txt", "r").readlines()

previous_move = "nothing"
Computer = "nothing"
User = "nothing"
point_Com = 0
point_User = 0
round = 0
winner = "Waiting..."
convert_round = "0"
End = 0

def countdown():
    max_time = 10 #the time you want
    start_time = time.time()
    while (time.time() - start_time) < max_time:
        mins, secs = divmod(max_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        max_time -= 1

def countdown1():
    countdown_time = 5
    start_time = time.monotonic()
    while countdown_time:
        current_time = time.monotonic()
        elapsed_time = current_time - start_time
        mins, secs = divmod(countdown_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        if elapsed_time >= 1:
            print(timer)
            countdown_time -= 1
            start_time = time.monotonic()

    print('Time is up!')    

def get_winner(User,Computer):
    global point_Com,point_User
    if User == Computer:
        return "Tie"

    elif User == "rock" :
        if Computer == "scissors":
            point_User = point_User+1
            return "You wins"
        elif Computer == "paper":
            point_Com = point_Com+1
            return "You lost"
        else:
            return "Invalid input"

    elif User == "paper" :
        if Computer == "scissors":
            point_Com = point_Com+1
            return "You lost"
        elif Computer == "rock":
            point_User = point_User+1
            return "You wins"
        else:
            return "Invalid input"

    elif User == "scissors" :
        if Computer == "rock":
            point_Com = point_Com+1
            return "You lost"
        elif Computer == "paper":
            point_User = point_User+1
            return "You wins"

        else:
            return "Invalid input"
    else:
        return "Error"


while True: 
    ret, frame = cap.read()
    if not ret:
        continue
    # rectangle for Computer to play
    cv2.rectangle(frame, (25, 25), (225, 200), (255, 255, 255), 2)
    # rectangle for Player to play
    cv2.rectangle(frame, (425, 25), (625, 200), (255, 255, 255), 2)
    # extract the region of image within the user rectangle
    roi = frame[25:200, 425:625]
    img = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)

    resized_frame = cv2.resize(img, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    #predict User
    User = labels[np.argmax(prediction)]
    User = User.strip()

    #Duel
    if round == 0:
        if User == "nothing":
            Computer = "nothing"
            winner = "Waiting..."

        elif User != "nothing":
            Computer = random.choices(['rock','paper','scissors'])
            Computer = Computer[0]
            winner = get_winner(User,Computer)
            round = round+1
            convert_round = str(round)
            countdown1()

    elif round == 1:
        if User == "nothing":
            Computer = "nothing"
            winner = "Waiting..."

        elif User != "nothing":
            Computer = random.choices(['rock','paper','scissors'])
            Computer = Computer[0]
            winner = get_winner(User,Computer)
            round = round+1
            convert_round = str(round)
            countdown1()

    elif round == 2:
        if User == "nothing":
            Computer = "nothing"
            winner = "Waiting..."

        elif User != "nothing":
            Computer = random.choices(['rock','paper','scissors'])
            Computer = Computer[0]
            winner = get_winner(User,Computer)
            round = round+1
            convert_round = str(round)
            countdown1()

    elif round >= 3:
        if point_Com == point_User:
            if User == "nothing":
                Computer = "nothing"
                winner = "Waiting..."

            elif User != "nothing":
                Computer = random.choices(['rock','paper','scissors'])
                Computer = Computer[0]
                winner = get_winner(User,Computer)
                round = round+1
                convert_round = str(round)
                countdown1()

        else:    
            print("Game End")
            print("Point Computer "+ str(point_Com))
            print("Point User "+ str(point_User))
            if point_Com < point_User:
                print("You win!!!")
            else:
                print("You lost T-T")
                countdown1()
            break


    #display the information
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "Your Move: " + User,
                (425, 10), font, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "Computer's Move: " + Computer,
                (25, 10), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "Winner: " + winner,
                (200, 300), font, 1, (0, 0, 255), 4, cv2.LINE_AA)
    cv2.putText(frame, "Round: " + convert_round,
                (200, 350), font, 1, (0, 0, 255), 4, cv2.LINE_AA)



    if Computer != "nothing":
        icon = cv2.imread(
           "images/{}.jpg".format(Computer))
        icon = cv2.resize(icon,(200,175))
        frame[25:200,25:225] = icon

    cv2.imshow('Rock Paper Scissors', frame)
    # Press q to close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    print(round)
    print(User)
    print(Computer)
    print(winner)
    print(point_Com)
    print(point_User)


# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()




