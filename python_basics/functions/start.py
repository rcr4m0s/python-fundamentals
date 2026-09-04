def analyze_numbers(numbers):
    maximum = numbers[0]
    minimum = numbers[0]
    total = 0


    for number in numbers:

        total += number
        if number > maximum:
            maximum = number
        elif number < minimum:
            minimum = number

    average = total/len(number)

    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")
    print(f"Total: {total}")
    print(f"Average: {average}")

user = []

for i in range(5):
    wow = float(input(f"Enter number {i + 1}: "))
    user.append(wow)


analyze_numbers(user)




