<h1><center>Download Sorter</center></h1>

## Description
<p>Automate sorting of the downloaded files according to their type.</p>

## Features
<li>Stores image, document, video and audio in separate files</li>
<li>Creates new directory if the directory is not present</li>
<li>Assigns unique name if file with same name is already in the directory</li>
<li>Stores other type of file in others directory</li>

## How to use
###  This instruction is only for linux operating system. 
If you are a windows of mac user this instruction will not work properly. You can run the script just like a normal python script but this instruction doesn't contain any ways to run the script at startup in windows or mac. 
### Step 1.
Clone this repository using this command:
``` console
git clone https://github.com/shihabalratul/download_sorter.git
```
### Step 2.
Open the file and install the dependencies:
</br>
``` console
cd download_sorter
pip3 install -r requirements.txt
```

### Step 3.
Open <code>download_sorter.py</code> file and set the download directory path to the <code>source</code> variable like this:
<pre>source='/home/user/Downloads'</pre> and save.

### Step 4.
Run the script at startup:

Open terminal and run:
``` console
crontab -e
```
Add this line at the bottom with the directory of this file:
``` 
@reboot /usr/bin/python3 [file_directory]/download_sorter.py
```
Here replace the <code>[file_directory]</code> with the full directory the script.

### Step 5.
### Enjoy Your Downloading
Download or copy anything in the download folder and see the magic.
