import os
import sys
from moviepy.editor import VideoFileClip
from moviepy.config import change_settings


def get_ffmpeg_binary():
	"""Returns the path to FFmpeg executable based on environment"""
	# Check if running as exe (via PyInstaller)
	if getattr(sys, 'frozen', False):
		# If exe, path will be relative to execution directory
		base_path = os.path.dirname(sys.executable)
		ffmpeg_path = os.path.join(base_path, "ffmpeg", "ffmpeg.exe")
	else:
		# Check if ffmpeg exists in project directory
		script_dir = os.path.dirname(os.path.abspath(__file__))
		ffmpeg_path = os.path.join(script_dir, "ffmpeg-minimal", "ffmpeg-7.1.1-essentials_build", "bin", "ffmpeg.exe")
		
		if not os.path.exists(ffmpeg_path):
			# If not found, use moviepy default
			return None
	
	return ffmpeg_path if os.path.exists(ffmpeg_path) else None


def ensure_directories_exist(input_dir, output_dir):
	"""Creates input and output directories if they don't exist"""
	if not os.path.exists(input_dir):
		os.makedirs(input_dir)
		print(f"Created input directory: {input_dir}")
		# Add basic README message to input directory
		readme_path = os.path.join(input_dir, "README.txt")
		with open(readme_path, "w", encoding="utf-8") as f:
			f.write("Place video files for conversion in this folder.")
	
	if not os.path.exists(output_dir):
		os.makedirs(output_dir)
		print(f"Created output directory: {output_dir}")


def extract_audio(input_dir, output_dir):
	# Ensure output directory exists
	if not os.path.exists(output_dir):
		os.makedirs(output_dir)

	# Check if there are files in input directory
	files = [f for f in os.listdir(input_dir) if f.lower().endswith((".mp4", ".avi", ".mov", ".mkv"))]
	if not files:
		print("No video files found in the input directory.")
		print(f"Please add video files to: {input_dir}")
		return

	# Process each file in input directory
	for filename in files:
		input_path = os.path.join(input_dir, filename)
		output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + ".mp3")

		# Extract audio and save as MP3
		video = VideoFileClip(input_path)
		audio = video.audio
		audio.write_audiofile(output_path)

		# Close files to release resources
		audio.close()
		video.close()

		print(f"Extracted audio from {filename}")


def main():
	# Set local FFmpeg if it exists
	ffmpeg_binary = get_ffmpeg_binary()
	if ffmpeg_binary:
		print(f"Using local FFmpeg: {ffmpeg_binary}")
		change_settings({"FFMPEG_BINARY": ffmpeg_binary})
	
	# Get execution directory path - use sys.executable for EXE mode
	if getattr(sys, 'frozen', False):
		base_dir = os.path.dirname(sys.executable)
	else:
		base_dir = os.path.dirname(os.path.abspath(__file__))
	
	# Define paths relative to execution location
	input_directory = os.path.join(base_dir, "input-videos")
	output_directory = os.path.join(base_dir, "output-audios")

	# Ensure directories exist
	ensure_directories_exist(input_directory, output_directory)

	# Run the function
	extract_audio(input_directory, output_directory)

	# Add completion message and wait for close (for EXE file)
	if getattr(sys, 'frozen', False):
		print("\nConversion complete! Press Enter to close this window.")
		input()


if __name__ == "__main__":
	main()
