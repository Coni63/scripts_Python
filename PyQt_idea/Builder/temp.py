from cx_Freeze import setup, Executable

setup(
	name="Your Program",
	version="1.0",
	description="First Script :)",
	executables=[Executable("C:/Users/Nicolas/PycharmProjects/MovieDB/classes.py")],
)