from jussuit_tts.naver_tts import jussuit_naver_tts as tts
from time import sleep

ANSWER_TIME = 5


def print_and_tts(ment: str, prefix=""):
    print(f"{prefix}{ment}")
    tts(ment)


def ice_breaking():
    opening_ment = """
---------------------------------------    
|   안녕하세요.                           |
|   지금부터 지옥의 AI 면접을 시작하겠습니다.    |
|   파이팅하시고, 모드를 선택해주세요.          |
---------------------------------------
        """
    print_and_tts(opening_ment)


def close_interview():
    closing_ment = """
        인터뷰를 종료합니다. 수고 많으셨습니다. 
        """
    print_and_tts(closing_ment)


def question_total():
    """ 전 범위 random question 구현 예정 """
    print_and_tts("미지원 모드입니다. 다음 업데이트를 기다려주세요.")


def question_the_os():
    with open("questions/question_os.txt", mode="r", encoding="utf8") as f:
        os_questions = [line.strip() for line in f]

    for q in os_questions:
        print_and_tts(q, prefix="OS 문제 ")
        sleep(ANSWER_TIME)


if __name__ == "__main__":
    ice_breaking()

    while (mode := input(
            "인터뷰 Mode를 선택하세요: 1. Total  2. OS  3. Network  4. Data Structuce  5. Algorithm  6. Python  0. 종료 : ")) != "0":
        {"1": question_total, "2": question_the_os}[mode]()

    close_interview()
