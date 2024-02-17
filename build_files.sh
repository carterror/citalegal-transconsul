# build_files.sh
apt install sqlite3
pip install -r requirements.txt
python3.9 manage.py collectstatic