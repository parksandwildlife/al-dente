echo "Downloading chromedriver..."
wget -N http://chromedriver.storage.googleapis.com/2.33/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
rm chromedriver_linux64.zip
sudo mv -f chromedriver /usr/local/share/
sudo chmod +x /usr/local/share/chromedriver
sudo ln -sf /usr/local/share/chromedriver /usr/local/bin/chromedriver
echo "Done: /usr/local/bin/chromedriver"

echo "Downloading geckodriver..."
wget https://github.com/mozilla/geckodriver/releases/download/v0.19.0/geckodriver-v0.19.0-linux64.tar.gz
tar xvf geckodriver-v0.19.0-linux64.tar.gz
rm geckodriver-v0.19.0-linux64.tar.gz
sudo mv -f geckodriver /usr/local/share/
sudo chmod +x /usr/local/share/geckodriver
sudo ln -sf /usr/local/share/geckodriver /usr/local/bin/geckodriver
echo "Done: /usr/local/bin/geckodriver"
