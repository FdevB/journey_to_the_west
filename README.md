# 🐉 Journey to the West

A simple **blog website** built with **Django 5.2**.

---

## 🚀 How to Use

Clone the repository, create a virtual environment, install requirements, set up the database, and run the server:

```bash
git clone <repo-link>
cd journey_to_the_west

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

pip install -r requirements.txt

# Update database settings in settings.py if needed
# Change SECRET_KEY in settings.py to your own secure key

python manage.py migrate
python manage.py createsuperuser   # optional, for admin access

python manage.py runserver
