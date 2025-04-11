# Python Socket-Based Guessing Game (Client-Server App)

This is a Python-based number guessing game using TCP socket communication. The project consists of a **server** that hosts the game and a **client** that connects to play it. Players guess a randomly generated number between 1 and 100 with feedback after each attempt. Password authentication is required to play.

---

## Project Structure

- `server.py`: Runs the server that hosts the game.
- `client.py`: Connects to the server and lets the user play the guessing game.

---

## Features

-  **Password Authentication** – Only authorized clients can play.
-  **Auto Game Reset** – The server resets the secret number after every win.
-  **Real-time Feedback** – Get hints like `Too high!`, `Too low!`, or `Correct!`.
-  **Performance Rating** – Based on how many attempts it took:

  - **Excellent** (≤ 5)
  - **Very Good** (6–20)
  - **Good / Fair** (> 20)

---

## Requirements

- Python 3.x
- No external libraries needed

---

## How to Run

### 1. Start the Server
```bash

python server.py
python client.py

## Example Output

Connected to the server.
Enter the password to start the game: 
Access granted! Welcome to the Guessing Game.
Guess a number between 1 and 100.
Enter your guess (1-100): 55
Too high!
Enter your guess (1-100): 23
Correct! You win! Attempts: 2. Rating: Excellent
New round starting...
