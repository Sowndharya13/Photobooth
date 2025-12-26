from PIL import Image
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

def create_collage():
    photos = []

    # Load photos
    for i in range(1, 5):
        path = os.path.join(OUTPUT_DIR, f"photo{i}.jpg")
        photos.append(Image.open(path).convert("RGB"))

    # Use width of first photo
    width = photos[0].width

    # Resize all photos to same width
    resized_photos = []
    total_height = 0

    for img in photos:
        ratio = width / img.width
        new_height = int(img.height * ratio)
        img = img.resize((width, new_height))
        resized_photos.append(img)
        total_height += new_height

    # Create blank canvas
    collage = Image.new("RGB", (width, total_height), color="white")

    # Paste photos
    y_offset = 0
    for img in resized_photos:
        collage.paste(img, (0, y_offset))
        y_offset += img.height

    # Save
    final_path = os.path.join(OUTPUT_DIR, "final_collage.jpg")
    collage.save(final_path, quality=95)

    return final_path
