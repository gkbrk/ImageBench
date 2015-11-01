import time
import subprocess
import os
import glob

jpg_images = glob.glob("images/*.jpg");

benchmarks = [
        {"name": "libjpeg-turbo decode scanlines (500 times)", "dir": "benchmarks/libjpeg", "compile": "make compile", "run": "bench", "images": jpg_images},
        {"name": "Rust-Image JPEG Decode scanlines (500 times)", "dir": "benchmarks/rustimage_bench", "compile": "cargo build --release --bin jpeg_scanline", "run": "target/release/jpeg_scanline", "images": jpg_images},
        {"name": "Rust-Image JPEG Decode full (500 times)", "dir": "benchmarks/rustimage_bench", "compile": "cargo build --release --bin jpegread", "run": "target/release/jpegread", "images": jpg_images}
]

for bench in benchmarks:
    print("Compiling the {} benchmark".format(bench["name"]))
    subprocess.Popen(bench["compile"].split(), cwd=bench["dir"]).wait()
    print("Running the {} benchmarks".format(bench["name"]))
    for img in bench["images"]:
        start = time.time()
        subprocess.Popen([os.path.join(bench["dir"], bench["run"]), img]).wait()
        end = time.time()
        print("The {} benchmark took {} seconds to run. [{}]".format(bench["name"], end-start, img))
