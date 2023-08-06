import setuptools
setuptools.setup(
    long_description="""# FoxBox

Foxbox is a python package to simplify messagebox and bin converter.

## Installation


```bash
pip install foxbox
```

## Usage

```python
from foxbox import * #Be sure to add * to import all Subpackages

int2bin(15)
# returns 1111

bin2int(1111)
# returns 15

str2bin('Text')
# returns 01110100011001010111100001110100

bin2str('01110100011001010111100001110100') #Add binairy text into ''

box("Text", MB_ICONQUESTION | MB_CANCELTRYCONTINUE, "Title")
           #Message box icon| Message box mode
file('filename.anyformat')
#create a file
```

## Message box mode list

### Mode

MB_ABORTRETRYIGNORE\n
MB_CANCELTRYCONTINUE\n
MB_HELP\n
MB_OK\n
MB_OKCANCEL\n
MB_RETRYCANCEL\n
MB_YESNO\n
MB_YESNOCANCEL
_________
### Icons

MB_ICONEXCLAMATION\n
MB_ICONWARNING\n
MB_ICONINFORMATION\n
MB_ICONASTERISK\n
MB_ICONQUESTION\n
MB_ICONSTOP\n
MB_ICONERROR\n
MB_ICONHAND
_____
### Buttons value

IDABORT = 3\n
IDCANCEL = 2\n
IDCONTINUE = 11\n
IDIGNORE = 5\n
IDNO = 7\n
IDOK = 1\n
IDRETRY = 4\n
IDTRYAGAIN = 10\n
IDYES = 6
___

#### Examples

```python
from foxbox import *
mybox = box("SOMETHING WEN WRONG. would you like to restart?", MB_ICONERROR | MB_YESNO, "ERROR!")
if mybox == IDYES:
    print('Restarted!')
if mybox == IDYES:
    print('Closed')
```

## Help

Thanks for use if you have any question join my Discord server link here [(--)](https://discord.gg/c6twk26h)

## What's new?

v0.0.1 - first release\n
v0.0.2 - updating package file\n
v0.0.3 - description added\n
v0.0.4 - changed description (current)\n
v0.0.5 - deleted markdown readme

""",
    long_description_content_type='text/markdown',
    name="FoxBox",
    version='0.0.5',
    author="Batte",
    description="An usefull package",
    packages=["foxbox"]
)
