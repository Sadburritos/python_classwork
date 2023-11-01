import hashlib
import itertools
import string
import time

target_hash = 'ebec4c0d4133e6ea7d83f7137cefa6a5'

characters = string.ascii_letters + string.digits + "~!@#$%^&*()_+-="

password_length = 4

start_time = time.time()

for password in itertools.product(characters, repeat=password_length):
    password_str = ''.join(password)
    md5_hash = hashlib.md5(password_str.encode()).hexdigest()
    if md5_hash == target_hash:
        print(f"Пароль найден: {password_str}")
        break

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Время выполнения: {elapsed_time} секунд")
