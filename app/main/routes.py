from app import db
from app.auth.forms import LoginForm
from app.auth.forms import RegistrationForm
from app.main.forms import ItemForm
from app.models import User, Item
from app.main import bp
from flask import render_template, request, redirect, flash, url_for
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.urls import url_parse


@bp.route("/")
@bp.route("/index")
@login_required
def index():
    items = Item.query.filter_by(user_id=current_user.id)
    return render_template("index.html", items=items)


@bp.route("/add", methods=["POST"])
def add_item():
    form = ItemForm()
    if request.method == "POST":
        item = Item(
            name=form.name.data, description=form.description.data, user=current_user
        )
        print(form.description.data)
        db.session.add(item)
        db.session.commit()
        flash("Your Home item is now added!")
        return redirect(url_for("main.index"))


@bp.route("/update/<int:id>")
def update_route(id):
    if not id or id != 0:
        item = Item.query.get(id)
        if item:
            return render_template("update.html", item=item)


@bp.route("/update/<int:id>", methods=["POST"])
def update_item(id):
    if not id or id != 0:
        item = Item.query.get(id)
        form = ItemForm()
        if item:
            item.name = form.name.data
            item.description = form.description.data
            db.session.commit()
        return redirect(url_for("main.index"))


@bp.route("/delete/<int:id>")
def delete_item(id):
    if not id or id != 0:
        item = Item.query.get(id)
        if item:
            db.session.delete(item)
            db.session.commit()
        return redirect(url_for("main.index"))


@bp.route("/turn/<int:id>")
def turn(id):
    if not id or id != 0:
        item = Item.query.get(id)
        if item:
            item.status = not item.status
            db.session.commit()
        return redirect(url_for("main.index"))

