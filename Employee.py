# Expert System for Employee Performance Evaluation

def get_input(question):
    while True:
        ans = input(question + " (yes/no): ").strip().lower()

        if ans in ["yes", "no"]:
            return ans

        print("Please enter only 'yes' or 'no'.")


def employee_expert_system():

    print("======================================")
    print(" Employee Performance Evaluation ")
    print("======================================\n")

    print("Answer the following questions:\n")

    # Employee evaluation questions
    punctual = get_input("Is the employee punctual?")
    teamwork = get_input("Does the employee work well in a team?")
    targets = get_input("Does the employee complete targets on time?")
    communication = get_input("Does the employee have good communication skills?")
    leadership = get_input("Does the employee show leadership qualities?")
    discipline = get_input("Is the employee disciplined?")

    print("\n===== Evaluation Result =====")

    # Expert system rules
    if (punctual == "yes" and teamwork == "yes" and
        targets == "yes" and communication == "yes" and
        discipline == "yes"):

        print("Performance Level : Excellent")
        print("Recommendation    : Promotion / Reward")

        if leadership == "yes":
            print("Leadership Skill  : Strong")

    elif (targets == "yes" and teamwork == "yes" and
          communication == "yes"):

        print("Performance Level : Good")
        print("Recommendation    : Appreciation and Growth Opportunities")

    elif (punctual == "yes" or discipline == "yes"):

        print("Performance Level : Average")
        print("Recommendation    : Needs Improvement in Work Performance")

    else:

        print("Performance Level : Poor")
        print("Recommendation    : Training and Close Supervision Required")


# Run the expert system
employee_expert_system()