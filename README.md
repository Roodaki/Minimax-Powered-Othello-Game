<div align="center">
  <h1><strong>Minimax-Powered Othello-Game</strong></h1>
  <p><strong>This project highlights a Python-based Othello game with a Pygame GUI, showcasing a robust AI player. The game offers single-player and multi-player modes, with the single-player mode featuring an AI powered by the sophisticated Minimax algorithm with alpha-beta pruning. The AI player employs strategic move evaluation based on diverse criteria, resulting in a challenging and engaging gameplay experience. The project's modular design and well-structured code ensure maintainability and deliver a professional Othello gaming experience enriched by the AI-powered opponent.</strong></p>  
  
![Screenshot (173)](https://github.com/Roodaki/Minimax-Powered-Othello-Game/assets/89901590/159fdda8-1f72-444c-9d14-7ca6d01e53d5)
![Screenshot (175)](https://github.com/Roodaki/Minimax-Powered-Othello-Game/assets/89901590/97a6e7db-234c-4ab7-90fb-a91ce1607a32)
</div>

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage Guide](#usage-guide)

## Features
- `Single-player and Multi-player Modes`: The game offers both single-player and multi-player modes, allowing users to play against an intelligent AI or challenge their friends in a local multiplayer setting.
- `Intelligent AI using Minimax with Alpha-Beta Pruning`: In the single-player mode, the AI opponent is powered by the Minimax algorithm with Alpha-Beta Pruning. The AI evaluates potential moves on the game board to make strategic decisions, providing players with a challenging and competitive gaming experience.
- `Strategic Move Evaluation`: The AI evaluates potential moves based on various criteria, including coin parity (difference in disk count), mobility (number of valid moves), corner occupancy, stability (number of stable disks), and edge occupancy. This strategic move evaluation ensures the AI makes smart and strategic decisions during gameplay.
- `Pygame GUI with Sound Effects`: The game is presented using a Pygame-based graphical user interface, offering an intuitive and visually appealing experience to players. It incorporates various sound cues and effects that trigger during crucial events, such as placing a disc on the board, capturing opponent discs, or when the game concludes with a winner, adding immersion and excitement to the gameplay.
- `Modular Design and Future Enhancements`: The project's modular design and well-structured code allow for easy maintenance and seamless integration of future enhancements. Developers can optimize the AI algorithm, introduce new playing modes, implement different AI difficulty levels, and integrate features like game statistics, ensuring the game's adaptability and continuous improvement.

## Project Structure
The project follows a specific structure to organize its files and directories:
```
Minimax-Powered-Othello-Game/
├── src/
│   ├── ai_agent.py
│   ├── othello_game.py
│   ├── GUI/
│   │   ├── button_gui.py
│   │   ├── menu_gui.py
│   │   └── othello_gui.py
│   └── main.py
├── utils/
│   ├── pictures/
│   └── sounds/
│       ├── disk_flip.mp3
│       ├── end_game.mp3
│       └── invalid_play.mp3
├── .gitignore
└── README.md
```
- `ai_agent.py`: This file contains the implementation of the AI agent for the Othello game. It includes the get_best_move function that uses the Alpha-Beta Pruning algorithm to find the best move for the AI player.
- `othello_game.py`: This file contains the Othello game rules and logic implementation. It defines the OthelloGame class, which manages the game board, validates moves, flips disks, checks for the game's end, and determines the winner.
- `button_gui.py`: This file contains the implementation of a class called Button, which represents a button in a Pygame GUI. It allows for creating interactive buttons with specified text, font, and actions when clicked.
- `othello_gui.py`: This file contains the implementation of a class called OthelloGUI, which represents the graphical user interface (GUI) for playing the Othello game. It displays the game board, handles user input, and runs the main game loop. It also provides sound effects and messaging.
- `menu_gui.py`: This file implements the main menu GUI for the Othello game using Pygame. It provides options to start the game, view credits, or exit. It also includes submenus to choose game modes (multi-player or single-player with AI) and displays credits with the developer's name.
- `main.py`: This is the entry point of the application. It starts the main menu of the Othello game.
- `utils/`: contains pictures and sound files used in the game's GUI and sound effects during gameplay.

## Getting Started
### Requirements
* Python (version 3.0 or higher)
* Pygame library
* Git command line tool (or Git GUI client) to clone the repository.
### Installation
1. Open a terminal or command prompt and clone this repository: `git clone https://github.com/Roodaki/Minimax-Powered-Othello-Game.git`
2. Navigate to the cloned repository's directory and run the main.py file: `python main.py`
### Usage Guide
1. After running the program, the main menu will be displayed with options to start the game, view credits, or exit.
2. Select "Start Game" to choose between "multi-player mode" (play with a friend) or "single-player mode" (play with AI).
3. To make a move during the game, click on an empty cell on the board.
4. The game will display messages for player turns, invalid moves, and the game's result (winner or tie).
