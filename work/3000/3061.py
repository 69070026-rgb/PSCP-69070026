"""Exam results"""

def main():
    """Pass/Fail Calculation"""
    midterm_score = int(input())
    final_score = int(input())
    result = midterm_score + final_score
    if result >= 50:
        print(result)
        print("pass")
    else:
        print(result)
        print("fail")
main()
