# 🎟️ EventEase – Event Ticket Booking System

**EventEase** is a full-stack Django web application that allows users to browse and book event tickets with QR code confirmation. Admins and organizers can manage events, view analytics, and export booking data.

---

## 🔥 Features

### 👤 User Features:
- Register and login securely
- Book tickets for available events
- Receive email confirmation after booking
- Get a downloadable **QR code** for each ticket
- View **your booking history** in `/my-bookings/`
- Automatically join **waitlist** if an event is full

### 🛠️ Admin Features:
- Create, edit, delete events via Django admin panel
- View all bookings and registered users
- Export booking data to **CSV**
- View booking statistics in **Analytics Dashboard**
- Manually notify users from the waitlist (if needed)

---

## 🧑‍💻 Tech Stack

- **Backend**: Django 4.2
- **Frontend**: HTML, Bootstrap 5
- **Database**: PostgreSQL
- **Auth**: Django Authentication System
- **Extras**: QR Code Generation, Chart.js, CSV Export

---

## 🚀 Getting Started

## 🛠️ Installation

```bash
git clone https://github.com/Getsand/eventease-or-event-ticket-booking.git
cd eventease
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Visit: http://127.0.0.1:8000/

## simple file structure

eventease/
├── eventapp/
│   ├── models.py        # Event, Ticket, Waitlist models
│   ├── views.py         # Booking, dashboard, QR logic
│   ├── urls.py
├── dashboard/
│   ├── views.py         # export CSV, analytics
├── templates/
│   ├── eventapp/        # booking list, my bookings
│   ├── dashboard/       # analytics view
├── static/
│   ├── css/style.css
├── media/               # stores QR codes
├── .env
├── requirements.txt
└── README.md


🔐 User Actions
Action	URL
Sign up	/register/
Login	/accounts/login/
Book Event	/ (home)
My Bookings	/my-bookings/
Logout	/accounts/logout/

👨‍💼 Admin Actions
Action	URL
Admin Panel	/admin/
Create Event	via Admin Panel
Export Bookings	/dashboard/export/
View Analytics	/dashboard/analytics/

✅ Use the superuser credentials you created to log in as admin.

python manage.py createsuperuser
Username: admin
Email address: admin@example.com
Password: ********
Password (again): ********




