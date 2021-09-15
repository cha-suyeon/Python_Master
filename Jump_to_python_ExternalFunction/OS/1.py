# OS 모듈은 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈

# 내 시스템의 환경 변수 값을 알고 싶을 때
# os.environ

import os
os.environ

# 결괏값
# environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\chasu\\AppData\\Roaming', 'CHROME_CRASHPAD_PIPE_NAME': '\\\\.\\pipe\\crashpad_17308_BYMNVHTMYDHVSZML', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'DESKTOP-3UD70VS', 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\chasu', 'LOCALAPPDATA': 'C:\\Users\\chasu\\AppData\\Local', 'LOGONSERVER': '\\\\DESKTOP-3UD70VS', 'NUMBER_OF_PROCESSORS': '12', 'ONEDRIVE': 'C:\\Users\\chasu\\OneDrive', 'ORIGINAL_XDG_CURRENT_DESKTOP': 'undefined', 'OS': 'Windows_NT', 'PATH': 'C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\NVIDIA Corporation\\NVIDIA NvDLISR;C:\\Program Files\\TortoiseGit\\bin;C:\\Program Files\\Git\\cmd;C:\\Ruby30-x64\\bin;C:\\Ruby27-x64\\bin;C:\\Users\\chasu\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.3\\bin;;C:\\Users\\chasu\\AppData\\Local\\GitHubDesktop\\bin;C:\\Users\\chasu\\AppData\\Local\\Programs\\Microsoft VS Code\\bin', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.RB;.RBW;.CPL', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 166 Stepping 0, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': 'a600', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\Users\\chasu\\OneDrive\\문서\\WindowsPowerShell\\Modules;C:\\Program Files\\WindowsPowerShell\\Modules;C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PUBLIC': 'C:\\Users\\Public', 'PYCHARM COMMUNITY EDITION': 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.3\\bin;', 'RUBYOPT': '-Eutf-8', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\Windows', 'TEMP': 'C:\\Users\\chasu\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\chasu\\AppData\\Local\\Temp', 'USERDOMAIN': 'DESKTOP-3UD70VS', 'USERDOMAIN_ROAMINGPROFILE': 'DESKTOP-3UD70VS', 'USERNAME': 'chasu', 'USERPROFILE': 'C:\\Users\\chasu', 'WINDIR': 'C:\\Windows', 'ZES_ENABLE_SYSMAN': '1', 'TERM_PROGRAM': 'vscode', 'TERM_PROGRAM_VERSION': '1.60.0', 'LANG': 'ko_KR.UTF-8', 'COLORTERM': 'truecolor', 'VSCODE_GIT_IPC_HANDLE': '\\\\.\\pipe\\vscode-git-4a80526233-sock', 'GIT_ASKPASS': 'c:\\Users\\chasu\\AppData\\Local\\Programs\\Microsoft VS Code\\resources\\app\\extensions\\git\\dist\\askpass.sh', 'VSCODE_GIT_ASKPASS_NODE': 'C:\\Users\\chasu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe', 'VSCODE_GIT_ASKPASS_MAIN': 'c:\\Users\\chasu\\AppData\\Local\\Programs\\Microsoft VS Code\\resources\\app\\extensions\\git\\dist\\askpass-main.js', 'PYTHONUSERBASE': 'C:\\Users\\chasu\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\\LocalCache\\local-packages', 'PYTHONIOENCODING': 'UTF-8', 'PYTHONUNBUFFERED': '1', 'PYDEVD_USE_FRAME_EVAL': 'NO'})