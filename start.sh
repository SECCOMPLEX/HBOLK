if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/SECCOMPLEX/HBOLK.git /HBOLK
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /HBOLK
fi
cd /HBOLK
pip3 install -U -r requirements.txt
echo "Starting HBOLK...."
python3 bot.py
