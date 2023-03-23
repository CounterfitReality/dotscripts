
INSTALL_DIR = ~/.scripts
BIN_DIR = ~/bin

.PHONY: link unlink

link:
    ln -s $(CURDIR)/password-creator $(INSTALL_DIR)/password-creator
    ln -s $(CURDIR)/image-downloader $(INSTALL_DIR)/image-downloader
    ln -s $(INSTALL_DIR)/password-creator $(BIN_DIR)/password-creator
    ln -s $(INSTALL_DIR)/image-downloader $(BIN_DIR)/image-downloader

unlink:
    rm -f $(INSTALL_DIR)/password-creator
    rm -f $(INSTALL_DIR)/image-downloader
    cp $(INSTALL_DIR)/password-creator $(BIN_DIR)/password-creator
    cp $(INSTALL_DIR)/image-downloader $(BIN_DIR)/image-downloader
