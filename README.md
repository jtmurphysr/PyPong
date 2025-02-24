# PyPong: A Python Pong Game

PyPong is a classic implementation of the Pong game built with Python's `turtle` module. It is a 2-player game where players control paddles to hit the ball back and forth, aiming to score against their opponent. The game includes paddles, a bouncing ball, and a scoreboard to keep track of the score.

---

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [How to Play](#how-to-play)
- [Game Rules](#game-rules)
- [Code Structure](#code-structure)
- [Future Improvements](#future-improvements)
- [Screenshots](#screenshots)
- [Acknowledgments](#acknowledgments)

---

## Features
- **Two paddles (player-controlled):** 
  - Right paddle controlled by arrow keys.
  - Left paddle controlled by `W` and `S` keys.
- **Ball mechanics:**
  - The ball moves and bounces off walls and paddles.
  - Ball speed increases upon paddle collision.
- **Scoreboard:**
  - Keeps track of both players' scores.
  - Scores update automatically when the ball goes offscreen.
- **Game restart:**
  - The ball resets to the center after a point is scored.

---

## Requirements
- Python 3.10 or higher
- Turtle library (comes pre-installed with Python)

---

## How to Play
1. Clone/download the repository.
2. Run the `pypong.py` file.
   ```bash
   python3 pypong.py
   ```
3. **Controls:**
   - **Left Paddle:** 
     - Move up: Press `W`
     - Move down: Press `S`
   - **Right Paddle:** 
     - Move up: Press the `Up Arrow`
     - Move down: Press the `Down Arrow`

4. Bounce the ball back and forth using the paddles to score against your opponent.

---

## Game Rules
1. When the ball hits the top or bottom boundaries, it bounces back.
2. When the ball hits a paddle, it bounces back and speeds up slightly.
3. If the ball passes a paddle and goes offscreen:
   - A point is awarded to the opponent.
   - The ball resets to the center.

---

## Code Structure

### Files and Directories
- **`pypong.py`:** Main game logic. Sets up the game, handles the loop, events, and conditions.
- **`paddle.py`:** Defines the functionality for the paddles used by the players.
- **`ball.py`:** Handles all ball-related logic, including movement, bouncing, and resetting.
- **`scoreboard.py`:** Displays and updates the scores for both players.

### Class Breakdown
1. **Paddle:**
   - Moves the paddle up or down.
   - Positions the paddles at the correct spot on screen.

2. **Ball:**
   - Moves across the screen.
   - Detects collisions with the walls and paddles.
   - Increases speed after hitting a paddle.

3. **Scoreboard:**
   - Updates and displays the score for both players.
   - Draws the scoreboard on the UI.

4. **Game Setup:**
   - Initializes the screen, paddles, ball, and scoreboard.
   - Listens for keyboard input to control the paddles.
   - Runs the main game loop.

---

## Future Improvements
- **Single-player mode:** Introduce AI to control one paddle for a single-player experience.
- **Custom settings:**
  - Adjustable paddle and ball speeds.
  - Customizable screen size and controls.
- **Enhanced visuals:** Add more graphical elements like a reset animation or paddle/ball effects.
- **Sound effects:** Add sounds for paddle hits, wall bounces, and scoring.
- **Pause/Resume functionality:** Allow players to pause and resume the game.

---

## Screenshots
*(To be added when visuals are available.)*

---

## Acknowledgments
- This project is inspired by the classic Pong game, originally created by Atari in 1972.
- Used Python's powerful `turtle` library for rendering graphics and managing animations.

---

Enjoy playing PyPong! 🏓