# Mamba Game

## Table of Contents
* [About](#about-mamba-game)
* [Video](#mamba-game-walkthrough-video)
* [Technologies](#technologies)
* [Code Examples](#code-examples)
* [Features](#mamba-game-features)
* [Status](#status)
* [Why Mamba Game](#why-mamba-game)
* [Contact](#contact)

## About Mamba Game
The Mamba game offers a unique African twist on the classic snake game, immersing players in the vibrant ecosystem of Africa. As players use their keys to maneuver the hungry snake to find its prey, they not only enjoy the thrill of the game but also gain valuable insights about the natural world. The game integrates educational elements, such as intriguing fun facts about snakes and the African green mamba, to become an engaging learning platform for young and old alike.

## Mamba Game Walkthrough Video
[Mamba Game Walkthrough Video](https://youtu.be/u3x1Lev1qz8)

## Technologies
Python

## Code Examples

```
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

```
```
def check_collisions(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT - (SPACE_SIZE*2):
        print("GAME OVER")
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False
```
## Mamba Game Features
* Incorporates education by providing interesting facts about snakes, including green mambas, at the end of the gameplay.
* Offers immersive graphics, featuring high-quality images of African wildlife, including the green mamba.
* Provides intuitive controls, allowing players to navigate the snake effortlessly.
* Enhances the user experience through music that fits the game's theme.  


To-Do List:
* Add features for scoreboard and options of speed/color etc.

## Status
Completed (on-going)


## Why Mamba Game?
I created the Mamba Game as a tribute to my love for Afro beats and the captivating essence of The Lion King. Fond memories of playing the classic snake game as a child inspired me to blend nostalgia with modern technology. Through this project, I aimed to enhance my Python programming skills, leveraging its versatility to ensure a seamless and enjoyable gameplay experience, combining my passion for coding with my appreciation for African culture and childhood favorites.

## Contact
Created by [Caila Bridges](https://www.linkedin.com/feed/)
