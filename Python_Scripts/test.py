import gc

#gc.enable()

a = 2
collected = gc.collect()
b = 4
collected = gc.collect()

print("Garbage collector: collected %d objects." % (collected))