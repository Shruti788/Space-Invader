# 🚀 Space Invaders

A simple 2D Space Invader game built using **Python** and **Pygame**. Defend the galaxy against incoming alien forces in this retro-inspired shooter!



---

## ✨ Features

* **Classic Arcade Gameplay:** Move your spaceship and shoot incoming aliens.  
* **Multiple Enemies:** Six aliens with simple movement patterns.  
* **Sound Effects & Music:** Background music and bullet/explosion sounds.  
* **Score Tracking:** See your score as you destroy enemies.  
* **Game Over & Restart:** Game ends when aliens reach the bottom, press ENTER to restart.


---

## 🛠️ Installation

### Prerequisites

This project requires **Python 3.x** and the **Pygame** library.

1.  **Clone the repository** (or download the files):
    ```bash
    git clone [YOUR_REPOSITORY_URL_HERE]
    cd space-invaders
    ```

2.  **Install Pygame:**
    ```bash
    pip install pygame
    ```

3.  **Ensure Media Files:**
    This project relies on a `media` folder containing all the images and sound files. Make sure the following files are present in a subdirectory named `media/` relative to your main game script:

    * `space_stars.jpg` (Background Image)
    * `retro27.mp3` (Background Music)
    * `rocket.png` (Icon)
    * `arcade-game.png` (Player Image)
    * `ufo.png` (Enemy Image)
    * `bullet.png` (Bullet Image)
    * `explosion.mp3` (Explosion Sound)
    * `crash.mp3` (Game Over Sound)

---

## ▶️ How to Run

After installing the prerequisites, simply run the main Python script from your terminal:

```bash
python your_game_script_name.py
```

## 🎮 Controls

* **Left Arrow (←):** Move player left
* **Right Arrow (→):** Move player right
* **Spacebar:** Fire bullet
* **ENTER (Game Over Screen):** Restart Game
* **Window Close:** Quit Game

## 📜 Code Overview

The game logic is contained within a single file, utilizing Pygame's main loop structure.
* Initialization: Sets up Pygame, screen dimensions `(800x600)`, title, icon, and background sound.
* Assets Loading: Loads all image and sound assets from the `media`/ folder.
* Game State Variables: Manages player position, enemy positions (using lists for multiple enemies), bullet state `("ready" or "fire")`, and the current score.
* Functions: Modular functions handle tasks such as drawing the player/enemy, firing the bullet, displaying the score, rendering the game-over screen, and most critically, collision detection (using the distance formula from the `math` module).
* Main Loop (while running):
  * Handles events (key presses, window close).
  * Manages player movement and boundary checks.
  * Updates enemy movement (side-to-side and downward progression).
  * Checks the Game Over condition (if an enemy reaches a specific `Y` coordinate).
  * Handles collision logic between bullets and enemies, rewarding the player with score points and resetting the enemy's position.
  * Updates the screen with new positions and the current score.




