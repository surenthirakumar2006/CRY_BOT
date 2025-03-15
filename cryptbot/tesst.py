import socket
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import hashlib
import random

# Configuration
FLAG = "expX{Y0u_Ne3d_Pr0f3ss0r_L3v3l_Crypt0_Sk1ll5!}"
MAX_ATTEMPTS = 3  # Allowed attempts per challenge

# --------------------------
# Enhanced Crypto Challenges
# --------------------------
challenges = [
    {  # Challenge 1: Multi-Layered Cipher
        "question": "Decrypt: V2VsY29tZVRvZXhwbG9pdFg= ",
        "answer": "WelcomeToexploitX"#base64
    },
    {  # Challenge 3: XOR with Key Derivation
        "question": "Decrypt:4b 42 45 5a 6e 66 67 72 65 6c",
        "answer": "XORMastery"#hex,rot13 #ok 
    },
    {  # Challenge 4: Hybrid Vigenère+Base64
        "question": "4e 65 68 78 6f 6a 59 6b 69 61 78 6f 7a 65",
        "answer": "HybridSecurity"#caser 6 + hex
    },
    {  # Challenge 5: Final CTF-Style Challenge
        "question": "Decrypt:30 30 30 30 30 30 30 30 20 20 34 33 20 35 34 20 34 36 20 37 62 20 34 36 20 36 39 20 36 65 20 36 31 20 36 63 20 35 66 20 34 32 20 36 66 20 37 33 20 37 33 20 37 64",
        "answer": "CTF{Final_Boss}"  #hex+hex
    }
    
]

# --------------------------
# Server Setup
# --------------------------
def handle_client(conn):
    conn.sendall(b"\n[+] Welcome to NSA-Level Crypto Challenge!\n")
    conn.sendall(b"[+] Anti-Automation Measures Active:\n")
    conn.sendall(b" - Sequential challenge progression\n - Dynamic keys\n")
    
    # Create a copy of challenges list to work with
    all_challenges = challenges.copy()
    random.shuffle(all_challenges)  # Randomize the order of challenges
    
    solved_count = 0
    total_challenges = len(all_challenges)
    
    # Iterate through all challenges
    for i, challenge in enumerate(all_challenges):
        conn.sendall(f"\n[+] Challenge {i+1}/{total_challenges}: {challenge['question']}\n".encode())
        attempts = 0
        
        while attempts < MAX_ATTEMPTS:
            try:
                conn.sendall(b"Enter answer: ")
                response = conn.recv(1024).decode().strip()
                
                if response == challenge["answer"]:
                    conn.sendall(b"\n[+] Correct! Challenge solved!\n")
                    solved_count += 1
                    break  # Move to the next challenge
                else:
                    attempts += 1
                    if attempts >= MAX_ATTEMPTS:
                        conn.sendall(b"\n[!] Maximum attempts reached for this challenge.\n")
                        return  # End the connection if max attempts reached
                    conn.sendall(f"\n[!] Incorrect! {MAX_ATTEMPTS - attempts} attempts remaining.\n".encode())
            except Exception as e:
                print(f"Error: {e}")
                conn.sendall(b"\n[!] An error occurred. Try again later.\n")
                return
    
    # If all challenges are solved, provide the flag
    if solved_count == total_challenges:
        conn.sendall(b"\n[+] Congratulations! You solved all challenges!\n")
        conn.sendall(f"\n[+] Your Flag: {FLAG}\n".encode())
    else:
        conn.sendall(b"\n[!] You did not complete all challenges. Try again later.\n")

# --------------------------
# Main Server
# --------------------------
if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 1236
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Listening on {HOST}:{PORT}...")
    
    while True:
        try:
            conn, addr = server.accept()
            print(f"New connection from {addr}")
            handle_client(conn)
            conn.close()
        except Exception as e:
            print(f"Server error: {e}")