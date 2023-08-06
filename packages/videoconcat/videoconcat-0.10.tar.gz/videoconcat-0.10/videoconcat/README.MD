<h2>Concatenates videos</h2>


```python

# needs ffmpeg 

vi = [
    r"C:\Users\Gamer\Videos\tesseract.mp4",
    r"C:\Users\Gamer\Videos\dfbs4.mp4",
    r"C:\Users\Gamer\Videos\yolov5.mp4",
]

concatenate_video(
    video_clip_paths=vi,
    output_path=r"f:\newvi\newvidxx1.mp4",  # if folder doesn't exist, it will be created
    newsize_w=720,
    newsize_h=1080,
    method="reduce",  # resizes all videos
)

concatenate_video(
    video_clip_paths=vi,
    output_path=r"f:\newvi\newvidxx2.mp4",  # if folder doesn't exist, it will be created
    newsize_w=720,
    newsize_h=1080,
    method="compose",  # does not resize videos (black background)
)


```



