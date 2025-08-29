# 🌏🐉 Journey to the West  

[![Python](https://img.shields.io/badge/python-3.13.2-blue?logo=python&logoColor=white)](https://www.python.org/) 
[![Django](https://img.shields.io/badge/django-5.2-green?logo=django&logoColor=white)](https://www.djangoproject.com/) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 

**Journey to the West** is a Django-based blog platform that comes with authentication, custom profiles, rating system, related objects, and extended blog features.  
This is my first official Django project published on GitHub and it is still under active development.  

---

## ✨ Features  

### ✅ Implemented
- **Blog System**
  - Blog list & detail pages  
  - Similar posts suggestion (via custom template tags)  
  - Highlight searched section
- **Authentication**
  - User registration & login system  
  - Automatic profile creation using Django signals  
- **Profiles & Interaction**
  - Custom profile page for each user
  - Editing profile system
  - User rating system  
- **Utilities**
  - About Us & Contact Us pages  
  - Custom template tags for advanced template logic  
- **SEO / Robots**
  - Dynamic `robots.txt` and `sitemap.xml` integration  

### 🔧 Upcoming
- **Role Management**
  - Three roles: **Writer**, **Critic**, & **Reader**  
  - Writers can create and manage posts
  - Critics can send comments
  - Reader can view the site
- **Post Submission**
  - Writers can submit draft posts for review  
- **Commenting System**
  - Threaded comment support on blog posts  
- **Security**
  - Using **Bleach** to sanitize post content before saving

---

## 🛠 Tech Stack
- **Backend:** Django (Python)  
- **Database:** SQLite (development)  
- **Frontend:** Django Template Language (DTL), HTML5, CSS3  
- **Other Tools:** Django Signals, Custom Template Tags, Bleach  

---

## 📦 Installation  

    git clone https://github.com/your-username/journey_to_the_west.git
    cd journey_to_the_west

    python -m venv venv
    source venv/bin/activate   # On Linux/Mac
    venv\Scripts\activate      # On Windows

    pip install -r requirements.txt
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

---

## 👤 Usage  
- Visit `http://127.0.0.1:8000/blog/` for blog pages  
- Register as a new user or log in  
- View and edit your profile  
- Rate other users  
- Explore custom features like similar posts  

---

## 📌 Roadmap  
- [ ] Writers can submit posts 
- [ ] Display related objects
- [ ] Commenting system  
- [ ] Post sanitization with Bleach  
- [ ] Robots.txt & sitemap integration  

---

## 🤝 Contributing  
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.  

---

## 📜 License  
This project is licensed under the MIT License.  
