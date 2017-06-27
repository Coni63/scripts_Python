arr = ['data1', 'data2', '\\u0643\\uFEBD', '\\u0643\\uFEBD']

#test = "test \\u0643\\uFEBD"

def f(string):
    return string.encode("utf-8").decode('unicode-escape')

arr = list(map(f, arr))
print(arr)


dic = {'foo': 1, 'bar': 2}
L = ['foo', 'bar', 'baz']

list_values = sum([ 1 for k in dic.keys() if k in L])
print(list_values)

list_values = sum(1 for k in L if k not in dic.keys())
print(list_values)

L = set(dic.keys())
L2 = set(['foo', 'bar', 'baz'])

print(len(L2) - len(L & L2))

print("Welcome to the Pig Latin Translator!")

# Start coding here!
original = input("Enter a word:")

if original.isalpha():
    print(original)

else:
    print("empty")

a = 0
if a:
    print("go")
else:
    print("nogo")


def replace_with_emoji(ch):
    emojis = {"panda": u"\U0001f43c", "bear": u"\U0001f43b", "dog": u"\U0001f43a",
              "cat": u"\U0001f63a", "eye": u"\U0001f441", "ear": u"\U0001f442", "nose": u"\U0001f443",
              "mouth": u"\U0001f444", "crown": u"\U0001f451", "glasses": u"\U0001f453", "jeans": u"\U0001f456",
              "boy": u"\U0001f466", "girl": u"\U0001f467", "ghost": u"\U0001f47b", "pill": u"\U0001f48a",
              "bomb": u"\U0001f4a3", "poo": u"\U0001f4a9", "money": u"\U0001f4b5", "phone": u"\U0001f4f1",
              "television": u"\U0001f4fa", "radio": u"\U0001f4fb", "key": u"\U0001f511", "lock": u"\U0001f512",
              "bell": u"\U0001f514", "fire": u"\U0001f525", "hammer": u"\U0001f528", "knife": u"\U0001f52a",
              "pistol": u"\U0001f52b", "microscope": u"\U0001f52c", "telescope": u"\U0001f52d",
              "hamburger": u"\U0001f354",
              "pizza": u"\U0001f355", "sushi": u"\U0001f363", "doughnut": u"\U0001f369", "cookie": u"\U0001f36a",
              "chocolate": u"\U0001f36b", "cocktail": u"\U0001f378", "wine": u"\U0001f377", "beer": u"\U0001f37a",
              "popcorn": u"\U0001f37f", "headphone": u"\U0001f3a7", "guitar": "F0 9F 8E B8"}

    for key, code in emojis.items():
        ch = ch.replace(key, code)
    return ch


message = input("Entrez un message: ")
print(replace_with_emoji(message))