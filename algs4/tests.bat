@ECHO OFF
SETLOCAL EnableDelayedExpansion

:: Set GLOBAL Variables 
SET /P OPTION="1-Check Style Only, 2-Find Bugs Only, 3-Both :"
SET /P FILEPATH="Please enter the folder name:"

:: Do we want to checkstyle, findbugs or both?
:runPromptMenu
IF %OPTION%==1 (
ECHO Option 1
CALL :run checkstylelog.txt checkstyle-algs4 java
ECHO Complete!
)
IF %OPTION%==2 (
ECHO Option 2
CALL :run findbugslog.txt findbugs-algs4 class
ECHO Complete!
)
IF %OPTION%==3 (
ECHO Running both
CALL :run checkstylelog.txt checkstyle-algs4 java
CALL :run findbugslog.txt findbugs-algs4 class
ECHO Complete!
)
EXIT /B

::Run the tests and store it to a log file
:run
SET LOGPATH=%FILEPATH%\logs
SET LOGFILE=%1
SET LOGFILEPATH=%lOGPATH%\%LOGFILE%

:: Create a log directory and file if we don't have one.
IF NOT EXIST %LOGPATH% (
MKDIR %LOGPATH%
NUL > %LOGPATH%\%LOGFILE%
)

ECHO Running %2 on %FILEPATH% ... Please be patient

ECHO %date% %time%>>%LOGFILEPATH%
FOR /R %%I IN (%FILEPATH%\*.%3) DO (
CMD /C %2 %%I >> %LOGFILEPATH%
ECHO. >> %LOGFILEPATH% 
)

EXIT /B
