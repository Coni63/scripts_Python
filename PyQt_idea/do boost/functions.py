def convert(number):
    notation = ["", "k", "m", "M", "b", "B", "C", "kC", "mC", "MC", "bC", "BC"]
    txt = notation + [notation[n%6] + "C<sup>" + str(n//6) + "</sup>" for n in range(12,50)]
    splitted_number = "{:,}".format(number).split(",")
    if len(splitted_number) >= 2:
        result = splitted_number[0] + "." + splitted_number[1] + " " + txt[len(splitted_number)-1]
    else:
        result = str(number)
    return result