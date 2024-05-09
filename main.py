import nltk
from nltk.corpus import words

nltk.download('words')
word_list = words.words()
five_letter_words = [word for word in word_list if len(word) == 5]

num_guesses = 0
guess = ""
feedback = ""
remaining_words = five_letter_words


def filter_words(words, guess, feedback):
    new_word_list = words
    for i in range(5):
        if feedback[i] in ["g", "G"]:  # Handle green feedback
            new_word_list = [word for word in new_word_list if word[i] == guess[i]]
        elif feedback[i] in ["y", "Y"]:  # Handle yellow feedback
            new_word_list = [word for word in new_word_list if guess[i] in word and word[i] != guess[i]]
        elif feedback[i] == "_":  # Handle gray feedback
            allowed_indices = [j for j, f in enumerate(feedback) if f in ["g", "G", "y", "Y"] and guess[j] == guess[i]]
            if not allowed_indices:  # If no allowed positions, the letter must not appear at all
                new_word_list = [word for word in new_word_list if guess[i] not in word]
            else:  # Letter can appear, but only in specific positions
                new_word_list = [word for word in new_word_list if all(word[j] != guess[i] for j in range(5) if j not in allowed_indices)]

    return new_word_list


def best_guess(words):
    best_word = None
    least_remaining = float('inf')

    for guess in words:
        outcomes = {}
        for target in words:
            feedback = []
            for i in range(5):
                if guess[i] == target[i]:
                    feedback.append('g')
                elif guess[i] in target:
                    feedback.append('y')
                else:
                    feedback.append('_')
            feedback = ''.join(feedback)
            outcomes.setdefault(feedback, []).append(target)

        avg_remaining = sum(len(outcomes[fb]) for fb in outcomes) / len(outcomes)
        if avg_remaining < least_remaining:
            best_word = guess
            least_remaining = avg_remaining

    return best_word, least_remaining


while num_guesses < 6:
    print(f"Remaining words count: {len(remaining_words)}")
    guess = input("What is your guess?").strip().lower()
    if guess == "done":
        print(remaining_words)
        best_word, avg_remaining = best_guess(remaining_words)
        print(f"Best guess: {best_word} which on average leaves {avg_remaining:.2f} possible words.")
        break
    feedback = input("What was your feedback for this guess?").strip().lower()
    remaining_words = filter_words(remaining_words, guess, feedback)
    num_guesses+=1
    if not remaining_words:
        print("No words exist like the one you're describing try again")
        break



