set p=%cd%
set /P quality="Quality value [l|m|h|q|k]: "
python -m manim %p%\scene.py CupSwapperScene -q %quality%
Pause