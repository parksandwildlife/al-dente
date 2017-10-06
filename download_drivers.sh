mkdir -p drivers
wget -qO- https://github.com/mozilla/geckodriver/releases/download/v0.19.0/geckodriver-v0.19.0-linux64.tar.gz | tar xvz -C drivers
wget https://chromedriver.storage.googleapis.com/2.33/chromedriver_linux64.zip -O tmp.zip
unzip -u tmp.zip -d drivers
rm tmp.zip
