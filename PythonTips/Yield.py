# We should use yield when we want to iterate over a sequence,
# but don’t want to store the entire sequence in memory
def simple_generator():
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
for value in simple_generator():
    print(value)


def next_square():
    i = 1
    # An Infinite loop to generate squares
    while True:
        yield i * i
        i += 1  # Next execution resumes
        # from this point


# Driver code to test above generator
# function
for num in next_square():
    if num > 100:
        break
    print(num)
