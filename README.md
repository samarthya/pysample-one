# A Sample Python Project

- Will use unittest to test

```bash
> python -m unittest 
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

## Code structure

```bash
.
├── README.md
├── setup.py
├── square.py
└── test_square.py
```

## Binary distribution

You can create a binary executable by using pyinstaller

### Installing pyinstaller

```bash
pip3 install pyinstaller
```

### Create binary `pyinstaller --onefile square.py`

```bash
> pyinstaller --onefile square.py

159 INFO: PyInstaller: 5.7.0
159 INFO: Python: 3.10.9
196 INFO: Platform: macOS-13.1-arm64-arm-64bit
197 INFO: wrote /Users/samarthya/sourcebox/github.com/python-projects/sample1/square.spec
207 INFO: UPX is not available.
226 INFO: Extending PYTHONPATH with paths
['/Users/samarthya/sourcebox/github.com/python-projects/sample1']
457 INFO: checking Analysis
457 INFO: Building Analysis because Analysis-00.toc is non existent
457 INFO: Initializing module dependency graph...
464 INFO: Caching module graph hooks...
470 INFO: Analyzing base_library.zip ...
1435 INFO: Loading module hook 'hook-heapq.py' from '/opt/homebrew/lib/python3.10/site-packages/PyInstaller/hooks'...
1503 INFO: Loading module hook 'hook-encodings.py' from '/opt/homebrew/lib/python3.10/site-packages/PyInstaller/hooks'...
2521 INFO: Loading module hook 'hook-pickle.py' from '/opt/homebrew/lib/python3.10/site-packages/PyInstaller/hooks'...
3402 INFO: Caching module dependency graph...
3462 INFO: running Analysis Analysis-00.toc
3468 INFO: Analyzing /Users/samarthya/sourcebox/github.com/python-projects/sample1/square.py
3470 INFO: Processing module hooks...
3477 INFO: Looking for ctypes DLLs
3478 INFO: Analyzing run-time hooks ...
3479 INFO: Including run-time hook '/opt/homebrew/lib/python3.10/site-packages/PyInstaller/hooks/rthooks/pyi_rth_inspect.py'
3482 INFO: Looking for dynamic libraries
3856 INFO: Looking for eggs
3857 INFO: Using Python library /opt/homebrew/Cellar/python@3.10/3.10.9/Frameworks/Python.framework/Versions/3.10/Python
3861 INFO: Warnings written to /Users/samarthya/sourcebox/github.com/python-projects/sample1/build/square/warn-square.txt
3868 INFO: Graph cross-reference written to /Users/samarthya/sourcebox/github.com/python-projects/sample1/build/square/xref-square.html
3893 INFO: checking PYZ
3893 INFO: Building PYZ because PYZ-00.toc is non existent
3893 INFO: Building PYZ (ZlibArchive) /Users/samarthya/sourcebox/github.com/python-projects/sample1/build/square/PYZ-00.pyz
4000 INFO: Building PYZ (ZlibArchive) /Users/samarthya/sourcebox/github.com/python-projects/sample1/build/square/PYZ-00.pyz completed successfully.
4002 INFO: EXE target arch: arm64
4002 INFO: Code signing identity: None
4002 INFO: checking PKG
4002 INFO: Building PKG because PKG-00.toc is non existent
4002 INFO: Building PKG (CArchive) square.pkg
7892 INFO: Building PKG (CArchive) square.pkg completed successfully.
7895 INFO: Bootloader /opt/homebrew/lib/python3.10/site-packages/PyInstaller/bootloader/Darwin-64bit/run
7895 INFO: checking EXE
7895 INFO: Building EXE because EXE-00.toc is non existent
7895 INFO: Building EXE from EXE-00.toc
7895 INFO: Copying bootloader EXE to /Users/samarthya/sourcebox/github.com/python-projects/sample1/dist/square
7905 INFO: Converting EXE to target arch (arm64)
8104 INFO: Removing signature(s) from EXE
8185 INFO: Appending PKG archive to EXE
8190 INFO: Fixing EXE headers for code signing
8202 INFO: Re-signing the EXE
8266 INFO: Building EXE from EXE-00.toc completed successfully.
```

You can look up in the dist folder and you will see the binary

```bash
> ls -als dist

total 10512
    0 drwxr-xr-x   3 samarthya  staff       96 Feb  1 10:21 .
    0 drwxr-xr-x  12 samarthya  staff      384 Feb  1 10:21 ..
10512 -rwxr-xr-x   1 samarthya  staff  5380416 Feb  1 10:21 square
```


## Source distribution `python setup.py sdist`

```bash
> python setup.py sdist

running sdist
running egg_info
creating square.egg-info
writing square.egg-info/PKG-INFO
writing dependency_links to square.egg-info/dependency_links.txt
writing top-level names to square.egg-info/top_level.txt
writing manifest file 'square.egg-info/SOURCES.txt'
reading manifest file 'square.egg-info/SOURCES.txt'
writing manifest file 'square.egg-info/SOURCES.txt'
running check
creating square-1.0
creating square-1.0/square.egg-info
copying files to square-1.0...
copying README.md -> square-1.0
copying setup.py -> square-1.0
copying square.py -> square-1.0
copying square.egg-info/PKG-INFO -> square-1.0/square.egg-info
copying square.egg-info/SOURCES.txt -> square-1.0/square.egg-info
copying square.egg-info/dependency_links.txt -> square-1.0/square.egg-info
copying square.egg-info/top_level.txt -> square-1.0/square.egg-info
Writing square-1.0/setup.cfg
Creating tar archive
removing 'square-1.0' (and everything under it)
```
A quick listing in the fist folder will show the newly `gz` file that has the source