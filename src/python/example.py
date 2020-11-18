import functions as f
import os

temp_dir =  os.path.join(os.pardir, os.pardir, "temp")

f.debug("Creating temp dir...")
f.remove_dir(temp_dir)
f.create_dir(temp_dir)
f.debug("Temp dir created")

f.debug("Downloading file...")
f.simple_download_file(
    "https://file-examples-com.github.io/uploads/2017/04/file_example_MP4_1920_18MG.mp4",
    temp_dir,
)
f.debug("File downloaded")