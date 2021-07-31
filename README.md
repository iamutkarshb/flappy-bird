# Python Game Development Project
Welcome to flappy-bird!
- Description: A clone of the popular Flappy Bird game using Python
- Language: Python, PYGAME 
- DB: Game Score is store on Local storage.
- Tags: Game development, Python

Instructions to Run
```bash
# Open cmd prompt and go to file directory
cd [file location]
# Activating the Virtual Environment
myenv\scripts\activate
# To start the game
python flappy.py
````

**Note:**

    Project is made according to my favorite play style. If you want to make your own custom game and initialize it to your custom play style. 
    
    Checkout the steps below.

![](https://i.imgur.com/6zM7JBq.png)

Python is a very versatile modern programming language and in this course you will learn basic game development using a python library called pygame.  We will be creating a clone version of the very popular game called flappy bird that made a lot of money for  it's developer few years ago.

Creating a flappy bird clone teach you some very useful practical skills in game development that you can use to create your own games in future.

Follow these steps to build a Game Development project using Python and its ecosystem of libraries:

TODO (Intro):
1. Create game surfaces and main display screen
2. Create basic animation
3. Check for events and how to trigger a response
4. Add scoring to game
5. Import images  onto their own surfaces and embed them in rectangles
6. Position objects on game screen
7. Spawn objects that are triggered by a timer
8. Add sound effects to game
9. Position objects on screen using coordinates

![](https://i.imgur.com/6zM7JBq.png)

For each topic we'll create a CSV file in the following format:
Repo Name,Username,Stars,Repo URL
three.js,mrdoob,69700,https://github.com/mrdoob/three.js
libgdx,libgdx,18300,https://github.com/libgdx/libgdx
Scrape the list of topics from Github

Explain how you'll do it:
use requests to download the page
user Beautiful soup to parse and extract information
convert to Pandas Dataframe

1. **Environment Setup**
    - Create a ***Python file***. 
    - ***Import*** *pygame*
    - ***Initialize*** *pygame*
    - Create ***display surface*** (*canvas*) to draw game images.
        - It includes Display size
        - and Frame per second at which the display will be updated for smooth function of game 
    - ***Game loop:*** *Contains game logic*
    - ***Quit game***

    ```mermaid
    graph TD
        Initialize Pygame --> Display Surface(canvas);
        Display Surface(canvas) --> Game Logic;
        Game Logic --> Quit Game;
    '''
2. **Building Flappy Bird Game**

this section will be added by 17:30 stay tuned till then, btw projet is still working, give it a go and see if you can crack the code on how to build this

Project is completed customize it to your favorite playing style, like I did. All u need to do it change timeframe to increase speed difficulties. or you can change the soundboard attach to your liking.
