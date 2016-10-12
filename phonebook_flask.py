from flask import Flask, render_template, redirect
import pg

db = pg.DB(dbname='phonebook_db')
# db.debug = True

app = Flask("phonebook")

@app.route("/")
def contacts():
    return render_template(
        "contacts.html",
        title = "Phonebook Contacts",
        contact_list = db.query("select * from phonebook").namedresult()
    )

if __name__ == '__main__':
    app.run(debug=True)
