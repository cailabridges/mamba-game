from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
import random

GAME_WIDTH = 800
GAME_HEIGHT = 600
SPEED = 150
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#F4C430"
FOOD_COLOR = "#B80F0A"
BACKGROUND_COLOR = "#000000"


# Main window
window = Tk()
window.title("Snake game")
window.resizable(False, False)

custom_font = font.Font(family='Andora Modern Serif', size=40, weight='normal')
custom_font2 = font.Font(family='Andora Modern Serif',
                         size=80, weight='normal')
custom_font3 = font.Font(family='Andora Modern Serif',
                         size=20, weight='normal')
custom_font4 = font.Font(family='Andora Modern Serif',
                         size=30, weight='normal')
custom_font5 = font.Font(family='Andora Modern Serif',
                         size=15, weight='normal')

# Load images
background_image = Image.open("images/african_safari_background.jpg")
background_image = background_image.resize(
    (GAME_WIDTH, GAME_HEIGHT), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)
snake_head_image = Image.open("images/snake_head.png")
snake_head_image = snake_head_image.resize(
    (SPACE_SIZE, SPACE_SIZE), Image.LANCZOS)
snake_head = ImageTk.PhotoImage(snake_head_image)
snake_body_image = Image.open("images/snake_body.png")
snake_body_image = snake_body_image.resize(
    (SPACE_SIZE, SPACE_SIZE), Image.LANCZOS)
snake_body = ImageTk.PhotoImage(snake_body_image)
snake_tail_image = Image.open("images/snake_tail.png")
snake_tail_image = snake_tail_image.resize(
    (SPACE_SIZE, SPACE_SIZE), Image.LANCZOS)
snake_tail = ImageTk.PhotoImage(snake_tail_image)
food_image = Image.open("images/mouse.png")
food_image = food_image.resize((75, 75), Image.LANCZOS)
food_photo = ImageTk.PhotoImage(food_image)


def set_background(canvas, background_image):
    canvas.create_image(0, 0, anchor=NW, image=background_image)
    # Keep a reference to the image to prevent it from being garbage collected
    canvas.background = background_image


class Snake:
    def __init__(self, canvas):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        self.direction = "right"  # Initial direction
        self.canvas = canvas

        for _ in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = self.canvas.create_image(
                x, y, anchor=NW, image=snake_head, tags="snake")
            self.squares.append(square)

    def update_head(self, direction):
        if direction == "up":
            self.canvas.itemconfig(self.squares[0], image=snake_head)
        elif direction == "down":
            self.canvas.itemconfig(self.squares[0], image=snake_head)
        elif direction == "left":
            self.canvas.itemconfig(self.squares[0], image=snake_head)
        elif direction == "right":
            self.canvas.itemconfig(self.squares[0], image=snake_head)

    def update_tail(self):
        self.canvas.itemconfig(self.squares[-1], image=snake_tail)
        for i in range(1, len(self.squares) - 1):
            self.canvas.itemconfig(self.squares[i], image=snake_body)


