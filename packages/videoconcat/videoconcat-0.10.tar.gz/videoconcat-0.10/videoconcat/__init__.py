import moviepy.editor as mpy
import os
from touchtouch import touch


def concatenate_video(
    video_clip_paths: list,
    output_path: str,
    newsize_w: int = 1080,
    newsize_h: int = 720,
    method="reduce",
):
    if not os.path.exists(output_path):
        touch(output_path)
        os.remove(output_path)
    clips = [mpy.VideoFileClip(c) for c in video_clip_paths]
    if method == "reduce":
        clips = [c.resize(newsize=(newsize_w, newsize_h)) for c in clips]
        final_clip = mpy.concatenate_videoclips(clips)
    else:
        final_clip = mpy.concatenate_videoclips(clips, method="compose")

        if newsize_h != 0 and newsize_w != 0:
            final_clip = final_clip.resize(newsize=(newsize_w, newsize_h))

    final_clip.write_videofile(output_path)

