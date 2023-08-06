import os

from easy_symlink import create_symlink

from touchtouch import touch


def convert_vid(videofile, outputfile):
    try:
        touch(outputfile)

        vidsym1 = f"__socialnetworktmmmmmmpin.{videofile.split('.')[-1]}"
        create_symlink(videofile, vidsym1)
        vidsym2 = f"__socialnetworktmmmmmmpout.{outputfile.split('.')[-1]}"
        create_symlink(outputfile, vidsym2)

        os.system(
            f"""ffmpeg -i {vidsym1} -y -codec:v libx264 -preset slow -filter:v fps=29.97 {vidsym2}"""
        )
        try:
            os.unlink(vidsym1)
        except Exception:
            pass
        try:
            os.unlink(vidsym2)
        except Exception:
            pass
    except Exception as Fehler:
        print(Fehler)


