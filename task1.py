
my_str = 'Слава неабв лучший препод на GB и у него неабв топовый дискорд'.split()

print(" ".join([i for i in my_str if 'абв' not in i]))
