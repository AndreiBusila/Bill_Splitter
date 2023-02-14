import random


def input_number_of_friends():
    user_input = int(input("Enter the number of friends joining (including you):\n"))
    print()
    if user_input > 0:
        return user_input
    else:
        print("No one is joining for the party")
        return None


def input_name(number):
    names = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(number):
        user_input = input()
        names[user_input] = 0.0
    print()
    return names


def input_bill_value():
    user_input = int(input("Enter the total bill value:\n"))
    print()
    return user_input


def input_lucky_choice():
    user_input = input("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:\n")
    print()
    if user_input == "Yes":
        return True
    elif user_input == "No":
        return False


def generate_random_lucky(lists):
    lucky_name = random.choice(list(lists.keys()))
    print("{} is the lucky one!".format(lucky_name))
    print()
    return lucky_name


def main():
    number_of_friends = input_number_of_friends()
    if number_of_friends is None:
        return
    list_with_names = input_name(number_of_friends)
    bill_value = input_bill_value()

    lucky_name = ""
    if input_lucky_choice():
        lucky_name = generate_random_lucky(list_with_names)
        number_of_friends = number_of_friends - 1
    else:
        print("No one is going to be lucky")

    split_bill = round(bill_value / number_of_friends, 2)
    for keys in list_with_names:
        if keys == lucky_name:
            continue
        list_with_names[keys] = split_bill
    print(list_with_names)


main()
