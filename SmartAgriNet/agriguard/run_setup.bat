@echo off
echo Installing required packages...
D:\agriguard\.venv\Scripts\pip.exe install pygame requests opencv-python torch torchvision
echo.
echo Running detect.py...
D:\agriguard\.venv\Scripts\python.exe d:\agriguard\detect.py
pause
