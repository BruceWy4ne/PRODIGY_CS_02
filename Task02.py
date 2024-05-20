from PIL import Image
import numpy as np


def load_image(path):
    try:
        image = Image.open(path)
        image.show()
        return image
    except FileNotFoundError:
        print("File not found. Please ensure the file path is correct.")
        return None


def image_to_array(image):
    return np.array(image)


def array_to_image(array):
    return Image.fromarray(np.uint8(array))


def encrypt_pixel(pixel, key):
    return (pixel + key) % 256


def decrypt_pixel(pixel, key):
    return (pixel - key) % 256


def encrypt_image(image_array, key):
    vectorized_encrypt = np.vectorize(encrypt_pixel)
    encrypted_array = vectorized_encrypt(image_array, key)
    return encrypted_array


def decrypt_image(encrypted_array, key):
    vectorized_decrypt = np.vectorize(decrypt_pixel)
    decrypted_array = vectorized_decrypt(encrypted_array, key)
    return decrypted_array


def save_image(image, path):
    image.save(path)


def main():
    image_path = input("Enter image path: ")
    encryption_key = 50

    # Load the image
    image = load_image(image_path)
    if image is None:
        return

    # Convert the image to a NumPy array
    image_array = image_to_array(image)

    # Encrypt the image
    encrypted_array = encrypt_image(image_array, encryption_key)
    encrypted_image = array_to_image(encrypted_array)
    encrypted_image.show()
    save_image(encrypted_image, 'encrypted_image.png')

    # Decrypt the image
    decrypted_array = decrypt_image(encrypted_array, encryption_key)
    decrypted_image = array_to_image(decrypted_array)
    decrypted_image.show()
    save_image(decrypted_image, 'decrypted_image.png')


if __name__ == "__main__":
    main()
