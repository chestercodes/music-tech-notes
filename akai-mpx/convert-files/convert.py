import os
import glob

print("Convert files...")

root_dir = os.path.dirname(os.path.realpath(__file__))

raw_dir = root_dir + "/raw"
raw_files = glob.glob(raw_dir + "/*")

out_dir = root_dir + "/out"
if not os.path.exists(out_dir):
    os.mkdir(out_dir)

for raw_file in raw_files:
    out_path = raw_file.replace(raw_dir, out_dir)
    print(raw_file + " -> " + out_path)

    if os.path.exists(out_path):
        os.remove(out_path)

    # -ac 1 -> mono
    # -ar 48000 -> 48khz
    # -acodec pcm_s16le -> 16bit
    extra_args = " -ac 1 -ar 48000 -acodec pcm_s16le " + out_path
    c = "ffmpeg -i " + raw_file + extra_args
    print(c)
    try:
        os.system(c)
    except Exception as err:
        print("call failed")
        print(err)
