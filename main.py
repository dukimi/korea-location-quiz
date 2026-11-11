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

    def run(self):
        while True:
            self.show_menu()

            choice = input("메뉴를 선택하세요: ")

            if choice == "1":
                print("퀴즈 풀기")
            elif choice == "2":
                print("퀴즈 추가")
            elif choice == "3":
                print("퀴즈 목록 확인")
            elif choice == "4":
                print("최고 점수 확인")
            elif choice == "5":
                print("프로그램을 종료합니다.")
                break
            else:
                print("올바른 메뉴 번호를 입력하세요.")

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

for quiz in quizzes:
    print(quiz.question)
    print(quiz.choices)

game = QuizGame(quizzes)
game.run()
