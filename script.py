from stack import Stack

print('\nLet\'s play Towers of Hanoi!')

num_disks = int(input('\nHow many disks do you want to play with? (Should be at least 3)\n'))

# TODO: Create check is string/letter
# while not num_disks.isdigit():
#     num_disks = int(input(
#         '\nAnswer should be a digit...\nHow many disks do you want to play with? ( Should be at least 3)\n'
#     ))

while num_disks < 3:
     num_disks = int(input('\nEnter a number greater or equal to 3\n'))

stacks = []
left_stack = Stack('Left')
middle_stack = Stack('Middle')
right_stack = Stack('Right', num_disks)

stacks.extend([left_stack, middle_stack, right_stack])

for i in range(num_disks, 0, -1):
  left_stack.push(i)

num_optimal_moves = 2 ** num_disks - 1
print('\nThe fastest you can solve this game is in {} move'.format(num_optimal_moves))

def get_input():
    choices = [stack.get_name()[0] for stack in stacks]

    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]

            print('Enter {0} for {1}'.format(name, letter))

        user_input = input('').capitalize()

        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]

num_user_moves = 0

while right_stack.has_space():
    print("\n\n\n...Current Stacks...")

    for stack in stacks:
        stack.print_items()
    
    while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input()
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()

        if from_stack.is_empty():
            print('\nInvalid Move. Try again.')

        if to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break

        print('\nInvalid Move. Try again.')

print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(
    num_user_moves,
    num_optimal_moves
))
