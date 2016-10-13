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

@app.route("/submit_new_entry", methods = ["POST"])
def submit_form():
    name = request.form.get("name")
    phone_number = request.form.get("phone_number")
    email = request.form.get("email")
    db.insert(
        'phonebook',
        name = name,
        phone_number = phone_number,
        email = email
    )
    return redirect("/")

@app.route("/update_entry", methods = ["GET"])
def update_entry():
    id = request.args.get('id')
    contact_list = db.query("select * from phonebook where id = %s;" % id).namedresult()

    return render_template(
        "update_entry.html",
        title = "Update Entry",
        contact_list = contact_list
    )
    
@app.route("/submit_update_entry", methods = ["POST"])
def submit_update_form():
    id = request.form.get("id")
    name = request.form.get("name")
    phone_number = request.form.get("phone_number")
    email = request.form.get("email")
    db.update(
        'phonebook', {
            'id': id,
            'name': name,
            'phone_number': phone_number,
            'email': email
        }
    )
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
