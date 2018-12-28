from app import db

def find_user():
    user = db.session.execute('select * from users')
    
    return user.fetchall()