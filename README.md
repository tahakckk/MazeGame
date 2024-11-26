# MazeGame

MazeGame is a competitive maze-solving game where the player competes against an AI to navigate through a randomly generated maze. The game includes treasures, penalties for wrong paths, and a scoring system. The goal is to reach the maze's end with the highest score.

## Features
- **Two-player Competition**: One player and one AI solve the maze simultaneously.
- **Treasure System**: Randomly placed treasures in the maze provide additional challenges.
- **Scoring**:
  - Collect treasures to increase your score.
  - Wrong paths decrease the score.
- **Dynamic Pathfinding**: The AI navigates the maze using random path exploration.
- **Visuals**: The game uses the `turtle` graphics module to render the maze and player movements.

## Technologies Used
- **Python**: Core programming language for the project.
- **Turtle Graphics**: Used for rendering the maze and visualizing player movements.
- **Threading**: Handles concurrent actions of the player and AI.
- **mttkinter**: Enhances the graphical interface with tkinter multithreading capabilities.

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/tahakckk/MazeGame.git
2. Navigate to the project directory:
   ```bash
   cd MazeGame
3. Install the required Python libraries:
   ```bash 
   pip install mttkinter

# How to Play
1. Run the game using the following command:
   ```bash
   python maze_game.py

The game window will open, showing the maze.
Player Controls:
Use the arrow keys (Up, Down, Left, Right) to navigate.
Objective: Reach the maze's end with the highest score, avoiding penalties and collecting treasures.

2. If you want to see a screen where the AI competes with itself, use the following command to run the game:  
   ```bash
   python maze_game.py

# Game Rules
Treasures are randomly scattered in the maze and grant bonus points when collected.
Entering a dead-end subtracts points and increases your "wrong ways" count.
The AI competes to finish the maze before you. Try to beat it!

# File Structure
maze_game.py: Main game logic and execution script.
README.md: Documentation file.
Other files: Supporting resources (if applicable).

# License 
This project is licensed under the MIT License. See LICENSE for more details.

# Screenshots
User and AI compete with each other :
![Ekran Alıntısı](https://github.com/user-attachments/assets/0df54874-1fdd-4372-9389-946636906d01)
The results of the user and AI competing with each other :
![Ekran Alıntısı1](https://github.com/user-attachments/assets/be7a2c45-a822-45e2-9dae-b9eabdf0a271)
AI competes with itself in 4 different ways :
![Ekran Alıntısı2](https://github.com/user-attachments/assets/a2f7d02e-bab6-45ea-b72a-f05933dae685)
The results of AI competing with itself in 4 different ways :
![Ekran Alıntısı3](https://github.com/user-attachments/assets/7c0240ae-6148-40cd-ac71-0ca7a42fa426)

# Contribution 
Contributions are welcome! Feel free to fork the repository, create a feature branch, and submit a pull request.

# Contact 
For questions or feedback, please open an issue in this repository.

## Happy gaming! 🎮

