TIMESTART=$EPOCHSECONDS

# Install required packages
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install python3-pip -y
sudo pip3 install --upgrade pip
sudo pip3 install -r requirements.txt

# Create templates directory and move index.html if needed
mkdir templates  # Uncomment this line if you have an index.html file to move
# mv index.html templates/  # Uncomment this line if you have an index.html file to move

echo "Setup took $((EPOCHSECONDS - TIMESTART)) seconds"

echo "Now execute..."
echo "export FLASK_APP=app.py; python3 -m flask run --host=0.0.0.0 --port=8000"
