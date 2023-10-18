@echo off
PUSHD ..

docker-compose up -d code --build
rem timeout 1
rem docker attach hw08-code-1

rem docker-compose down 

POPD