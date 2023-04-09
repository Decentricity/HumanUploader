import openai
import os
import datetime
from pathlib import Path

# Atur API OpenAI
openai.api_key = "your_openai_api_key"

# Atur direktori keluaran
output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

# Fungsi untuk menghasilkan pertanyaan dengan menggunakan OpenAI API
def generate_question(prompt):
    # Membuat permintaan ke API OpenAI
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
    )
    # Mendapatkan teks pertanyaan yang dihasilkan
    question = response.choices[0].text.strip()
    return question

# Fungsi utama
def main():
    # Daftar untuk menyimpan pertanyaan sebelumnya
    previous_questions = []

    while True:
        # Membuat teks permintaan untuk pertanyaan acak terkait kepribadian
        prompt = "Buat pertanyaan acak terkait kepribadian manusia. Gunakan indeks kepribadian Myers-Briggs atau topik terkait lainnya."
        if previous_questions:
            prompt += f" Pertanyaan terakhir adalah: {previous_questions[-1]}"

        # Menghasilkan pertanyaan
        question = generate_question(prompt)

        # Memeriksa apakah pertanyaan belum pernah diajukan
        if question not in previous_questions:
            previous_questions.append(question)
            print(question)
            answer = input("Jawaban Anda: ")

            # Menyimpan pertanyaan dan jawaban dalam file teks berdasarkan tanggal saat ini
            today = datetime.date.today().strftime("%Y-%m-%d")
            output_file = output_dir / f"{today}_pertanyaan_jawaban.txt"

            with open(output_file, "a") as f:
                f.write(f"P: {question}\n")
                f.write(f"J: {answer}\n\n")

        else:
            # Jika pertanyaan adalah duplikat, buat pertanyaan baru
            print("Membuat pertanyaan duplikat. Menghasilkan yang baru...")

# Jalankan fungsi utama
if __name__ == "__main__":
    main()
