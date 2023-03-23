# dotscripts

Password-Creator and Image-Downloader

This repository contains two scripts: password-creator and image-downloader. The Makefile in this repository can be used to install and uninstall these scripts on your system.

Installation:

To install the scripts, navigate to the directory containing the Makefile and run the command:

    make link

This will create symbolic links between ~/bin and ~/.scripts for the two files.

Uninstallation:

To uninstall the scripts, navigate to the directory containing the Makefile and run the command:

    make unlink

This will remove the symbolic links and leave copies of the files in ~/bin.

Note: The Makefile assumes that you have ~/.scripts and ~/bin directories already set up on your system. If this is not the case, you will need to create these directories before running the Makefile.
