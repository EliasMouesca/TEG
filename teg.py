#!/bin/python3

from itertools import product
import sys

max_suggestion = 3              # You can enter more, but it will take some time. Also, rules specify a maximum of 3 dices.
max_warning_enabled = True

# 'calculate' receives the number of dices each player is using and returns a list with the probablity of each outcome
def calculate(attack_num_of_dices, defense_num_of_dices):
    number_of_posible_cases = min(attack_num_of_dices, defense_num_of_dices) + 1
    attacker_performance = [0] * number_of_posible_cases
    number_of_posible_cases = 0
    number_of_dices = attack_num_of_dices + defense_num_of_dices

    for roll in product([1, 2, 3, 4, 5, 6], repeat=number_of_dices):
        attack = list(roll)[:attack_num_of_dices]
        defense = list(roll)[-defense_num_of_dices:]

        number_of_posible_cases += 1
        attacker_performance[win_count(attack, defense)] += 1

    for i in range(0, len(attacker_performance)):
        attacker_performance[i] /= number_of_posible_cases

    return attacker_performance


# The win count is the number of dice rolls the attacker won. For example: if the outcome of the battle was a:6_3_2 d:6_4_1, the win count would be 1 (the attacker lost the first dice 6:6, lost the second dice 3:4 and won the third 2:1
def win_count(attack_arr, defense_arr):
    win_count = 0
    attack_arr.sort(reverse = True)
    defense_arr.sort(reverse = True)
    number_of_rolls = min(len(attack_arr), len(defense_arr))

    for i in range(0, number_of_rolls):
        if (attack_arr[i] > defense_arr[i]): win_count += 1

    return win_count


def main():
    # Args
    if (len(sys.argv) == 3):
        attack_num_of_dices = int(sys.argv[1])
        defense_num_of_dices = int(sys.argv[2])
    else:
        print_usage()
        exit(0)
    
    # No negatives..
    if (attack_num_of_dices <= 0 or defense_num_of_dices <= 0):
        print("Number of dices must be strictly positive")
        exit(1)

    # If needed, warn about the maximum dices allowed
    if (attack_num_of_dices > max_suggestion or defense_num_of_dices > max_suggestion): 
        if (max_warning_enabled): print (f"Rules specify a maximum of {max_suggestion} dices...\n")

    # ---- Begin actual calculations ----
    print (f"Attack: {attack_num_of_dices}  \tDefense: {defense_num_of_dices}\n")

    # 'results' is a list; the index is the number of rolls the attacker one, and the value the chance of that happening. ie. 'results[1] = 0.23' means that the chance of the attacker winning 1 and only 1 dice roll is 0.23
    results = calculate(attack_num_of_dices, defense_num_of_dices)

    favorable_result_chance = .0
    neutral_result_chance = .0
    score = .0
    average_loss = .0
    number_of_rolls = min(attack_num_of_dices, defense_num_of_dices)

    for i in range(0, len(results)):
        if (results[i] != 0.0): 
            print(f"Attacker wins {i}: {round(results[i] * 100, 2)}%")
            score += (i - number_of_rolls / 2) * results[i] * 100
            average_loss += (number_of_rolls - i) * results[i]
            if (i > number_of_rolls / 2): favorable_result_chance += results[i]     # If this is true, the attacker won more than he lost: favorable result
            if (i == number_of_rolls / 2): neutral_result_chance += results[i]      # Both attacker and defender lost the same amount: neutral result

    print (f"\nScore: {round(score, 2)}")
    print (f"Average loss: {round(average_loss, 2)}")
    
    print (f"\nFavorable result for attacker: {round(favorable_result_chance * 100, 2)}%")
    if (neutral_result_chance != 0.): print (f"Neutral result: {round(neutral_result_chance * 100, 2)}%")

    exit(0)         # main


def print_usage():
    print(f"Usage: \t{sys.argv[0]}\n\t{sys.argv[0]} <# of attacker dices> <# of defender dices>")


if __name__ == '__main__':
    main()

