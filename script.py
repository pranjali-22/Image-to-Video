from PIL import Image, ImageDraw, ImageFont
import subprocess
import os

def process_image(input_image, output_image, text="Sample Text", transformation="grayscale"):
    
    image = Image.open(input_image)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 80)  

    text_position = (image.width // 2, image.height // 2)
    draw.text(text_position, text, fill=(0, 255, 0), font=font)
    
    if transformation == "grayscale":
        image = image.convert("L")
    elif transformation == "rotate":
        image = image.rotate(90)
    elif transformation == "resize":
        image = image.resize((image.width // 2, image.height // 2))
    
    image.save(output_image)
    print(f"Image saved as {output_image}")

def create_video(image_file, output_video, music_file, duration=5):
    command = [
        "ffmpeg", "-loop", "1", "-i", image_file,
        "-i", music_file, "-c:v", "libx264", "-t", str(duration),
        "-pix_fmt", "yuv420p", "-vf", "scale=1280:720",
        output_video
    ]
    subprocess.run(command, check=True)
    print(f"Video created: {output_video}")

if __name__ == "__main__":
    input_image = "input.jpg"  
    output_image = "output.jpg"
    output_video = "output.mp4"
    music_file = "background.mp3"  

    process_image(input_image, output_image, text="Image to Video", transformation="rotate")
    create_video(output_image, output_video, music_file)
