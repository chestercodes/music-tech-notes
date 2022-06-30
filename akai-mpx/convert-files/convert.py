import os
import glob
from subprocess import call

print("Convert files...")

root_dir = os.path.dirname(os.path.realpath(__file__))

raw_dir = root_dir + "/files/raw"
raw_files = glob.glob(raw_dir + "/**/*", recursive=True)

out_dir = root_dir + "/files/out"
if not os.path.exists(out_dir):
    os.mkdir(out_dir)

for raw_file in raw_files:
    if os.path.isdir(raw_file):
        continue
    
    raw_file_name = os.path.basename(raw_file)
    out_path = out_dir + "/" + raw_file_name
    print(raw_file + " -> " + out_path)

    if os.path.exists(out_path):
        os.remove(out_path)

    # -ac 1 -> mono
    # -ar 48000 -> 48khz
    # -acodec pcm_s16le -> 16bit
    try:
        call(('ffmpeg', '-i', raw_file, '-ac', '1', '-ar', '48000', '-acodec', 'pcm_s16le', out_path))

    except Exception as err:
        print("call failed")
        print(err)
