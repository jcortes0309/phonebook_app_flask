from flask import Flask, render_template, redirect, request
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

@app.route("/new_entry/")
def add_contact():
    return render_template(
        "new_entry.html",
        title = "Add New Entry"
    )



if __name__ == '__main__':
    app.run(debug=True)
