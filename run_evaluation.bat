@echo off
cd /d "%~dp0src"
c:\python314\python.exe evaluate.py > ..\eval_results.txt 2>&1
echo Avaliacao concluida! Verifique eval_results.txt
