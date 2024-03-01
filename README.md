# image-chunker
Python based tool to split a large image into chunks.

Supports [.png, .jpg, .jpeg]

Pre-defined to export 2048x2048 sized chunks.

## Use
- In the source, edit the line with `CHUNK_SIZE` to define the NxN chunks you wish to split your image into.
- Run the `.exe` provided in the latest release, or run the source with `python3`.
  - `python3 image_chunker.py`
- A windows file explorer will open. Select the image.
- A new folder will be created in the directory of the selected image. New directory will open automatically after the process is finished and you'll find the chunked images inside.
- Done!

## Requirements
- python3
- pip3
- Python package: `PIL`
- Python package: `pillow`
- Python package: `pyinstaller` (To create .exe from source)

## Setup
[python3 download](https://www.python.org/downloads/) will include latest version of pip
Install pip packages:
```python
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade pyinstaller
python3 -m pip install --upgrade Pillow --no-binary :all:
```

