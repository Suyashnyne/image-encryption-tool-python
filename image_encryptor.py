from PIL import Image


def encrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Simple encryption using key
            pixels[x, y] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    encrypted_image = "encrypted_image.png"
    img.save(encrypted_image)

    print(f"Encrypted image saved as {encrypted_image}")


def decrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Reverse encryption
            pixels[x, y] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    decrypted_image = "decrypted_image.png"
    img.save(decrypted_image)

    print(f"Decrypted image saved as {decrypted_image}")


# User choice
print("1. Encrypt Image")
print("2. Decrypt Image")

choice = input("Enter your choice: ")

image_path = input("Enter image path: ")
key = int(input("Enter encryption key: "))

if choice == "1":
    encrypt_image(image_path, key)

elif choice == "2":
    decrypt_image(image_path, key)

else:
    print("Invalid choice!")
