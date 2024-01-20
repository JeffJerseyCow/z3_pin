from z3 import *


def constrain_values(solver, value_list):
    for value in value_list:
        solver.add(value >= 1, value <= 9)


def check_sat_print(solver, value_list, constraint_set):
    while solver.check() == sat:
        model = solver.model()

        output = ''.join([str(model[value]) for value in value_list])
        constraint_set.add(output)

        new_constraints = [value != model[value] for value in value_list]
        solver.add(Or(new_constraints))


def print_consecutive_digits_model(value_list, constraint_set):
    solver = Solver()
    constrain_values(solver, value_list)

    constraints = []
    for position in range(0, len(value_list) - 3):
        constraints.append(And([
            value_list[position] == value_list[position + 1] - 1,
            value_list[position + 1] == value_list[position + 2] - 1,
            value_list[position + 2] == value_list[position + 3] - 1])
        )
    solver.add(Or(constraints))

    check_sat_print(solver, value_list, constraint_set)


def print_three_repeated_digits_model(value_list, constraint_set):
    solver = Solver()
    constrain_values(solver, value_list)

    constraints = []
    for position in range(0, len(value_list) - 2):
        constraints.append(And([
            value_list[position] == value_list[position + 1],
            value_list[position + 1] == value_list[position + 2]])
        )
    solver.add(Or(constraints))

    check_sat_print(solver, value_list, constraint_set)


def print_two_repeated_digits_model(value_list, constraint_set):
    solver = Solver()
    constrain_values(solver, value_list)

    constraints = []
    for position in range(0, len(value_list) - 3):
        constraints.append(And(
            value_list[position] == value_list[position + 1],
            value_list[position + 2] == value_list[position + 3])
        )
    solver.add(Or(constraints))

    check_sat_print(solver, value_list, constraint_set)


def print_two_consecutive_digits_model(value_list, constraint_set):
    solver = Solver()
    constrain_values(solver, value_list)

    constraints = []
    for position in range(0, len(value_list) - 3):
        constraints.append(And(
            value_list[position] == value_list[position + 1] - 1,
            value_list[position + 2] == value_list[position + 3] - 1)
        )
    solver.add(Or(constraints))

    check_sat_print(solver, value_list, constraint_set)


def main():
    import sys

    try:
        length = int(sys.argv[1])
    except IndexError:
        print('Please provide a length')
        return
    except ValueError:
        print('Please provide an integer')
        return

    constraint_set = set()

    value_list = [Int(str(i)) for i in range(0, length)]

    print_consecutive_digits_model(value_list, constraint_set)
    print_three_repeated_digits_model(value_list, constraint_set)
    print_two_repeated_digits_model(value_list, constraint_set)
    print_two_consecutive_digits_model(value_list, constraint_set)

    for item in constraint_set:
        print(item)
