# Survival of the Fishest


## Short description
A 2D survival game. You start as a small fish, swimming about in an infinitely big world. You score points by eating fish. Be careful though, because other fish can also eat/damage you.
It's an educational game in which you learn what different kinds of fish exist, what they eat and what their natural enemies are. The game also raises awareness of environmental issues such as the pollution of oceans due to plastic waste.


## Game Features
- Health/energy/stamina bars
- Flashlight that can be used for bottom of the ocean
- Camera
- Enemy damage/dying
- Compass that leads you to an enemy in the game
- Boundaries against rock, surface or bottom of the ocean
- AI movement
- Pause/Main Menu
- Score/highscore
- Music
- Optimization FPS/dirty rectangles
- AI control
- Sprite design
- Spawning of sprites

## Potential extra features
- Stamina
- Fish can starve to death
- Fish can multiply when a threshold (food/score/...) is reached
- Texture mapping
- Oceans are deeper
- World design
- Educative elements
- Fishes can eat each other
- Fisherboats are fishing using nets or fishing rods
- Plastic kills fishes
- Game settings adjuster for the player
- Cutscenes
- Special NPC like a mermaid or spooky ghost
- Missions/Quests to explore or fight the plastic pollution


## Dependencies

### Installation
Requirements.txt contains all the required packages needed to run and test
the game.

```
atomicwrites==1.4.0
attrs==20.3.0
colorama==0.4.4
coverage==5.3
iniconfig==1.1.1
packaging==20.7
pluggy==0.13.1
py==1.9.0
pygame==2.0.0
pyparsing==2.4.7
pytest==6.1.2
toml==0.10.2
```

For simple installations, you can use the *pip* command below. Pip is a
package manager for Python packages.

```
pip install -r requirements.txt
```

### Running
To run the game you need the lastest Python version (2.0.0).

```
python3 main.py
```

## Unit testing

There are two different methods you can unit test depending on what operating
system you are using. Each system has the following commands you need to use to
test *vector*, *limit* and *math* classes.

### Windows 10

```
coverage run --omit test_*.py -m pytest;

coverage report -m
```

### Ubuntu 20.04 LTS
On a Linux system, you can use *Makefile* to test. Makefile is used to compile
 a program from source code.
```
command: make
```

## Game controls
- **W, A, S, D** keys are for moving up, left, down, right
- **Arrow** keys can also be used for moving
- Holding **SHIFT** key while pressing one of the move keys will increase both maximum speed and acceleration
- **O** key pauses/plays background music
- **P** key pauses the game
- **ESC** key opens Main Menu and pauses the game
- **Q** key quits the game


## Want to contribute?
Great! We love valuable input. Please email your thoughts and ideas to <r.a.h.m.mathijssen@umail.leidenuniv.nl>.


## Contributors
- Ralph Mathijssen (Team Leader)
- Jun Fei Cheung
- Rutger Homma
- Paula Mieras
- Desley Nijssen
