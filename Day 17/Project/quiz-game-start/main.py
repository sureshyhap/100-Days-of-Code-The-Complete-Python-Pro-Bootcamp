import data, question_model, quiz_brain

question_bank = []

for question in data.question_data:
    text = question["question"]
    answer = question["correct_answer"]
    new_question = question_model.Question(text, answer)
    question_bank.append(new_question)

driver = quiz_brain.QuizBrain(question_bank)
driver.run_quiz()
print(f"Your final score is: {driver.num_correct} / {driver.question_num}")