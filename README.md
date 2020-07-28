# DownloadSorter

I download a bunch of random files all the time (memes, videos, songs, installers, etc etc) so I wanted an easy and automated way to shuffle things into different folders based on type. 
This is a quick download sorter tool to create folders and shuffle files into them based on file type. It re-checks the directory every 15 seconds and shuffles files accordingly. 

To use: create a directory.txt file in the same directory as this program, and enter the full directory you want monitored. Hit the start.bat to start the program in a CMD window. 

The default folders and corresponding extensions are 
* Images (jpg, jpeg, bmp, png, gif)
* Music Files (mp3, wav)
* Videos (webm, mp4)
* Executables and Installers (exe, msi, jar)
* Archives (zip, 7z, rar)
* Documents (docx, doc, pdf)
* Torrents (torrent)

The extensions/folders are in a dictionary and can be easily extended. If a file does not fit into any of these, it will just be left in the main thing.
On first initialize it will create the folders if they are not created automatically.

Room to grow:
* Making something like this in a different language (like C#) so that it would be portable would be useful for others. Adding a simple GUI to add extensions and folders would be really useful. The core mechanics aren't too complicated, so the libraries must definitely already exist in C#. 
* Making it start on windows start would be nice, and making it run without needing a CMD window to be open would be neater. 


