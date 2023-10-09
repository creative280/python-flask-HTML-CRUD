from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.contact import Contact
from app import db


contacts = Blueprint("contacts", __name__)


@contacts.route("/")
def index():
    contacts = Contact.query.all()
    return render_template("index.html", contacts=contacts)


@contacts.route("/new", methods=["POST", "GET"])
def addContact():
    fullname = request.form["fullname"]
    email = request.form["email"]
    phone = request.form["phone"]
    role = request.form["role"]

    new_contact = Contact(fullname, email, phone, role)

    db.session.add(new_contact)
    db.session.commit()

    flash("Contacto Añadido Correctamente")

    return redirect(url_for("contacts.index"))


@contacts.route("/update/<id>", methods=["POST", "GET"])
def update(id):
    contact = Contact.query.get(id)
    if request.method == "POST":
        contact.fullname = request.form["fullname"]
        contact.email = request.form["email"]
        contact.phone = request.form["phone"]
        contact.role = request.form["role"]

        db.session.commit()

        flash("Contacto Actualizado Correctamente")

        return redirect(url_for("contacts.index"))

    return render_template("update.html", contact=contact)


@contacts.route("/delete/<id>")
def delete(id):
    contact = Contact.query.get(id)

    db.session.delete(contact)
    db.session.commit()

    flash("Contacto Eliminado Correctamente")

    return redirect(url_for("contacts.index"))


@contacts.route("/about")
def about():
    return render_template("about.html")
