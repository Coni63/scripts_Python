import os
import glob
import PyQt4.uic as pyuic

UI_PATH = os.path.join("..", "UI")
PY_PATH = os.path.join("..", "PyGuiModeles")

def removeOldFiles():
    print("Un peu de menage :")
    for files in (glob.glob(os.path.join(PY_PATH, '*.py'))
                  + glob.glob(os.path.join(PY_PATH, '*.pyc'))):
        if "__init__" not in files:
            print("--> Suppression de " + files)
            os.remove(files)

def createNewFiles():
    print("Generation des fichiers Python GUI :")
    if not os.path.isdir(PY_PATH):
        os.makedirs(PY_PATH)

    for files in os.listdir(UI_PATH):
        name, ext = os.path.splitext(files)
        if ext.lower() != '.ui':
            continue
        if name[0:1] == '_':
            continue

        print("--> Compilation de " + files)
        i = open(os.path.join(UI_PATH, files), 'r')
        o = open(os.path.join(PY_PATH, '%sModele.py' % name), 'w')
        o.write("# noinspection\n#@PydevCodeAnalysisIgnore\n")
        pyuic.compileUi(i, o, execute=True)
        i.close()
        o.close()
        print("build")

def run():
    removeOldFiles()
    createNewFiles()

if __name__ == '__main__':
    run()
    print("Fin d'execution")
    #os.system("PAUSE")