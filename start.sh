if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/SECCOMPLEX/AutoFilterSECLK.git /AutoFilterSECLK
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /AutoFilterSECLK
fi
cd /AutoFilterSECLK
pip3 install -U -r requirements.txt
echo "Starting AutoFilterSECLK...."
python3 bot.py
