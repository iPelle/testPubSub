# INstall pip
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
sudo python get-pip.py

# Install gcp
#sudo pip install google-cloud

# INstall pubsub
sudo pip install --upgrade google-cloud-pubsub

# install these pip requirements
google-cloud-pubsub==0.23

# Install GIT
sudo apt-get install git

#Clone PubSub test
git clone https://github.com/iPelle/testPubSub

#Clone python samples
git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git

# Install datalab
sudo apt-get install google-cloud-sdk-datalab


# Startup datalab
datalab create mydatalabvm --zone us-east1-b


