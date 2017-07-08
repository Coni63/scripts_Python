from cx_Freeze import setup, Executable

setup(
	name="DO Boost",
	version="1.0",
	description="Calculate the boost with diams",
	option = {"build_exe":["function.py", "Classes_UI.py", "Classes.py", "PyGuiModeles/mainModele.py", "PyGuiModeles/about_meModele.py"], "include_files": ["icon.png"]},
	requires=['PyQt4']
	executables=[Executable("script.py")],
)