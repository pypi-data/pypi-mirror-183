# pyFileWatcher - A library for monitoring files and directories for changes
The python package for monitoring files and directories provides a fast and efficient way to detect changes to files and directories. It is particularly small and resource-efficient, making it ideal for use in environments with limited resources.
The package is also easy to integrate and can be effortlessly incorporated into existing projects. It provides icomprehensive documentation to get you started.
Overall, our Python package for monitoring files and directories is a powerful and reliable choice for anyone who wants to monitor changes to files and directories.

## Installation
### pip
```bash
python3 -m pip install --user pyfilewatcher
```

### Manual
**Currently still in progress!**

## Example
```python
from pyfilewatcher import FileWatcher

file = FileWatcher(name="Test", files=["example.log"], interval=1)
file()
```