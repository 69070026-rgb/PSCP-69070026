"""Exam results"""

def main():
    """Pass/Fail Calculation"""
    exercise_score = int(input())
    midterm_score = int(input())
    final_score = int(input())
    if exercise_score < (10/2) or midterm_score < (40/2) or final_score < (50/2):
        print("fail")
    else:
        print("pass")
main()
