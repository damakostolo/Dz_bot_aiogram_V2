@echo off

call %~dp0Dz_bot\venv\Scripts\activate

cd %~dp0Dz_bot

set TOKEN=5971340761:AAFCF7-chA51k0Mq-AdgjEjIfoZ4bYYAZNE

python bot_telegram.py 

pause