from flask import Blueprint, render_template, request, redirect
from models.contact import Contact
from app import db


contacts = Blueprint("contacts", __name__)


@contacts.route("/")
def home():
    contacts = Contact.query.all() 
    return render_template("index.html", contacts=contacts)


@contacts.route("/new", methods=['POST','GET'])
def addContact():
    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']
    role = request.form['role']

    new_contact = Contact(fullname, email, phone, role)

    db.session.add(new_contact)
    db.session.commit()

    return redirect('/')


@contacts.route("/update")
def update():
    return "Update Contact"


@contacts.route("/delete")
def delete():
    return "Delete Contact"


@contacts.route("/about")
def about():
    return render_template("about.html")
