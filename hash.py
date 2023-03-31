import pytube
import tqdm
import os
import time
from pytube import Stream
from pytube import YouTube
from tqdm import tqdm
import os

video_urls = []

with open("urls.txt", "r") as f:
    x = f.read()
    urls = x.split("\n")
    print(urls)
video_urls = urls

def progress_callback(stream: Stream, data_chunk: bytes, bytes_remaining: int) -> None:
    pbar.update(len(data_chunk))

for ur in video_urls:
    os.system("cls")
    print("Starting New Download")
    url = ur
    yt = YouTube(url, on_progress_callback=progress_callback, proxies={})
    stream = yt.streams.get_highest_resolution()
    print(f"Downloading video to '{stream.default_filename}'")
    pbar = tqdm(total=stream.filesize, unit="bytes")
    path = stream.download(output_path="./download")
    pbar.close()
    print(f"Saved video to {path}")
    time.sleep(3)
    