import os
import subprocess
import re

def get_video_fps(video_path):
    """
    Get the frames per second (FPS) of a video using ffprobe.

    :param video_path: Path to the video file.
    :return: FPS (frames per second) as a float.
    """
    # Command to get video information using ffprobe
    command = [
        "ffprobe",
        "-v", "error",  # Suppress unnecessary output
        "-select_streams", "v:0",  # Select the first video stream
        "-show_entries", "stream=r_frame_rate",  # Show frame rate info
        "-of", "default=noprint_wrappers=1:nokey=1",  # Output format
        video_path
    ]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    # The output is a ratio like "30000/1001", convert it to float
    fps_ratio = result.stdout.strip()
    fps = eval(fps_ratio)  # Convert to float (e.g., "30000/1001" -> 29.97)
    return float(fps)

def extract_frames(video_path, output_dir, frame_rate=60):
    """
    Extract frames from a video file at the specified frame rate.

    :param video_path: Path to the input video.
    :param output_dir: Directory to save the extracted frames.
    :param frame_rate: Frame extraction rate (frames per second).
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Command to extract frames using ffmpeg
    command = [
        "ffmpeg",
        "-i", video_path,  # Input video
        "-vf", f"fps={frame_rate}",  # Extract frames at specified rate
        os.path.join(output_dir, "frame_%04d.png")  # Output frame format
    ]

    subprocess.run(command, check=True)
    print(f"Frames extracted to {output_dir} at {frame_rate} FPS.")

# Example usage
video_file = "wav2lip_output.mp4"
frames_directory = "path/to/GFPGAN/inputs/whole_imgs"

# Get the video's FPS and extract frames at that rate
fps = get_video_fps(video_file)
print(f"Video FPS: {fps}")
extract_frames(video_file, frames_directory, frame_rate=fps) #frame_rate=fps

