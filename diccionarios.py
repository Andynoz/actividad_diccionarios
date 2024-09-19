juegos={
    'Juan': 17,
    'Mario': 18,
    'Maria': 20,
}
juegos.update({
    'David': 15,
    'Camilo': 16,
})
del(juegos['Mario'])
for i,j in juegos.items():
    print(i,j)