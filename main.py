import json

class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

class QuizGame:
    def __init__(self, quizzes):
        self.quizzes = quizzes
        self.high_score = 0

    def show_menu(self):
        print("\n====================================")
        print("       한국 지명 맞추기 퀴즈")
        print("====================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록 확인")
        print("4. 최고 점수 확인")
        print("5. 프로그램 종료")

    # 퀴즈 플레이
    def run(self):
        while True:
            self.show_menu()
            self.load_data()

            choice = input("메뉴를 선택하세요: ")

            if choice == "1":
                print("퀴즈 풀기")
                score = self.play_quiz()
                if score > self.high_score:
                    self.high_score = score
                    self.save_data()
                    print("새로운 최고 점수를 달성했습니다!")
            elif choice == "2":
                print("퀴즈 추가")
                self.add_quiz()
            elif choice == "3":
                print("퀴즈 목록 확인")
                self.show_quizzes()
            elif choice == "4":
                print("최고 점수 확인")
                self.show_high_score()
            elif choice == "5":
                print("프로그램을 종료합니다.")
                break
            else:
                print("올바른 메뉴 번호를 입력하세요.")

    # 퀴즈 플레이
    def play_quiz(self):
        score = 0

        for quiz in self.quizzes:
            print("\n" + quiz.question)

            for i, choice in enumerate(quiz.choices, start=1):
                print(f"{i}. {choice}")

            answer = input("정답을 입력하세요: ")

            if answer == str(quiz.answer):
                print("정답입니다!")
                score += 1
            else:
                print("오답입니다.")

        print(f"최종 점수: {score} / {len(self.quizzes)}")
        return score

    # 퀴즈 추가
    def add_quiz(self):
        question = input("문제를 입력하세요: ")

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

    # 저장하기 함수
    def save_data(self):
        data = {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer
                }
                for quiz in self.quizzes
            ],
            "high_score": self.high_score
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
                    item["answer"]
                )
                for item in data["quizzes"]
            ]

            self.high_score = data["high_score"]

        except FileNotFoundError:
            print("저장된 데이터가 없습니다. 기본 데이터를 사용합니다.")

        except json.JSONDecodeError:
            print("저장 파일이 손상되었습니다. 기본 데이터를 사용합니다.")

quizzes = [
    Quiz(
        "대한민국의 수도는?",
        ["서울특별시", "부산광역시", "대구광역시", "전남광주통합특별시"],
        1
    ),
    Quiz(
        "대한민국에서 가장 넓은 시는?",
        ["대전광역시", "전남광주통합특별시", "부산광역시", "울산광역시"],
        2
    ),
    Quiz(
        "제주특별자치도의 중심 도시는?",
        ["서귀포시", "제주시", "목포시", "창원시"],
        2
    ),
    Quiz(
        "대한민국의 동쪽에 위치한 대표적인 광역시는?",
        ["인천광역시", "부산광역시", "울산광역시", "대전광역시"],
        3
    ),
    Quiz(
        "경상남도의 도청 소재지는?",
        ["거제시", "안동시", "여수시", "창원시"],
        4
    )
]

game = QuizGame(quizzes)
game.run()
