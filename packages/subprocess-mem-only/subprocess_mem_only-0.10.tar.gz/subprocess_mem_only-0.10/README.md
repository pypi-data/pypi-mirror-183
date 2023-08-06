# Pass a variable as a SpooledTemporaryFile directly to subprocess.

```python
$pip install subprocess-mem-only
from subprocess_mem_only import subprocess_with_spooledtempfile

var_as_binary= b'Hi there, how are you?\nYou are my best friend'

resi = subprocess_with_spooledtempfile(
    command=["grep", r"\bmy\b"], content=var_as_binary
)
print(resi)
CompletedProcess(args=['grep', '\\bmy\\b'], returncode=0, stdout=b'You are my best friend\n', stderr=b'')

```


