
from app import app #import from __init__ 
from app import db
    
if __name__ == '__main__':
    app.run(host='localhost', port=5000)
