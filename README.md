# 🐍 Python Maze Game

A two-level interactive maze game developed using **Python and Turtle** during my Software Development apprenticeship.

This was my first substantial programming project and one of the projects that helped develop my interest in software development.

> This repository preserves the project largely as it was originally developed during my apprenticeship. Earlier versions have also been retained to show how the application evolved throughout development.

---

## 📖 About the Project

The Python Maze Game is a grid-based game where the player navigates through maze levels while collecting items, avoiding threats and progressing through the game.

The project was developed incrementally, with new functionality introduced and tested across multiple versions.

The final version includes two different levels, player movement, collision detection, collectible items, scoring and moving enemies with different behaviours.

---

## ✨ Features

The application includes:

- Two playable maze levels
- Grid-based player movement
- Wall and collision detection
- Collectible coins and scoring
- Moving threats
- Proximity-based enemy behaviour
- Level progression
- Custom game assets
- Object-oriented game components

---

## 🛠️ Built With

- **Python**
- **Turtle**
- Object-oriented programming
- Grid-based level design
- Movement and collision logic

---

## 📸 Application

### Level 1

![Python Maze Game - Level 1](docs/maze-game-level-1.png)

### Level 2

![Python Maze Game - Level 2](docs/maze-game-level-2.png)

---

## 📂 Repository Structure

```text
python-maze-game/
│
├── src/
│   ├── maze_game.py
│   └── [game assets]
│
├── development-history/
│   ├── maze_game_v1.py
│   ├── maze_game_v2.py
│   ├── maze_game_v3.py
│   ├── maze_game_v4.py
│   ├── maze_game_v4_1.py
│   └── maze_game_v4_2.py
│
├── docs/
│   ├── maze-game-level-1.png
│   └── maze-game-level-2.png
│
├── README.md
└── .gitignore
```

---

## ▶️ Running the Project

The game is a desktop application built using Python's Turtle graphics module.

Clone the repository:

```bash
git clone https://github.com/NunoQPS/python-maze-game.git
```

Navigate to the source directory:

```bash
cd python-maze-game/src
```

Run the application:

```bash
python maze_game.py
```

The game assets included in the `src` directory should remain alongside the Python file so the original asset paths continue to work correctly.

---

## 🎓 Project Background

This project was originally developed during my Software Development apprenticeship and was my first substantial programming project.

It was built independently as an assessment project and gave me early practical experience turning programming concepts into a complete working application.

Through the project, I gained experience with:

- Object-oriented programming
- Grid-based movement and collision detection
- Game state and level progression
- Implementing different enemy behaviours
- Breaking a larger problem into smaller pieces of functionality
- Incrementally testing functionality during development

Development took place across multiple versions as functionality was introduced and tested. These earlier versions are preserved in the [`development-history`](development-history/) directory.

The original implementation has intentionally been preserved rather than rewritten using my current knowledge.

---

## 💭 What I'd Improve Today

Looking back at this project with the software engineering experience I've developed since building it, there are several areas I would approach differently today.

I would:

- Split the application into smaller modules rather than keeping most of the game logic in a single file
- Improve separation of responsibilities between game components
- Reduce duplicated logic and create more reusable functionality
- Apply more consistent naming and code formatting
- Separate level data from application logic
- Add automated tests for game logic where appropriate
- Improve documentation and error handling
- Use Git throughout development rather than maintaining separate version files

These improvements reflect how my approach to designing and maintaining software has developed since completing the original project.

---

## 🔄 Development Journey

This project represents one of the earliest stages of my software development journey.

Rather than retrospectively rewriting the original application to reflect my current abilities, I have preserved the code largely as it was developed during my apprenticeship.

My more recent projects demonstrate how my approach has evolved across areas such as application architecture, database design, source control, testing and structured development.

Keeping the original implementation alongside my newer work provides a clear record of that progression.
