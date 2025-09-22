# Python Template using Raylib


## main.py

The main.py entry file is minimal and only instanciates a singleton Application and calls the run method.

## app.py

The singleton Application class, has only three variables **WINDOW_WIDTH**, **WINDOW_HEIGHT** and **TITLE**

Runs the Application until it quits, calls the **engine.update()** and **engine.draw()** methods

## engine.py

Initialization
+ set reference to the **app** instance
+ **load_fonts()**

Font loaded are only **AdwaitaMonoNerdFont_Regular_24** there are more fonts in the resource/fonts/AdwaitaMono folder you can use if needed.

Engine updates can be import other methods for updates in larger projects, same with draw. You might want to seperate the debug draw methods into it's own class with methods to draw debugs.

The 3D scene code is just a placeholder replace it with whatever is needed to get you going.