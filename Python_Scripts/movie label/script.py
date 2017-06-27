import sys, os
import fileinput

extension_vu = "(VU)-"
extension_pas_vu = "(PAS_VU)-"

file = sys.argv[1]

try:
    filename = str(file).split("\\")[-1]
    print("file : ", filename)
    directory = os.path.dirname(file)
    root = os.path.abspath(directory)
    in_fullpath = os.path.join(root, filename)
    print("input path :", in_fullpath)
    if filename[:len(extension_vu)] == extension_vu:
        print("Tu l'as deja vu Blyat !")
        out_fullpath = os.path.join(root, extension_pas_vu + filename[len(extension_vu):])
        print("output path :", out_fullpath)
    elif filename[:len(extension_pas_vu)] == extension_pas_vu:
        print("Tu l'as pas vu celui la ?")
        out_fullpath = os.path.join(root, extension_vu + filename[len(extension_pas_vu):])
        print("output path :", out_fullpath)
    else :
        print("Kurwa, tu viens de regarder", filename)
        out_fullpath = os.path.join(root, extension_vu+filename)
        print("output path :", out_fullpath)
    os.rename(in_fullpath, out_fullpath)
    print("renamed")
except:
    print("Error on", file)
    pass

os.system("PAUSE")