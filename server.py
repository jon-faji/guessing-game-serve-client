import random
import socket

class GuessingGameServer:
    def __init__(self, host="10.125.6.148", port=7777, password="guessme"): # Use IP address or Hostname connection
        self.host = host
        self.port = port
        self.password = password  # Server password for authentication
        self.secret_number = random.randint(1, 100)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        # Binding the server to the IP and port
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"Server is waiting for a client to connect on {self.host}:{self.port}...")

        while True:
            # Wait for a client to connect (blocking call)
            conn, addr = self.server_socket.accept()
            print(f"Connected by {addr}")

            with conn:
                # Ask the client for the password
                conn.sendall(b"Enter the password to start the game: ")
                client_password = conn.recv(1024).decode().strip()

                # If the password is incorrect close the connection
                if client_password != self.password:
                    conn.sendall(b"Incorrect password. Connection closing...\n")
                    conn.close()
                    continue

                # If password is correct start the game
                conn.sendall(b"Access granted! Welcome to the Guessing Game.\n")
                conn.sendall(b"Guess a number between 1 and 100.\n")

                attempts = 0
                while True:
                    data = conn.recv(1024).decode().strip()
                    if not data:
                        break  # End game if no input received

                    try:
                        guess = int(data)
                        attempts += 1

                        if guess < self.secret_number:
                            response = "Too low!"
                        elif guess > self.secret_number:
                            response = "Too high!"
                        else:
                            # Provide a performance rating
                            if attempts <= 5:
                                rating = "Excellent"
                            elif 6 <= attempts <= 20:
                                rating = "Very Good"
                            else:
                                rating = "Good / Fair"

                            response = f"Correct! You win! Attempts: {attempts}. Rating: {rating}\n"

                            # Prepare for next round
                            self.secret_number = random.randint(1, 100)
                            attempts = 0

                        conn.sendall(response.encode())

                    except ValueError:
                        # Inform the client of invalid input clearly
                        conn.sendall(b"Invalid input! Please enter a number between 1 and 100.\n")

    def stop(self):
        self.server_socket.close()

def main():
    server = GuessingGameServer()
    try:
        server.start()
    except KeyboardInterrupt:
        print("\nServer shutting down...")
    finally:
        server.stop()

if __name__ == "__main__":
    main()
