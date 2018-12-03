@echo off
if %1.==. (
    echo No parameters have been provided.
) else (
    echo Parameters:
    echo %*
)
pause