"""
This is my main file that will run the app and
create the website needed. It is inline with the
Learning_Journal folder so that it is neat
and understandable
"""

from Learning_Journal import app, db




if __name__ == '__main__':
    """
    I create the DataBase and then run the app.
    """
    db.create_all()
    app.run(debug=True, port=8000)
