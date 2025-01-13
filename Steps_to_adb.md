
## ADB command

- USB devices

```

adb --version

adb devices -l

adb shell ls

adb shell ls storage/emulated/0/

adb shell ls storage/emulated/0/qpython/stocks3

adb pull storage/emulated/0/qpython/stocks3/aaazhulicheck.py

adb push aaazhulicheck.py storage/emulated/0/qpython/stocks3
```

