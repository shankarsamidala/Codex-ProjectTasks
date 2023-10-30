*DJANGO SETUP
pip install virtualenv
python -m virtualenv myenv
source myenv/scripts/activate
pip install -r req.txt
django-admin startproject olx_clone
ls
python manage.py frunserver
follow link(development server)
python manage.py startapp products