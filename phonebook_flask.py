from flask import Flask, render_template
import pg

db = pg.DB(dbname='phonebook_db')
# db.debug = True

app = Flask("phonebook")
