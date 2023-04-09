import openai
import os
import datetime
from pathlib import Path

# Set up OpenAI API
openai.api_key = "your_openai_api_key"

# Set up the output directory
output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

def generate_question(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
    )
    question = response.choices[0].text.strip()
    return question

def main():
    previous_questions = []
    while True:
        prompt = "Ask a random question related to human personality. Use Myers-Briggs Personality Index or any other related topic."
        if previous_questions:
            prompt += f" The last question was: {previous_questions[-1]}"

        question = generate_question(prompt)

        if question not in previous_questions:
            previous_questions.append(question)
            print(question)
            answer = input("Your answer: ")

            today = datetime.date.today().strftime("%Y-%m-%d")
            output_file = output_dir / f"{today}_questions_answers.txt"

            with open(output_file, "a") as f:
                f.write(f"Q: {question}\n")
                f.write(f"A: {answer}\n\n")

        else:
            print("Generated a duplicate question. Generating a new one...")

if __name__ == "__main__":
    main()
