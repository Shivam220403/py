from PIL import Image


def get_image_resolution(img_path):
    # Open an image file
    with Image.open(img_path) as img:
        # Get the resolution (width, height)
        width, height = img.size
    return width, height


# Example usage
image_path = "/home/shivam/Pictures/Screenshots/Screenshot from 2024-09-02 17-35-42.png"
resolution = get_image_resolution(image_path)
print(f"The resolution of the image is: {resolution[0]}x{resolution[1]} (width x height)")
