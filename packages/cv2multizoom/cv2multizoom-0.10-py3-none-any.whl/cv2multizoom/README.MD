# Fast multiple zooms on a picture using cv2 and ffmpeg


```python
# Allowed image formats: url/path/buffer/base64/PIL/np
# ffmpeg must be installed 
from cv2multizoom import multizoom
multizoom(
    img=r"https://github.com/hansalemaos/screenshots/raw/main/splitted1.png",
    howmanyzooms=10,  # number of output pictures might be a little less than howmanyzooms
    outputfolder=r"F:\cv2mergepics\tt4",  # will be created if it does not exist
    zoomfactor_start=1,
    zoom_speed=2.5,
    framerate=29.97,
    zfill=7,  # 0000001.png instead of 1.png
    prefix="zoompics_",
    threads=5,
)


```


<img src="https://github.com/hansalemaos/screenshots/raw/main/zoompics_0000000.png"/>


<img src="https://github.com/hansalemaos/screenshots/raw/main/zoompics_0000001.png"/>


<img src="https://github.com/hansalemaos/screenshots/raw/main/zoompics_0000002.png"/>


<img src="https://github.com/hansalemaos/screenshots/raw/main/zoompics_0000003.png"/>


<img src="https://github.com/hansalemaos/screenshots/raw/main/zoompics_0000004.png"/>


<img src="https://github.com/hansalemaos/screenshots/raw/main/zoompics_0000005.png"/>


<img src="https://github.com/hansalemaos/screenshots/raw/main/zoompics_0000006.png"/>


<img src="https://github.com/hansalemaos/screenshots/raw/main/zoompics_0000007.png"/>


<img src="https://github.com/hansalemaos/screenshots/raw/main/zoompics_0000008.png"/>



