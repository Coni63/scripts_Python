"""Fichier d'installation de notre script salut.py."""
import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["configparser", "pyglet", "random", "math"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

# On appelle la fonction setup
setup(
    name = "TSP_ Genetic_Algo",
    version = "1.0",
    description = "Small Genetic Algo to sole the Traveling Salesman Problem",
    options = {"build_exe": build_exe_options},
    executables = [Executable("script_opengl_cleaner.py")]
)