class Food:
    def __init__(self, canvas, snake_coordinates):
        self.canvas = canvas
        self.snake_coordinates = snake_coordinates
        self.food_photo = food_photo
        self.spawn_food()

    def spawn_food(self):
        while True:
            x = random.randint(1, (GAME_WIDTH // SPACE_SIZE) - 2) * SPACE_SIZE
            y = random.randint(1, (GAME_HEIGHT // SPACE_SIZE) - 3) * SPACE_SIZE
            if [x, y] not in self.snake_coordinates and y < GAME_HEIGHT - SPACE_SIZE:
                break
        self.coordinates = [x, y]
        self.canvas.create_image(
            x, y, anchor=NW, image=self.food_photo, tags="food")


def next_turn(snake, food):
    global score
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, [x, y])
    snake.update_head(direction)

    square = snake.canvas.create_image(
        x, y, anchor=NW, image=snake_head, tags="snake")
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score : {}".format(score))
        canvas.delete("food")
        food = Food(canvas, snake.coordinates)
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
        snake.update_tail()

    if check_collisions(snake):
        game_over()
        return

    window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):
    global direction
    snake.direction = new_direction
    if new_direction == 'left' and direction != 'right':
        direction = new_direction
    elif new_direction == 'right' and direction != 'left':
        direction = new_direction
    elif new_direction == 'up' and direction != 'down':
        direction = new_direction
    elif new_direction == 'down' and direction != 'up':
        direction = new_direction


def check_collisions(snake):
    x, y = snake.coordinates[0]
    # print("x:", x, "y:", y, "GAME_HEIGHT:", GAME_HEIGHT, "SPACE_SIZE:", SPACE_SIZE)
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT - (SPACE_SIZE*2):
        print("GAME OVER")
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False


def restart_game():
    global score, direction, restart_button
    score = 0
    direction = 'down'
    label.config(text="Score:{}".format(score))
    canvas.delete("all")
    set_background(canvas, background_photo)
    snake.__init__(canvas)
    food.__init__(canvas, snake.coordinates)
    next_turn(snake, food)
    canvas.create_window(GAME_WIDTH // 2, GAME_HEIGHT //
                         2 + 50, window=restart_button)
    restart_button.destroy()


snake_facts = [
    "Green mambas are highly venomous snakes found in eastern Africa.",
    "Green mambas are bright green to blend into the trees where they live.",
    "Green mambas can strike quickly and accurately from a distance.",
    "Green mambas can grow up to 2 meters (6.6 feet) in length.",
    "Green mambas are shy and usually avoid human encounters.",
    "Deforestation and habitat loss are big challenges for these cool snakes.",
    "Green mambas feed on birds, rodents and lizards.",
    "Green mamba venom affects the nervous system, causing paralysis.",
    "Africa is home to over 700 different snake species.",
    "Most African snakes lay eggs, but some give birth to live young.",
    "Many snakes can 'see' heat using special pits on their faces.",
]


def game_over():
    canvas.delete(ALL)

 # Get random fact text
    random_fact = random.choice(snake_facts)

    # Draw the text temporarily to measure its dimensions
    temp_text = canvas.create_text(
        0, 0, font=custom_font5, text=random_fact, anchor=NW)
    text_width = canvas.bbox(temp_text)[2] - canvas.bbox(temp_text)[0]
    text_height = canvas.bbox(temp_text)[3] - canvas.bbox(temp_text)[1]

    # Remove the temporary text
    canvas.delete(temp_text)

    # Calculate box dimensions with padding
    box_padding = 20
    box_width = text_width + 2 * box_padding
    box_height = text_height + 2 * box_padding

    # Calculate box position
    # x-coordinate of the top-left corner of the box
    box_x = GAME_WIDTH // 2 - box_width // 2
    # y-coordinate of the top-left corner of the box
    box_y = GAME_HEIGHT // 2 - box_height // 2 - 200

    # Calculate text position inside the box (centered)
    # x-coordinate of the text (left-padding inside the box)
    text_x = box_x + box_padding
    # y-coordinate of the text (top-padding inside the box)
    text_y = box_y + box_padding

    # Draw rectangular box around FUN FACT and random fact text
    canvas.create_rectangle(box_x, box_y, box_x + box_width, box_y + box_height,
                            outline="white", width=2)

    # Draw FUN FACT and random fact text inside the box (centered)
    canvas.create_text(text_x + text_width // 2, text_y + text_height // 2 - 8,
                       font=custom_font3, text="FUN FACT:", fill="white", anchor=CENTER)
    canvas.create_text(text_x + text_width // 2, text_y + text_height,
                       font=custom_font5, text=random_fact, fill="white", anchor=CENTER)

    # Make the Game Over Text and Restart Button
    canvas.create_text(GAME_WIDTH // 2, GAME_HEIGHT // 2 - 50,
                       font=custom_font2, text="GAME OVER", fill="#B80F0A", tag="gameover")

    global restart_button
    restart_button = Button(window, text="Restart",
                            font=custom_font3, command=restart_game, bg="white")
    canvas.create_window(GAME_WIDTH // 2, GAME_HEIGHT //
                         2 + 50, window=restart_button)


# Remove Restart button after game
restart_button = Button(window, text="Restart",
                        font=custom_font2, command=restart_game)
restart_button.pack_forget()

background_label = Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

score = 0
direction = 'right'

score_frame = Frame(window, bg=BACKGROUND_COLOR)
score_frame.pack(fill=X)
label = Label(score_frame, text="Score : {}".format(score),
              font=custom_font, bg=BACKGROUND_COLOR, fg='white')
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR,
                height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()
set_background(canvas, background_photo)

snake = Snake(canvas)
food = Food(canvas, snake.coordinates)

window_width = GAME_WIDTH
window_height = GAME_HEIGHT
x = int((window.winfo_screenwidth() / 2) - (window_width / 2))
y = int((window.winfo_screenheight() / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))


next_turn(snake, food)
window.mainloop()
