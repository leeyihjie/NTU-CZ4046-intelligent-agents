import part_1.value_iteration as VI
import part_1.policy_iteration as PI

# Rename to main to run and other to another name (This main is for Task 1)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        try:
            choice = int(input("Part 1! Input 1 for Value Iteration or 2 for Policy Iteration: "))
        except ValueError:
            print("Input 1 for Value Iteration or 2 for Policy Iteration!")
            continue
        if choice == 1:
            print("Preparing Value Iteration!")
            break
        elif choice == 2:
            print("Preparing Policy Iteration!")
            break
        else:
            print("Input 1 for Value Iteration or 2 for Policy Iteration!")
            continue

    if choice == 1:
        VI.open_file()
        environment = VI.initialise_env()
        print(environment)
        print(f"Displaying initial policy: ")
        VI.print_environment(environment)

        environment = VI.value_iteration(environment)

        optimal_policy = VI.get_optimal_policy(environment)

        # Displaying the Optimal Policy
        print(f"Optimal policy through Value Iteration: ")
        VI.print_policy(optimal_policy)
    elif choice == 2:
        PI.open_file()
        environment, policy = PI.initialise_env()
        print(f"Displaying initial policy")
        PI.print_policy(policy)

        # Policy Iteration
        policy = PI.policy_iteration(policy, environment)

        # Displaying the Optimal Policy
        print(f"Optimal policy through Policy Iteration is ")
        PI.print_policy(policy)



