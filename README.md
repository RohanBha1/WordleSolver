# Wordle Solver

## What's This?
This is a Wordle Solver built in Python. It helps you out by suggesting the best next guess when you play Wordle, based on the clues you've entered so far. It uses a neat list of five-letter words and some smart filtering based on your game feedback (like those green, yellow, and gray responses you get after each guess).

## Cool Features
- **Smart Filtering:** The tool filters out words that don't match your game's feedback.
- **Best Guess Suggestion:** It suggests the most strategic next guess to help you crack the word faster.
- **Interactive Gameplay:** You get to input your guesses and see suggestions in real-time through a simple command-line interface.

## Before You Start
Make sure you've got:
- Python 3.6 or newer
- NLTK library (don't worry, I'll show you how to install it below)

To install NLTK, just open up your terminal and punch in:
```bash
pip install nltk
```
## How to Set It Up
1. **Grab the Code:**
   Clone this repo or download the zip and unpack it wherever you like:
   ```bash
   git clone https://github.com/RohanBha1/WordleSolver.git
   cd WordleSolver
   ```
2. **Fire It Up:**
   Start the solver by running:
   ```bash
   python WordleSolver.py
   ```

## How to Use It
1. **Kick things off** by running the script.
2. **Type your guesses** when prompted.
3. **Enter the feedback** after each guess using 'g' for green, 'y' for yellow, and '_' for gray.
4. **Take the hints**—the solver tells you how many words are left and what to guess next.

## Get Involved
Got ideas or improvements? Feel free to fork this repo, tweak it, and send a pull request my way.

## License
This project is open-sourced under the MIT License. Check out the LICENSE file for more details.

