import hashlib
import os
import random
import subprocess
import time
import typer


def main():
    password: str = typer.prompt("Password to hash?")

    with_salt: bool = typer.confirm("Do you want the password hashed with salt?")
    if with_salt:
        # Adding the salt to password
        salt = str(random.getrandbits(256))
        password = password + salt

    # Encode the password as bytes
    password_bytes = password.encode("utf-8")

    # Use SHA-256 hash function to create a hash object
    hashed = hashlib.sha256(password_bytes).hexdigest()

    # Print the hash
    print(f"\nHash: {hashed}\n")

    # Start timer
    start = time.time()

    # Use "Search That Hash" to find the hash
    rockyou_path: str = os.path.join(os.getcwd(), "wordlists", "rockyou.txt")
    result = subprocess.run(
        f"sth -t '{hashed}' --verbose --wordlist {rockyou_path}",
        shell=True,
        stdout=subprocess.PIPE,
    )
    print(result.stdout.decode("utf-8"))

    # Display elapsed time
    end = time.time()
    print(f"Elapsed time: {round(end - start, 3)} seconds")


if __name__ == "__main__":
    typer.run(main)
