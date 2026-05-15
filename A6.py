# Expert System - Employee Performance Management
# Artificial Intelligence Practical

print("=" * 60)
print("     EXPERT SYSTEM : EMPLOYEE PERFORMANCE MANAGEMENT")
print("=" * 60)

# ----------------------------------------------------------
# THRESHOLDS
# ----------------------------------------------------------
# Score 0  - 25  : EXCELLENT
# Score 26 - 50  : GOOD
# Score 51 - 70  : AVERAGE
# Score 71 - 85  : POOR
# Score 86 - 100 : CRITICAL PERFORMANCE
# ----------------------------------------------------------

def get_verdict(score):

    if score <= 25:
        return (
            "EXCELLENT PERFORMANCE",
            "Employee is performing exceptionally well.\n"
            "Eligible for promotion and bonus."
        )

    elif score <= 50:
        return (
            "GOOD PERFORMANCE",
            "Employee performance is good.\n"
            "Minor improvements can increase productivity."
        )

    elif score <= 70:
        return (
            "AVERAGE PERFORMANCE",
            "Employee performance is average.\n"
            "Training and guidance are recommended."
        )

    elif score <= 85:
        return (
            "POOR PERFORMANCE",
            "Employee performance is below expectations.\n"
            "Performance improvement plan required."
        )

    else:
        return (
            "CRITICAL PERFORMANCE",
            "Employee performance is critically low.\n"
            "Immediate action and strict monitoring required."
        )

# ----------------------------------------------------------
# EMPLOYEE CHECK
# ----------------------------------------------------------

def employee_check():

    score = 0
    issues = []

    print("\n" + "-" * 60)
    print("           EMPLOYEE PERFORMANCE ANALYSIS")
    print("-" * 60)

    # Attendance
    attendance = int(input("\nEnter Attendance Percentage: "))

    if attendance < 50:
        score += 35
        issues.append("Very Low Attendance")

    elif attendance < 75:
        score += 20
        issues.append("Low Attendance")

    # Task Completion
    task = int(input("Enter Task Completion Percentage: "))

    if task < 40:
        score += 30
        issues.append("Very Low Task Completion")

    elif task < 70:
        score += 15
        issues.append("Low Task Completion")

    # Communication Skills
    communication = int(input("Enter Communication Skill Rating (1-10): "))

    if communication <= 3:
        score += 20
        issues.append("Poor Communication Skills")

    elif communication <= 6:
        score += 10
        issues.append("Average Communication Skills")

    # Teamwork
    teamwork = int(input("Enter Teamwork Rating (1-10): "))

    if teamwork <= 3:
        score += 20
        issues.append("Poor Teamwork")

    elif teamwork <= 6:
        score += 10
        issues.append("Average Teamwork")

    # Punctuality
    punctuality = int(input("Enter Punctuality Rating (1-10): "))

    if punctuality <= 3:
        score += 15
        issues.append("Poor Punctuality")

    elif punctuality <= 6:
        score += 8
        issues.append("Average Punctuality")

    score = min(score, 100)

    return score, issues

# ----------------------------------------------------------
# RESULT
# ----------------------------------------------------------

def show_result(score, issues):

    status, desc = get_verdict(score)

    print("\n" + "=" * 60)
    print("                  FINAL REPORT")
    print("=" * 60)

    print("Performance Score :", score, "/100")

    print("\nSTATUS :", status)

    print("\nDESCRIPTION :")
    print(desc)

    print()

    if issues:

        print("ISSUES DETECTED :")

        for i, issue in enumerate(issues, 1):
            print(str(i) + ".", issue)

    else:
        print("No issues detected.")

    print("=" * 60)

# ----------------------------------------------------------
# MAIN
# ----------------------------------------------------------

while True:

    print("\n1. Evaluate Employee")
    print("2. Exit")

    ch = input("\nEnter Choice : ")

    if ch == "1":

        score, issues = employee_check()

        show_result(score, issues)

    elif ch == "2":

        print("\nExiting Program...")
        break

    else:
        print("Invalid Choice")
        