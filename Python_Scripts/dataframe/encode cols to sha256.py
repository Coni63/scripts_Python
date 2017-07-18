import pandas as pd
import hashlib

email = ["toto@tata.com" , "toto2@tata.com", "toto@tat2a.com" , "todsfqfgto@tata.com" , "toqsgto@tata.com" , "totgqdfgo@tata.com"  ]

dataframe = pd.DataFrame({'clear':email})
print(dataframe)

dataframe["encode"] = [hashlib.sha256(each.encode('utf-8')).hexdigest() for each in dataframe["clear"]]

print(dataframe)