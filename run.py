# imports from __init__.py. Note the app variable must exist in init.py
from cleanerskin import app

# already using Config class as default, don't need to pass in parameter
# app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
