# 20221126
# Creating a custom time tracking generator


from time import time


def track(func_ref):
    def wrapper(*args):
        start = time()
        result = func_ref(*args)
        end = time()
        elapsed_time = end - start
        print(elapsed_time)
        return result
    return wrapper


@track
def magic(n):
    arr = []
    for num in range(n):
        arr.append(num)

    return arr


@ track
def gen_str(word, n):
    result = ''
    for _ in range(n):
        result += word
    return result


print(magic(19))
print(gen_str('abc', 10))
