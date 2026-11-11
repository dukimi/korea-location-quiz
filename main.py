class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

quiz1 = Quiz("대한민국의 수도는?",["서울특별시","부산광역시"],1)
print(quiz1.question)
print(quiz1.choices)
print(quiz1.answer)