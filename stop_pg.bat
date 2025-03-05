@echo off
set PG_PATH="C:\Program Files\PostgreSQL\16\bin"
set PG_DATA="C:\Program Files\PostgreSQL\16\data"

echo stoping postgresql...
%PG_PATH%\pg_ctl.exe stop -D %PG_DATA%
echo postgresql stoped.