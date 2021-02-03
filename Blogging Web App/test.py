from flask_bcrypt import Bcrypt

bcrypt=Bcrypt()
hashed_pw=bcrypt.generate_password_hash('testing').decode('utf-8')

# $2b$12$30Wjxrzoj.SilAPDc7XQ6e2kNnvnkI5aSMWb0Vd1zRrfSbREvM1vq

print(bcrypt.check_password_hash(hashed_pw,'testing'))