def hammingDistance(x, y):
    # ^ is bitwise xor
    # bin() convert an integer to binary in str type
    # count() is used to count the times of 1
    return bin(x^y).count("1")
