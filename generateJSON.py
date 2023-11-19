import re
import json

def parse_questions(file_content):
    alphabet_answers = ["A", "B", "C", "D"]

    # Regular expression pattern to match each question block
    pattern = re.compile(r"Câu (\d+):(.*?)Đáp án: (\w)", re.DOTALL | re.UNICODE)

    matches = pattern.findall(file_content)

    questions = []
    for match in matches:
        question_number = match[0].strip()
        question_content = match[1].strip()
        correct_answer = match[2].strip()

        # Extracting answer choices
        answer_pattern = re.compile(r"([A-D])\. (.+)", re.UNICODE)
        answer_matches = answer_pattern.findall(question_content)

        # answers = [{"choice": ans[0], "content": ans[1].strip()} for ans in answer_matches]
        answers = question_content.split("\n")

        four_answers = []
        for x in range(4):
            four_answers.append(answers.pop())
            
        question_content = '\n'.join(answers)

        right_index = alphabet_answers.index(correct_answer)
        correct_full_answer = four_answers[right_index]
        four_answers.remove(correct_full_answer)

        # Constructing the question dictionary
        question_dict = {
            "question_number": question_number,
            "question_content": question_content,
            "answers": answers,
            "correct_answer": correct_answer,
            "right_index": right_index,
            "H": "Câu " + question_number + ": " + question_content,
            "Đ": correct_full_answer,
            "T1": four_answers[0],
            "T2": four_answers[1],
            "T3": four_answers[2],
        }

        questions.append(question_dict)

    return questions

def main():
    file_path = "output.txt"
    
    with open(file_path, "r", encoding="utf-8") as file:
        file_content = file.read()

    questions = parse_questions(file_content)

    # Convert to JSON and print or save to a file
    json_output = json.dumps(questions, ensure_ascii=False, indent=2)
    
    # Print to console
    print(json_output)

    # Write to a file
    with open("output.json", "w", encoding="utf-8") as json_file:
        json_file.write(json_output)

if __name__ == "__main__":
    main()
