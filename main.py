
import json
import random


class Quiz:
    def __init__(self, question, choices, answer, hint=""):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint


class QuizGame:
    def __init__(self, quizzes, score_history):
        self.quizzes = quizzes
        self.score_history = score_history
        self.high_score = 0

    def show_menu(self):
        print("\n====================================")
        print("       한국 지명 맞추기 퀴즈")
        print("====================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록 확인")
        print("4. 최고 점수 확인")
        print("5. 퀴즈 삭제")
        print("6. 프로그램 종료")
        print("7. 점수 기록 확인")

    # 퀴즈 플레이
    def run(self):
        while True:
            self.show_menu()

            try:
                choice = int(input("숫자를 입력하세요: "))
            except ValueError:
                print("숫자만 입력해주세요.")
                continue

            if choice == 1:
                print("퀴즈 풀기")
                score = self.play_quiz()

                if score > self.high_score:
                    self.high_score = score
                    print("새로운 최고 점수를 달성했습니다!")

                # 게임을 할 때마다 점수 기록 저장
                self.save_data()

            elif choice == 2:
                print("퀴즈 추가")
                self.add_quiz()

            elif choice == 3:
                print("퀴즈 목록 확인")
                self.show_quizzes()

            elif choice == 4:
                print("최고 점수 확인")
                self.show_high_score()

            elif choice == 5:
                print("퀴즈 삭제")
                self.delete_quiz()

            elif choice == 6:
                print("프로그램을 종료합니다.")
                break

            elif choice == 7:
                print("점수 기록 확인")
                self.show_score_history()

            else:
                print("올바른 메뉴 번호를 입력하세요.")

    # 퀴즈 플레이
    def play_quiz(self):
        score = 0

        while True:
            try:
                count = int(input("몇 문제를 풀겠습니까? "))
            except ValueError:
                print("숫자만 입력해주세요.")
                continue

            if 1 <= count <= len(self.quizzes):
                break

            print(f"1에서 {len(self.quizzes)} 사이의 숫자를 입력해주세요.")

        selected_quizzes = random.sample(self.quizzes, count)

        for quiz in selected_quizzes:
            print("\n" + quiz.question)

            for i, choice in enumerate(quiz.choices, start=1):
                print(f"{i}. {choice}")

            while True:
                answer = input("정답 번호를 입력하세요: ")

                if answer == "h":
                    print(f"힌트: {quiz.hint}")
                    continue

                if answer.isdigit():
                    answer = int(answer)

                    if 1 <= answer <= 4:
                        break

                print("1부터 4 사이의 숫자를 입력해주세요.")

            if answer == quiz.answer:
                print("정답입니다!")
                score += 1
            else:
                print("오답입니다.")

        # 점수 기록 추가
        self.score_history.append({
            "score": score,
            "total": count
        })

        print(f"최종 점수: {score} / {count}")

        return score

    # 퀴즈 추가
    def add_quiz(self):
        question = input("문제를 입력하세요: ").strip()

        if not question:
            print("문제 내용을 입력해주세요.")
            return

        choices = []

        for i in range(4):
            choice = input(f"{i + 1}번 선택지: ")
            choices.append(choice)

        answer = int(input("정답 번호(1~4): "))

        quiz = Quiz(question, choices, answer)

        self.quizzes.append(quiz)
        self.save_data()

        print("퀴즈가 추가되었습니다.")

    # 등록된 퀴즈 출력
    def show_quizzes(self):
        print("\n===== 등록된 퀴즈 목록 =====")

        for i, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[{i}] {quiz.question}")

            for number, choice in enumerate(quiz.choices, start=1):
                print(f"{number}. {choice}")

    # 최고 점수
    def show_high_score(self):
        print("\n===== 최고 점수 =====")
        print(f"최고 점수: {self.high_score}")

    # 점수 기록 확인
    def show_score_history(self):
        print("\n===== 점수 기록 =====")

        if not self.score_history:
            print("아직 플레이 기록이 없습니다.")
            return

        for i, record in enumerate(self.score_history, start=1):
            print(
                f"{i}회차: "
                f"{record['score']} / {record['total']}"
            )

    # 저장하기 함수
    def save_data(self):
        data = {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                    "hint": quiz.hint
                }
                for quiz in self.quizzes
            ],
            "high_score": self.high_score,
            "score_history": self.score_history
        }

        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    # 불러오기 함수
    def load_data(self):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)

            self.quizzes = [
                Quiz(
                    item["question"],
                    item["choices"],
                    item["answer"],
                    item.get("hint", "")
                )
                for item in data["quizzes"]
            ]

            self.high_score = data.get("high_score", 0)
            self.score_history = data.get("score_history", [])

        except FileNotFoundError:
            print("저장된 데이터가 없습니다. 기본 데이터를 사용합니다.")
            self.score_history = []

        except json.JSONDecodeError:
            print("저장 파일이 손상되었습니다. 기본 데이터를 사용합니다.")
            self.score_history = []

    # 퀴즈 삭제
    def delete_quiz(self):
        self.show_quizzes()

        try:
            number = int(input("삭제할 퀴즈 번호를 입력하세요: "))
        except ValueError:
            print("숫자를 입력해주세요.")
            return

        if 1 <= number <= len(self.quizzes):
            self.quizzes.pop(number - 1)
            self.save_data()
            print("퀴즈가 삭제되었습니다.")
        else:
            print("올바른 번호를 입력해주세요.")


# 기본 퀴즈 데이터
quizzes = [
    Quiz(
        "대한민국의 수도는?",
        ["서울특별시", "부산광역시", "대구광역시", "광주광역시"],
        1,
        "한강이 흐르는 도시에요."
    ),
    Quiz(
        "대한민국에서 가장 넓은 시는?",
        ["대전광역시", "인천광역시", "부산광역시", "울산광역시"],
        2,
        "수도권에 위치한 광역시예요."
    ),
    Quiz(
        "제주특별자치도의 중심 도시는?",
        ["서귀포시", "제주시", "목포시", "창원시"],
        2,
        "이름 그대로에요."
    ),
    Quiz(
        "대한민국의 동쪽에 위치한 대표적인 광역시는?",
        ["인천광역시", "부산광역시", "울산광역시", "대전광역시"],
        3,
        "경상남도와 부산광역시 사이에 있어요."
    ),
    Quiz(
        "경상남도의 도청 소재지는?",
        ["거제시", "안동시", "여수시", "창원시"],
        4,
        "경상남도에서 가장 큰 도시에요."
    )
]


if __name__ == "__main__":
    try:
        game = QuizGame(quizzes, [])
        game.load_data()
        game.run()

    except (EOFError, KeyboardInterrupt):
        print("\n프로그램을 종료합니다.")
