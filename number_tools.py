def is_even(number):
    return number % 2 == 0

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

num = 7

print("Is even:", is_even(num))
print("Is prime:", is_prime(num))
