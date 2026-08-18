import hashlib
email = "tweezyson@admin.dev"      # ganti
password = "QUZMoEmBjlmo3##"      # ganti
print("Email hash:   ", hashlib.sha256(email.lower().encode()).hexdigest())
print("Password hash:", hashlib.sha256(password.encode()).hexdigest())