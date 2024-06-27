@echo off

rem Set the directory path where zip files are located
set "sourceDir=C:\Users\c2tlha\Desktop\data-engineering\Dataset\terencicp"

rem Check if source directory exists
if not exist "%sourceDir%" (
    echo Directory "%sourceDir%" not found.
    pause
    exit /b 1
)

rem Change the current directory to the source directory
cd /d "%sourceDir%" || (
    echo Cannot change to the directory "%sourceDir%"
    pause
    exit /b 1
)

rem Loop through each zip file in the source directory
for %%f in (*.zip) do (
    rem Extract each zip file directly into the current directory
    7z x "%%f" -o"%%~dpf"
    
    rem Check if extraction was successful before deleting the zip file
    if errorlevel 1 (
        echo Error extracting "%%f"
        pause
        exit /b 1
    ) else (
        rem Delete the zip file after extraction
        del "%%f"
    )
)

rem Display message indicating process completion
echo All zip files extracted and deleted successfully.
pause
