This is a python exe form compiled for windows using cx_Oracle and Tkinter

In order to get this to work you must have all proper cx_Oracle files ("instant_client")

I found that pip install works best for cx_Oracle install.

Make sure to have python dir set as "C:\Python27\"

drop instant client folder in this dir ^

grab pip install and compile it for windows then install cx_Oracle pip install cx_Oracle 

you might get a warning about the c++ compiler you have to download the MS c++ compiler then retry pip install of cx_Oracle

Download it from here ---> https://www.microsoft.com/en-us/download/details.aspx?id=44266

install pyinstaller or py2exe which ever is your prefered stack if py2exe use a setup.py file in sub dir

then compile 

===========================================================================================