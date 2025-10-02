# image-resizer-tool

📌 Overview

A simple Python tool to resize and convert images in batch using the Pillow library.
It automates repetitive image tasks like scaling, format conversion, and preparing images for web or projects.

🚀 Features

🔄 Resize all images in a folder at once.
🎯 Choose custom width and height.
🖼️ Convert formats (.jpg, .png, .jpeg) easily.
⚡ Fast and automated batch processing.

📂 Input/Output folder structure for better organization.

📂 Project Structure
image-resizer-tool/
 ├── images/              # Place your original images here
 ├── output/              # Resized images will be saved here
 ├── resize_images.py     # Main script
 ├── requirements.txt     # Dependencies (Pillow)
 └── README.md            # Documentation

 🎉 Example Run
Enter new width: 300
Enter new height: 450
Convert format? (e.g., .png, .jpg, leave blank for same): .jpg
✅ Resized and saved: output/photo1_resized.jpg
✅ Resized and saved: output/logo_resized.jpg
🎉 All images have been resized successfully!

🖼️ Original image: picture.jpg  width=1000px heght=1777px
<img width="249" height="423" alt="image" src="https://github.com/user-attachments/assets/00f10b00-414a-42b7-a6f9-236dde442cd3" />

Resized image: picture_resized.jpg width=300px height=450px
<img width="286" height="415" alt="image" src="https://github.com/user-attachments/assets/3ec2811a-8f3a-4e78-9899-88fc755d8851" />

