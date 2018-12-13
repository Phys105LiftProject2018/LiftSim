@echo off
reg Query "HKLM\Hardware\Description\System\CentralProcessor\0" | find /i "x86" > NUL && set OS=LiftSimEnv32 || set OS=LiftSimEnv64


if %1.==. (
    REM If no argument has been provided - execute without arguments
    .\%OS%\Scripts\python.exe Results.py
) else (
    if %2.==. (
		REM If only the first argument has been provided - execute with the first argument
		.\%OS%\Scripts\python.exe Results.py %1
	) else (
		if %3.==. (
			REM If the first and second argument has been provided - execute with the first and second arguments
			.\%OS%\Scripts\python.exe Results.py %1 %2
		) else (
			.\%OS%\Scripts\python.exe Results.py %1 %2 %3
		)
	)
)

pause