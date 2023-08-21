@echo off

:fetch
for /f "delims=" %%i in ('git fetch -f') do set check=%%i

if %check%==0 exit /b
goto :fetch
