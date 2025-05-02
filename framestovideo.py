from videotoframes import get_video_fps
import os
import subprocess

def combine_frames_with_audio(input_dir, output_video, frame_rate, original_video):
    """
    Combine frames into a video and add audio from the original video.

    :param input_dir: Directory containing the frames.
    :param output_video: Path to the final output video file.
    :param frame_rate: Frame rate for the output video.
    :param original_video: Path to the original video (to extract audio).
    """
    # Temporary video file (frames combined without audio)
    temp_video = "temp_video.mp4"

    # Step 1: Combine frames into a video without audio
    command_combine_frames = [
        "ffmpeg",
        "-framerate", str(frame_rate),  # Use the provided frame rate
        "-i", os.path.join(input_dir, "frame_%04d.png"),  # Input frame format
        "-c:v", "libx264",  # Use H.264 codec for compression
        "-pix_fmt", "yuv420p",  # Ensure compatibility with most players
        temp_video
    ]
    subprocess.run(command_combine_frames, check=True)
    print(f"Temporary video created: {temp_video}")

    # Step 2: Add audio from the original video to the combined video
    command_add_audio = [
        "ffmpeg",
        "-i", temp_video,  # Input video (no audio)
        "-i", original_video,  # Input original video (with audio)
        "-c:v", "copy",  # Copy the video stream (no re-encoding)
        "-c:a", "aac",  # Encode audio in AAC format
        "-map", "0:v:0",  # Use the video stream from the temp video
        "-map", "1:a:0",  # Use the audio stream from the original video
        "-shortest",  # Trim the video or audio to match the shortest stream
        output_video
    ]
    subprocess.run(command_add_audio, check=True)
    print(f"Final video with audio saved to: {output_video}")

    # Clean up temporary video
    os.remove(temp_video)
    print("Temporary video removed.")

# Example usage
original_video_file = "wav2lip_output.mp4"
frames_directory = "path/to/GFPGAN/results/restored_imgs"
output_video_file = "gfpgan_output.mp4"

# Get FPS of the original video (reuse the function from earlier)
fps = get_video_fps(original_video_file)
print(f"Combining frames at {fps} FPS and adding audio...")
combine_frames_with_audio(frames_directory, output_video_file, frame_rate=fps, original_video=original_video_file) # frame_rate=fps



