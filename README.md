# Cup Swapper
Code to emulate a cup swapping game using 3blue1brown's animation engine [Manim](www.github.com/3b1b/manim/). 

The init file contains raw code to find the last cup, which is not used in the animation code.

The scene.py file, when ran with [Manim](www.github.com/3b1b/manim/), will generate a video in /media/videos/scene/480p15/ that contains the animation of the cups being moved.

Both pieces of code run by giving them  a list of paths, which could look like this:

    ["AB","BC","AC","BA"]
    ["CA","BA","BA","BC","AB","CA"]
   
   where each "path" in the list contains two letters reffering to the cups to be swapped. In the init file, it takes it as an argument to the `swapper()` function, and in the scene.py file, it takes it as the `PATHS` variable defined near the top if the file.

To run the scene.py file so that it generates the video, you will first need to clone the repository to your local computer and install [Manim](www.github.com/3b1b/manim/) (instructions for installing [Manim](www.github.com/3b1b/manim/) can be found [here](https://docs.manim.community/en/stable/installation.html)). After this, open  cmd, navigate to the directory containing scene.py, and run this command: `python -m manim -pql scene.py CupSwapperScene` (can also be found commented at the bottom of scene.py). The code will then generate the video.
