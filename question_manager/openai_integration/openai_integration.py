import os
import openai
import re
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set up OpenAI API credentials
temperature = os.getenv("TEMPERATURE", 0.7)
max_tokens = os.getenv("MAX_TOKENS", 500)
model = 'text-davinci-003'


def generate_mcq(input_text: str, number_of_questions: int):
    if not number_of_questions:
        number_of_questions = 5

    input_text = re.sub(r'\W+', ' ', input_text)
    prompt = f"""Generate {number_of_questions} multiple-choice question in the following form: 'What is the capital of France?\n A) Berlin\n B) Rome\n C) Paris (correct)\n D) Amsterdam' separated by two new line characters, "\n", from the following text: `{input_text}`"""

    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    generated_text = response["choices"][0]["text"].strip()
    question_set_pre_process = generated_text.split("\n\n")
    print("full pre process: ", question_set_pre_process)
    question_set = []
    for obj in question_set_pre_process:
        print(f"Objects of pre process: {obj}")
        try:
            lines = obj.strip().split("?")
            print("dcvghjkl: ", lines[0].split(" ", 1))
            print("ftyuioijhb: ", lines[1].split("\n"))
            question = lines[0].strip().split(" ", 1)[1] if len(lines[0].strip().split(" ", 1)) > 0 else lines[0]
            choices = [choice.strip().split(" ", 1)[1] for choice in lines[1].strip().split("\n")]

            # Find the correct answer by searching for the answer that contains "(correct)"

            print("choices: ", choices)
            correct_choice = 0
            for i, choice in enumerate(choices):
                if "(correct)" in choice:
                    choices[i] = choices[i][0:-9]
                    correct_choice = i + 1
                    break

            question_obj = {"question": question, "choices": choices, "correct_index": correct_choice}
            print(f"Appending: {question_obj}")
            question_set.append(question_obj)
        except Exception as e:
            # print(f"Error occured: {e}")
            raise e

    print("set: ", question_set)
    return question_set

    #     if len(obj) < 8:
    #         pass

    #     obj = obj.strip()
    #     question = obj.split("?")[0].split(" ", 1) + "?"
    #     generated_choices = [choice.strip().split(" ", 1) for choice in generated_text.split("?")[1].split("\n")]
    #     for choice in generated_choices:

    #     question_set.append({"question": question, "choices": generated_choices, "correct_index": correct_index})

    # generated_questions = [question[] for question in generated_text]

    # Parse the response to extract the generated question and answer choices
# generated_question = generated_text.split("?")[0] + "?"
# generated_choices = [choice[3:] for choice in generated_text.split("?")[1].split("\n")]
# generated_choices = generated_choices[1:]
# generated_choices = [choice["text"].strip() for choice in response["choices"][0]["options"]]


# Print the generated question and answer choices
# print("Generated question: ", generated_question)
# print("Generated answer choices: ", generated_choices)
