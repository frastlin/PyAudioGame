<title>Getting Started -- Basic Tutorial</title>

[Back to index](index.html)

__________

#What you need
To do this tutorial you will need
[python 32 bit](https://www.python.org/download/releases/2.7.8/) or the full install of pyaudiogame with the pyaudiogame.bat file  
and a  
[text editor.](http://www.EmpowermentZone.com/edsetup.exe)  
\*Note\* You can use python 2 or 3 with this tutorial and package, you just need to make sure you have all the correct dependencies for pyaudiogame to work. (Those include all the packages in requirements and [pygame).](http://pygame.org/news.html)  
if you are using the included python distribution, you don't need to worry, everything is installed for you.
#how to run scripts
Python files with your code are called "scripts" so when you hear "run the script" it is the same as "run the code".  
##saving
You save a python script as a .py file. If you are using a text editor such as EdSharp or notepad, they will often give a default extension like .txt. You need to change this when you type the name of your document. hit ctrl+a while you are in the filename box and then type your document's name and type .py, so like: ex1.py.  
If you use a word processor like Microsoft Word, they won't let you do this. They will also fill your documents with symbles that python won't like such as leftQuote rather than quote.  
##using the command shell
After you have your .py file, open up a command shell by either clicking on the pyaudiogame.bat file, hitting `ctrl+\` in EdSharp, or by navigating to the place where you saved your file with windows explorer, hitting alt+d and typing "cmd" and hitting enter.  
Use your screen reader's review cursor (Jaws cursor or NVDA's object navigation) to read this window. Check that your current directory  is where you saved your .py file. If it isn't, type  
cd projects  
if you are using the pyaudiogame.bat file, or  
cd programming/python/pyaudiogame/excersizes  
where the / seperates folder names. If you don't know, hit f4 when in windows explorer and it will say something like:  
`c:\users\frastlin\programming\pythonFiles\projects\PyAudioGame\projects`  
If it makes you feel better, use `\` after cd, but `/` is more excepted as you can use it on any system where as `\` is only windows.  
If your extension has spaces like:  
`c:\Program Files (x86)`  
put it in quotes after cd like:  
`cd "c:\Program Files (x86)"`  
So if your windows explorer says something like:  
`c:\programming\pythonFiles\PyAudioGame\projects`  
and your command prompt window says:  
`c:\programming\pythonFiles\PyAudioGame`  
you type:  
cd projects  
If you wish to go back out of the folder you are in, type:  
cd ..
##running the .py file
Once you have your command shell open at the correct location, type:  
python filename.py  
to run filename.

#useful things to know about python
When you are in a command shell, you can type  
python  
without any file name to get into what is called the "python interpreter". This is basicly a text file where you can type python commands and see them exicuted right away.  
##environment variables
If you installed python and are not using the pyaudiogame.bat file, you need to set python in the environment variable before the "python" command will work.  
First hit the windows key to get into the start menu. arrow down once and hit c till you hear "computer". Hit applications (or right-click) on this and arrow up for properties. Hit enter.  
In the "system" window tab till you hear "change settings". In windows 7 this is 3 times. Hit enter.  
In the computer properties window hit ctrl+tab till you hear "advanced"  
\*note\*You need to be logged in as an administrator to go past this point  
tab till you hear "environment variables..." and hit enter.  
now tab 4 times and you should hear "system variables". Arrow down 4 times and you will hear "path;". Hit alt+i.  
\*warning warning warning!!!!\* If you delete anything in here, it will do bad things to your computer, so be very careful! Hit escape and do the process over if you delete something.  
in the edit system variable diologue hit ctrl+end to get to the last entry. Hit left arrow to check if there is a `;` at the end of the last character. If not add one. Now type:  
for python 2.7  
;c:\python27;c:\python27\scripts  
for python 3.4 do:  
;c:\python34;c:\python34\scripts  
Now tab once and hit the OK button. Tab till you hear the OK button again and hit enter. Hit tab once and hit the OK button again. Now open up a command shell and type  
python  
if you get: python is not recognised as an internal or external command, operable program or batch file.  
restart your computer and try it again.  
If it still doesn't work, go to computer, OSc (c:\) and hit p till you hear "python". if it has a different number at the end than what you typed, change it in your environment variable by following the steps above.  
##notes on EdSharp
EdSharp is a very complex and fantastic text editor that is built for blind programmers. The user guide is very long and very detailed and is a little more than what most people would like to sit down and read. So here are some of the more useful commands and settings you should set:  
###settings
hit alt+shift+c  
extension default should be either:  
*  
or  
.py  
indent unit should be:  
\t  
word wrap  
n  
extra speech:  
y  
###commands
tab anywhere in a line to indent it  
press ctrl+return to indent the next line the same amount as the last line    
You can select a block of code and press tab to indent and shift+tab to unindent everything.  
You can select a block of code and press ctrl+q to quote and ctrl+shift+q to unquote the code.  
To jump between blocks of code press ctrl+up and ctrl+down arrows  
To open up a command prompt press ctrl+\  
To open up file explorer press alt+\  
to delete the current line of code press ctrl+d  
press ctrl+c without selecting to copy the current line  
You can use expressions like `\t, and \n` in your replace or search options.    
