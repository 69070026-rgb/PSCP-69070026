"""Filter"""
import ast
def main():
    """Filter"""
    d = ast.literal_eval(input())
    score_limit = float(input())
    filt = {}
    for student_id, score in d.items():
        if score >= score_limit:
            filt[student_id] = score
    if not filt:
        print("Nope")
        return
    for student_id in sorted(filt.keys()):
        print(f"{student_id}\t{filt[student_id]:.2f}")
main()
