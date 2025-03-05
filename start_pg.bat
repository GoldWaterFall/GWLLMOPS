@echo off
set PG_PATH="C:\Program Files\PostgreSQL\16\bin"
set PG_DATA="C:\Program Files\PostgreSQL\16\data"

echo starting postgresql...
%PG_PATH%\pg_ctl.exe start -D %PG_DATA%
echo postgresql started.