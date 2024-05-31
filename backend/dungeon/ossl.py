import subprocess

def command(_type, op, secret_file_name, password):
    return [
        "openssl",
        "enc",
        _type, #encode/decode?
        "-aes-256-cbc", #aes256 enc/dec protocol
        "-salt", #add salt (avoid rainbow table attack)
        "-pbkdf2",
        "-md",
        "sha512", #key derivation function hashed with message digsest sha512
        "-a", #encode in base64
        op,
        secret_file_name,
        "-pass",
        "pass:" + password
    ]

def aes_encrypt(password, plaintext, secret_file_name):
    # Convert plaintext to bytes
    plaintext_bytes = plaintext.encode()
    encryption_command = command("-e", "-out", secret_file_name, password)
    try:
        encryption_process = subprocess.Popen(encryption_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        encrypted_output, _ = encryption_process.communicate(input=plaintext_bytes)
        encryption_process.wait()
        # Check if the encryption process completed successfully
        if encryption_process.returncode == 0:
            # Print the encrypted output
            print("Encryption successful")
        else:
            print("Encryption failed. Return code:", encryption_process.returncode)
            output, error = encryption_process.communicate()
            print("Output:", output)
            print("Error:", error)
    except Exception as e:
        print("Error:", e)
    finally:
        encryption_process.terminate()

def aes_decrypt(password, encrypted_file):
    decryption_command = command("-d", "-in", encrypted_file, password)
    try:
        decryption_process = subprocess.Popen(decryption_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        decrypted_output, _ = decryption_process.communicate()
        # Check if the decryption process completed successfully
        if decryption_process.returncode == 0:
            # Print the decrypted output
            print("Decryption successful. Decrypted data:")
            print(decrypted_output.decode())
        else:
            print("Decryption failed. Return code:", decryption_process.returncode)
            output, error = decryption_process.communicate()
            print("Output:", output)
            print("Error:", error)
    except Exception as e:
        print("Error:", e)
    finally:
        decryption_process.terminate()