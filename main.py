import argparse
import subprocess

def convert_video_to_audio(video_file, audio_file):
    command = f'ffmpeg -i "{video_file}" -vn -acodec copy "{audio_file}"'
    subprocess.run(command, shell=True, check=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert a video file to an audio file.')
    parser.add_argument('video_file', type=str, help='Path to the video file. Common file types include .mp4, .mkv, .avi')
    parser.add_argument('audio_file', type=str, help='Path for the output audio file. Common file types include .mp3, .aac, .wav')
    args = parser.parse_args()

    convert_video_to_audio(args.video_file, args.audio_file)

