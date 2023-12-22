@echo off
git add .
cls
set /p r=Name changes: 
git commit -m "%r%"
cls
git push origin main
cls
echo Done!