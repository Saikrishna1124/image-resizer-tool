import os
from PIL import Image

def resize_images(input_folder="images", output_folder="output", size=(400, 400), format=None):
    # Create output folder if not exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)

        # Only process image files
        if file_name.lower().endswith((".png", ".jpg", ".jpeg")):
            img = Image.open(file_path)

            # Resize image
            resized_img = img.resize(size)

            # Prepare output filename
            name, ext = os.path.splitext(file_name)
            new_ext = format if format else ext
            output_path = os.path.join(output_folder, f"{name}_resized{new_ext}")

            # Save resized image
            resized_img.save(output_path)
            print(f"✅ Resized and saved: {output_path}")

    print("🎉 All images have been resized successfully!")

if __name__ == "__main__":
    # User input
    width = int(input("Enter new width: "))
    height = int(input("Enter new height: "))
    fmt_choice = input("Convert format? (e.g., .png, .jpg, leave blank for same): ").strip()

    resize_images(size=(width, height), format=fmt_choice if fmt_choice else None)
