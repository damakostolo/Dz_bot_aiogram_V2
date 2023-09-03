@echo off

call %~dp0telegram_bot\venv\Scripts\activate

cd %~dp0telegram_bot

set TOKEN=6476647584:AAHGHKAHRVudthCWaMmO3vg6AvtMYPMHtoA

python bot_pizza.py 

pause