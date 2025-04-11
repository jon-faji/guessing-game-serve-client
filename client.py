import socket

class GuessingGameClient:
    def __init__(self, host="10.125.6.148", port=7777): # Use IP address or hostname connection
        self.host = host
        self.port = port

    def play(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((self.host, self.port))
                print("Connected to the server.")

                # Receive and display the server's password prompt
                server_prompt = client_socket.recv(1024).decode()
                print(server_prompt)

                # Send password input
                password = input("Enter the password: ")
                client_socket.sendall(password.encode())

                # Get authentication response
                auth_response = client_socket.recv(1024).decode()
                print(auth_response)

                # If access is not granted, break
                if "Access granted" not in auth_response:
                    print("Authentication failed. Disconnecting...")
                    return

                # Receive welcome/game instructions
                welcome_msg = client_socket.recv(1024).decode()
                print(welcome_msg)

                # Start guessing loop
                while True:
                    guess = input("Enter your guess (1-100): ").strip()
                    client_socket.sendall(guess.encode())

                    response = client_socket.recv(1024).decode()
                    print(response)

                    # Check if the game round ended
                    if "Correct! You win!" in response:
                        print("New round starting...")  # Because server resets after correct guess

        except ConnectionRefusedError:
            print("Could not connect to the server. Make sure the server is running.")
        except KeyboardInterrupt:
            print("\nDisconnected from server.")
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    client = GuessingGameClient()
    client.play()

if __name__ == "__main__":
    main()
