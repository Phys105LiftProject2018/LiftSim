@echo off
reg Query "HKLM\Hardware\Description\System\CentralProcessor\0" | find /i "x86" > NUL && set OS=LiftSimEnv32 || set OS=LiftSimEnv64

.\%OS%\Scripts\python.exe LiftSim.py
pause