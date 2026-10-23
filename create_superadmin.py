"""Birinchi superadminni yaratish (bo'sh bazada kirish uchun).

Ishlatish:
    python create_superadmin.py                       # savollar so'raladi
    python create_superadmin.py <username> <email>    # parol so'raladi
"""
import sys
from getpass import getpass

from database import Base, SessionLocal, engine
from main import get_password_hash
from models import User


def main() -> None:
    args = sys.argv[1:]
    username = args[0] if len(args) > 0 else input("Username: ").strip()
    email = args[1] if len(args) > 1 else input("Email: ").strip()
    password = getpass("Parol: ")
    if len(password) < 8:
        sys.exit("Parol kamida 8 belgidan iborat bo'lishi kerak.")

    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        if db.query(User).filter(User.role == "superadmin").first():
            sys.exit("Superadmin allaqachon mavjud.")
        if db.query(User).filter(User.username == username).first():
            sys.exit("Bu username band.")
        db.add(User(username=username, email=email,
                    hashed_password=get_password_hash(password),
                    role="superadmin", is_active=True))
        db.commit()
        print(f"Superadmin '{username}' yaratildi.")
    finally:
        db.close()


if __name__ == "__main__":
    main()
