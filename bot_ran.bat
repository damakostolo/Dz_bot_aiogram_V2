@echo off

call %~dp0Dz_bot\venv\Scripts\activate

cd %~dp0Dz_bot

set TOKEN=6476647584:AAHGHKAHRVudthCWaMmO3vg6AvtMYPMHtoA

python bot_telegram.py 

pause