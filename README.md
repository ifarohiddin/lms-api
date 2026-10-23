# 🎓 LMS System API

O'quv markazlari uchun **Learning Management System** backend'i. FastAPI, SQLAlchemy va JWT autentifikatsiya asosida qurilgan. Filiallar, guruhlar, o'qituvchilar va talabalarni boshqarish imkonini beradi.

## ✨ Imkoniyatlar

- 🔐 JWT orqali login (`/token`)
- 👥 Rollar: `superadmin`, `admin`, `teacher`
- 🏢 Filiallarni boshqarish (CRUD)
- 📚 Guruhlarni yaratish va ko'rish
- 🧑‍🎓 Talabalarni guruhlarga biriktirish
- 🔑 Parollar `bcrypt` bilan shifrlanadi

## 🛠️ Texnologiyalar

`Python` · `FastAPI` · `SQLAlchemy` · `SQLite` · `python-jose (JWT)` · `bcrypt` · `Pydantic`

## 🚀 Ishga tushirish

```bash
git clone https://github.com/ifarohiddin/lms-api.git
cd lms-api

python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

pip install -r requirements.txt
cp .env.example .env          # Windows: copy .env.example .env
# .env ichiga SECRET_KEY yozing: python -c "import secrets; print(secrets.token_hex(32))"
uvicorn main:app --reload
```

Swagger hujjatlari: <http://127.0.0.1:8000/docs>

SQLite baza (`lms.db`) birinchi ishga tushishda avtomatik yaratiladi.

## 🔌 Asosiy endpointlar

| Method | Endpoint | Tavsif |
|---|---|---|
| `POST` | `/token` | Login, JWT token olish |
| `POST` | `/users/` | Foydalanuvchi yaratish |
| `GET` | `/users/me` | Joriy foydalanuvchi |
| `GET` | `/users/` | Foydalanuvchilar ro'yxati |
| `GET/POST` | `/branches/` | Filiallar ro'yxati / yaratish |
| `GET/PUT/DELETE` | `/branches/{branch_id}` | Filialni ko'rish / yangilash / o'chirish |
| `GET/POST` | `/groups/` | Guruhlar ro'yxati / yaratish |
| `POST` | `/students/` | Talabani guruhga qo'shish |
| `GET` | `/branches/{branch_id}/students/{group_id}` | Guruhdagi talabalar |

## 📁 Tuzilma

```text
lms-api/
├── main.py         # FastAPI ilova va endpointlar
├── models.py       # SQLAlchemy modellari (User, Branch, Group, StudentGroup)
├── schemas.py      # Pydantic sxemalari
├── database.py     # Baza ulanishi
├── constants.py    # Rollar
└── requirements.txt
```

## 🌱 Rejalar

- [x] `SECRET_KEY` muhit o'zgaruvchisidan (`.env`) o'qiladi
- [ ] Testlar qo'shish
- [ ] Davomat va to'lovlar moduli

## 👤 Muallif

**Isomidinov Farohiddin** — [@ifarohiddin](https://github.com/ifarohiddin)
