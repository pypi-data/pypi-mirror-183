import os
import tempfile
from functools import partial
from a_cv_imwrite_imread_plus import open_image_in_cv
import cv2
from easy_symlink import create_symlink
import regex


def get_tmpfile(suffix=".txt"):
    tfp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    filename = tfp.name
    filename = os.path.normpath(filename)
    tfp.close()
    return filename, partial(os.remove, tfp.name)


def multizoom(
    img,
    howmanyzooms: int,
    outputfolder: str,
    zoomfactor_start: float = 8.0,
    zoom_speed: float = 2.5,
    framerate: float = 29.97,
    zfill: int = 8,
    prefix: str = "out",
    threads: int = 5,
) -> list:

    howmanyseconds = howmanyzooms / framerate
    howmanyseconds = round(howmanyseconds, 2)
    pathimagefolder = outputfolder
    if not os.path.exists(pathimagefolder):
        os.makedirs(pathimagefolder)
    tempicture, tempicture_delete = get_tmpfile(suffix=".png")
    img = open_image_in_cv(img)
    cv2.imwrite(tempicture, img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
    y_size = img.shape[0]
    x_size = img.shape[1]
    simpic = "xxxxxxxxxxxxxxxxxxxxxxxxxbab.png"
    create_symlink(tempicture, simpic)
    simfold = "xxxxxxxxxxxxxxxxxxxxxxxxxbabxz"
    create_symlink(pathimagefolder, simfold)

    os.system(
        f"""ffmpeg -threads {threads} -y -loop 1 -i {simpic} -vf "scale=w=({x_size}*{zoomfactor_start}):h=({y_size}*{zoomfactor_start}), zoompan=z='min(pzoom+({zoom_speed}-1)/{howmanyzooms},{zoom_speed})':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={x_size}x{y_size}" -t {howmanyseconds} ./{simfold}/{prefix}%0{zfill}d.png"""
    )
    try:
        os.unlink(simpic)
    except Exception:
        pass
    try:
        os.unlink(simfold)
    except Exception:
        pass
    try:
        tempicture_delete()
    except Exception:
        pass
    rec = regex.compile(rf"^{prefix}\d{{{zfill}}}\.png")
    allfiles = list(
        sorted(
            [
                os.path.normpath(os.path.join(outputfolder, x))
                for x in os.listdir(outputfolder)
                if rec.search(x) is not None
            ]
        )
    )
    return allfiles


