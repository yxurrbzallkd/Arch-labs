PYTHON=python3
PIP=pip3
$PIP install django
cd facade
$PYTHON manage.py runserver 8000&
F_ID=$!
cd ..
cd logger
$PYTHON manage.py runserver 7000&
L_ID=$!
cd ..
cd messages
$PYTHON manage.py runserver 5000&
M_ID=$!
cd ..
echo "Enter any character to terminate"
read -n 1
kill $F_ID
kill $L_ID
kill $M_ID
cd logger
python manage.py flush # clear database
cd ..