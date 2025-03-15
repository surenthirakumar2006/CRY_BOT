expX{Y0u_Ne3d_Pr0f3ss0r_L3v3l_Crypt0_Sk1ll5!

# NSA-Level Crypto Challenge Server

## Description
This project is a cryptographic challenge server that presents users with a series of progressively harder encryption-based challenges. The user must correctly solve each challenge to receive the final flag.

## Features
- Multi-layered cryptography challenges (Base64, ROT13, Reverse, AES-256-CBC, XOR, Vigenère, Base85)
- Dynamic encryption challenges with randomized keys
- Anti-automation security measures
- Socket-based interactive challenge system

## Requirements
- Python 3.x
- Required dependencies:
  ```bash
  pip install pycryptodome
  ```

## Usage
### Running the Server
1. Start the server by running:
   ```bash
   python server.py
   ```
2. The server will listen on port `1337`. Players can connect using netcat:
   ```bash
   nc <server_ip> 1337
   ```

## Challenges Overview
    *challenges = [
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
## Deployment with Docker
### Build and Run the Container
```bash
# Build the Docker image
docker build -t crypto_challenge .

# Run the container
docker run -p 1337:1337 -d crypto_challenge
```

### Stopping and Removing the Container
```bash
docker ps # Find the container ID
docker stop <container_id>
docker rm <container_id>
```

## Example Connection
After running the server, connect using:
```bash
nc 192.168.29.64 1337
```
Then, follow the on-screen prompts to solve each challenge.

## Notes
- Ensure the firewall allows traffic on port `1337`.
- Adjust `HOST` and `PORT` in the script if needed for different environments.
- The flag is revealed only after successfully solving all challenges.

---
Enjoy hacking and decrypting!

