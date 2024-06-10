# Maza-thon Game: A Maze Adventure

This project is a simple maze game implemented in Python using the `tkinter` library for the GUI and the `turtle` module for graphics. 

## Game Mechanics

* **Maze Generation:** The game uses a text-based representation to create a maze layout. Characters like 'X' denote walls, 'P' is the player's starting position, 'T' marks treasures, and 'E' indicates enemies.
* **Player Movement:** The player, represented by a turtle character, can move within the maze using arrow keys (or alternative key sets). Walls restrict movement.
* **Treasures:** Collecting treasures scattered throughout the maze increases the player's score.
* **Enemies:** Enemies move randomly and chase the player when they get close.  
* **Game Over:** The player loses if they collide with enemies too many times.

## Code Structure

The code is organized into classes and functions:

* **Classes:**
    * `Pen:` Used to draw the maze and other elements.
    * `Player:` Controls the player character's movement and interaction with other objects.
    * `Treasure:` Represents treasures in the maze.
    * `Enemy:` Controls enemy behavior (random movement, chasing the player).

* **Functions:**
    * `startgame:` Initializes the game window, sets up the maze, and handles game logic.
    * `set_maze:` Converts the text-based maze into a visual representation using turtle graphics.
    * `menu:` Displays the main menu with options to start, adjust settings, or quit.
    * `Settings:` Allows changing background or control schemes.
    * `Controls:` Provides options for different key bindings.

## Main Game Loop

The game loop continuously:

1. Checks for collisions between the player and treasures/enemies.
2. Updates the player's score if a treasure is collected.
3. Triggers enemy movement.
4. Refreshes the game window.

## Key Improvements (Potential)

* **More Levels:** Introduce additional maze layouts for increased replayability.
* **Power-Ups:** Add power-ups that give the player temporary abilities (e.g., speed boost, invincibility).
* **Graphical Enhancements:** Improve the visual appearance using custom graphics instead of basic turtle shapes.
* **Sound Effects:** Incorporate sound to make the game more immersive.
* **Difficulty Settings:** Allow players to choose the number of enemies or their speed.


Feel free to explore and modify the code to create your own maze adventures!

**Keywords:** Python, tkinter, turtle, game development, maze
