README

A simple SQL project with three different query outputs, the first is to find the three most popular articles, the second is to find the three most popular authors and the third is to find the percentage of errors for each day.

To use the same virtual machine to run this SQL database, you will first need to download VirtualBox, this will run the virtual machine. You do not need the extension pack, SDK or to launch the virtualbox, vagrant will do that. This is the link to download virtual box:

https://www.virtualbox.org/wiki/Download_Old_Builds_5_1

Download vagrant, install the version for your operating system. This is the link:

https://www.vagrantup.com/downloads.html

Fork and clone this github repository:

https://github.com/udacity/fullstack-nanodegree-vm

Navigate into the cloned directory, you will find another directory called vagrant, cd into this directory. From the terminal inside the vagrant subdirectory, run the command "vagrant up". This will download and install the Linux operating system. Once "vagrant up" is finished, you can run vagrant ssh to log into your new Linux VM.

Once you are logged in, change into the shared vagrant sub-directory using "cd /vagrant". This will be the subdirectory directly inside the "fullstack-nanodegree-vm" called vagrant. Anything you save in this subdirectory can be accessed using the Linux VM.

Download the following newsdata file, and unzip into the vagrant folder. 

https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

Download the newsDB.py file into the newsdata folder. Login to your vagrant directory using your linux command line, navigate to the newsdata folder. Once in the newsdata folder, input into the command line:

psql -d news -f newsdata.sql

Utilizing psql, connect to the database named news and run the sql statements in the newsdata.sql file.

Once in the Linux VM, and in the newsdata folder, type "python newsDB.py" in the command line, the program will run in the command line.

Author
James Moore

Unlicensed