# ffmpeg stream to numpy arrays 

```python

# ffmpeg must be installed! 

$pip install ffmpeg-stream-to-numpy
from ffmpeg_stream_to_numpy import NumpyVideo
import cv2 
vi = NumpyVideo(
    videofile=r"C:\Users\Gamer\Videos\dfbs4.mp4",
    ffmpeg_param=(
        "-re", # real speed
        "-hwaccel",
        "cuda",
        "-c:v",
        "h264_cuvid",
    ),
)

for ini, i in enumerate(vi.play_video_ffmpeg()):
    # do something here 
    cv2.imshow("test", i)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    if ini == 100:
        vi.playvideo = False # stops the stream
cv2.destroyAllWindows()

    
```




