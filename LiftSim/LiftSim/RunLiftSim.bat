@echo off
reg Query "HKLM\Hardware\Description\System\CentralProcessor\0" | find /i "x86" > NUL && set OS=LiftSimEnv32 || set OS=LiftSimEnv64

if %1.==. (
    REM If an argument has been provided - execute with argument
    .\%OS%\Scripts\python.exe LiftSim.py
) else (
    .\%OS%\Scripts\python.exe LiftSim.py %1
)

pause