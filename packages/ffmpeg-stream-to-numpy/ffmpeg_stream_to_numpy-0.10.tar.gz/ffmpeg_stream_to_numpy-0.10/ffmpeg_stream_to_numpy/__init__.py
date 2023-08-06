import os

import subprocess as sp
import numpy
from easy_symlink import create_symlink
from get_video_len import get_video_len_and_frames


class NumpyVideo:
    def __init__(
        self,
        videofile: str,
        ffmpeg_param: tuple = (
            "-re",
            "-hwaccel",
            "cuda",
            "-c:v",
            "h264_cuvid",
        ),
    ):
        self.videofile = videofile
        if isinstance(ffmpeg_param, tuple):
            self.ffmpeg_param = list(ffmpeg_param)
        else:
            self.ffmpeg_param = ffmpeg_param

        self.playvideo = True

    def play_video_ffmpeg(
        self,
    ):
        self.playvideo = True
        inputfile_ = self.videofile
        vid = get_video_len_and_frames(inputfile_)
        IMG_H = vid["height"]
        IMG_W = vid["width"]
        inputfile = "_______ffmpeg." + inputfile_.split(".")[-1]
        create_symlink(inputfile_, inputfile)
        ffmpeg_para = self.ffmpeg_param
        ffmpeg_add = ["ffmpeg", "-y"]
        ffmpeg_app = ["-i", inputfile, "-pix_fmt", "bgr24", "-f", "rawvideo", "-"]
        ffmpeg_cmd = ffmpeg_add + ffmpeg_para + ffmpeg_app
        pipe = sp.Popen(ffmpeg_cmd, stdout=sp.PIPE)

        while self.playvideo is True:
            try:
                raw_image = pipe.stdout.read(IMG_W * IMG_H * 3)
                image = numpy.frombuffer(raw_image, dtype="uint8")
                if image.shape[0] == 0:
                    break
                else:
                    image = image.reshape((IMG_H, IMG_W, 3))
                yield image
            except Exception as fe:
                print(fe)
                break

        pipe.stdout.close()
        pipe.wait()
        try:
            os.unlink(inputfile)
        except Exception:
            pass
