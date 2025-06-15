# 🎟️ EventEase – Event Ticket Reservation System

A scalable full-stack **Django** application to book tickets for events with user roles, concurrency protection, dashboards, and booking analytics.

---

## 🚀 Features

- 👥 Role-based access (Admin, Organizer, Attendee)
- 🎫 Event listing, seat availability, and booking
- 💳 Payment simulation (mock)
- 🔐 Pessimistic locking to avoid double bookings
- 📧 Email confirmation after ticket booking
- 📤 Export tickets as CSV (Admin only)
- 📊 Organizer dashboard with booking analytics
- 🐘 PostgreSQL support, modular app structure

---

## 📦 Tech Stack

- **Backend:** Django, Python
- **Frontend:** HTML, Bootstrap, Chart.js
- **Database:** PostgreSQL
- **Others:** Django Auth, CORS, Bootstrap4

---

## 🛠️ Installation

```bash
git clone https://github.com/yourusername/eventease.git
cd eventease
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
