import os
os.system("""
cd
git clone https://github.com/cccvev/ELSHAPEH-ELMODAMER
mv ELSHAPEH-ELMODAMER $HOME
mv ELSHAPEH-ELMODAMERRR $HOME
cd
cd ELSHAPEH-ELMODAMERRR
mkdir .vmaker
cd
cd ELSHAPEH-ELMODAMER
mv * /data/data/com.termux/files/home/ELSHAPEH-ELMODAMERRR/.vmaker
cd
cd ELSHAPEH-ELMODAMERRR
python ELSHAPEH-ELMODAMER.py

""")
