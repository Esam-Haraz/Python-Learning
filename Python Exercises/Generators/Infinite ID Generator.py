def id_generator():
    id_gen = 0
    while True:
        id_gen += 1
        yield id_gen
userid = id_generator()

print(next(userid))
print(next(userid))
print(next(userid))
print(next(userid))
print(next(userid))