# this will take the newly generated folder content and generate the reel
from text_to_audio import text_to_speech_file
import os, subprocess, json
def text_to_audio(folder):
    with open(os.path.join("user_uploads", folder, "description.txt"), "r") as f:
        text = f.read()
    print(text)
    value = text_to_speech_file(text,folder)
    print(f"Audio generated for folder {folder}: {value}")

def generate_reel():
    folders = os.listdir("user_uploads")

    with open("generated.txt", "r") as f:
        already_generated = f.readlines()
    already_generated = [folder.strip() for folder in already_generated]

    for folder in folders:
        if folder not in already_generated:
            # generate the audio file from the text
            text_to_audio(folder)
            # generate the reel
            create_reel(folder)
            with open("generated.txt", "a") as f:
                f.write(folder + "\n")
    

def create_reel(folder):
    input_txt_path = f"user_uploads/{folder}/input.txt"
    if not os.path.exists(input_txt_path):
        print(f"No input.txt found for folder {folder}, skipping reel creation.")
        return
    
    # Get audio duration
    audio_path = f"user_uploads/{folder}/output.mp3"
    if not os.path.exists(audio_path):
        print(f"No output.mp3 found for folder {folder}, skipping reel creation.")
        return
    probe_cmd = f'ffprobe -v quiet -print_format json -show_format "{audio_path}"'
    result = subprocess.run(probe_cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ffprobe failed for {audio_path}: {result.stderr}")
        return
    data = json.loads(result.stdout)
    duration = float(data['format']['duration'])
    print(f"Audio duration for {folder}: {duration} seconds")
    
    # Read and modify input.txt
    with open(input_txt_path, "r") as f:
        lines = f.readlines()
    
    num_images = sum(1 for line in lines if line.startswith("file"))
    if num_images == 0:
        print(f"No images found in input.txt for folder {folder}, skipping.")
        return
    new_duration = duration / num_images
    new_duration = round(new_duration, 2)  # Round to 2 decimal places
    print(f"New duration per image for {folder}: {new_duration} seconds")
    
    new_lines = []
    for line in lines:
        if line.startswith("file '"):
            filename = line.split("'")[1]
            image_path = f"user_uploads/{folder}/{filename}"
            if not os.path.exists(image_path):
                print(f"Image {image_path} not found, skipping this image.")
                continue
            abs_image_path = os.path.abspath(image_path)
            new_lines.append(f"file '{abs_image_path}'\n")
            new_lines.append(f"duration {new_duration}\n")
    
    if not new_lines:
        print(f"No valid images found for folder {folder}, skipping.")
        return
    
    with open(input_txt_path, "w") as f:
        f.writelines(new_lines)
    
    # Run ffmpeg command
    command = f'''ffmpeg -f concat -safe 0 -i user_uploads/{folder}/input.txt -i user_uploads/{folder}/output.mp3 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" -c:v libx264 -c:a aac -shortest -r 30 -pix_fmt yuv420p static/reels/{folder}.mp4'''
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"FFmpeg failed for folder {folder}: {e}")
        print(f"Command: {command}")
        print(f"Stderr: {e.stderr}")
        return

    


# if __name__ == "__main__":
    