import subprocess
from tempfile import SpooledTemporaryFile


def create_spooledtempfile_with_content(content: bytes):
    f = SpooledTemporaryFile()
    f.seek(0)
    f.write(content)
    f.seek(0)
    return f


def subprocess_with_spooledtempfile(command: list, content: bytes):
    data = None

    try:
        file = create_spooledtempfile_with_content(content=content)
        data = subprocess.run(command, stdin=file, capture_output=True, shell=True)
    finally:
        try:
            file.close()
        except Exception:
            pass
    return data
