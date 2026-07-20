"""Exam Score"""

def main():
    """Find the Top score and find out how many people have it"""
    allrabbit = int(input())
    score_list = []
    for i in range(allrabbit):
        score = int(input())
        score_list.append(score)

    topscore = max(score_list)
    count_top = score_list.count(topscore)

    print(topscore)
    print(count_top)
main()
