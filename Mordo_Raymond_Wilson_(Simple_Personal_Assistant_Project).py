
"""
Simple Personal Assistant - Input/Output Project
Prompts the user for personal information, summarizes it, and optionally saves it.
"""

import random


def get_user_data():

    required_questions = [
        ("name", "What is your name? "),
        ("age", "How old are you? ")
    ]

    optional_questions = [
        ("color", "What is your favorite color? "),
        ("food", "What is your favorite food? "),
        ("city", "Which city do you live in? "),
        ("school", "Which SHS did you attend? "),
        ("team", "What is your favorite soccer team? ")
    ]

    selected_optional = random.sample(
        optional_questions, k=random.randint(2, 4))

    all_questions = required_questions + selected_optional
    responses = {}

    for key, prompt in all_questions:
        responses[key] = input(prompt)

    return responses


def display_summary(responses):
    print("\n--- Personalized Summary ---")
    print(f"Hello, {responses.get('name', 'Friend')}!")

    if 'age' in responses:
        print(f"You are {responses['age']} years old,", end=' ')
    if 'color' in responses:
        print(f"love the color {responses['color']},", end=' ')
    if 'food' in responses:
        print(f"and enjoy eating {responses['food']}.")
    else:
        print()
    if 'city' in responses:
        print(f"Life must be awesome in {responses['city']}!")
    if 'school' in responses:
        print(f"You went to {responses['school']} SHS.")
    if 'team' in responses:
        print(f"Go {responses['team']}!")


def save_to_file(responses, rating):
    filename = f"{responses.get('name', 'user')}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("User Summary\n")
        f.write("============\n")
        for key, value in responses.items():
            f.write(f"{key.capitalize()}: {value}\n")
        f.write(f"Rating: {rating}/5\n")
    print(f"Summary saved to {filename}")


def main():
    while True:
        responses = get_user_data()
        display_summary(responses)

        save = input(
            "\nDo you want to save this summary? (yes/no): ").strip().lower()
        if save == "yes":
            while True:
                try:
                    rating = int(
                        input("Please rate this assistant (1 to 5): "))
                    if 1 <= rating <= 5:
                        break
                    else:
                        print("Rating must be between 1 and 5.")
                except ValueError:
                    print("Please enter a number.")
            save_to_file(responses, rating)

        again = input(
            "\nDo you want to restart the process? (yes/no): ").strip().lower()
        if again != "yes":
            print("Goodbye! 😊")
            break


if __name__ == "__main__":
    main()
