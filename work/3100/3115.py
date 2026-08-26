"""Arcade of Time: Store Check"""
import sys

def main():
    """Arcade of Time: Store Check"""
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    num = int(input_data[0])
    check = int(input_data[1])
    timeline = [0] * 1442
    idx = 2
    for _ in range(num):
        start = int(input_data[idx])
        stop = int(input_data[idx+1])
        idx += 2
        timeline[start] += 1
        timeline[stop] -= 1
    for i in range(1, 1441):
        timeline[i] += timeline[i-1]
    answers = []
    for _ in range(check):
        query_time = int(input_data[idx])
        idx += 1
        answers.append(str(timeline[query_time]))
    print(" ".join(answers))
main()
