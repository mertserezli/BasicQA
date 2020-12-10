import csv
from collections import namedtuple


def main():
    file_name = input("Enter the q/a file name\n")
    print("When a question is asked press enter if you know the answer, if not press n and enter")
    read_qa = csv.reader(open(file_name), delimiter="\t")
    QA = namedtuple('QA', "question answer")
    qa_pairs = []
    for row in read_qa:
        qa_pairs.append(QA(*row))

    while len(qa_pairs):
        if ask(qa_pairs[0]):
            qa_pairs.pop(0)
        else:
            qa_pairs.append(qa_pairs.pop(0))


def ask(qa):
    print(qa.question)
    input("Show?")
    print(qa.answer)
    user_answer = input("Answer?\n")
    if user_answer.lower().startswith('n'):
        return False
    return True


if __name__ == '__main__':
    main()
