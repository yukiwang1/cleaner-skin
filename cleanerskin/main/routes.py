from flask import render_template, request, Blueprint, flash, redirect, url_for
from flask_login import login_required, current_user
from cleanerskin import db
from cleanerskin.models import Product, BadIngredients, User, user_favorite_products
from cleanerskin.main.forms import SearchForm
from cleanerskin.main.utils import (
    query_user_or_product,
    review_product,
    get_ingredients,
    get_risk,
    search,
)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_
from flask_paginate import Pagination, get_page_args

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
@main.route("/home", methods=["GET", "POST"])
def home():
    form = SearchForm()
    if request.method == "POST" and form.validate_on_submit():

        if form.content.data:
            return redirect((url_for("main.search_results", query=form.content.data)))

        if form.ingredient_content.data:
            query = form.ingredient_content.data.replace("/", " ")
            return redirect((url_for("main.ingredients", query=query)))

        flash("Please fill in one of the search fields")
    return render_template("home.html", form=form)


# Pagination
def get_results(offset=0, per_page=10, results=[]):
    return results[offset : offset + per_page]


@main.route("/search_results/<query>", methods=["GET", "POST"])
def search_results(query):
    page, per_page, offset = get_page_args(
        page_parameter="page", per_page_parameter="per_page"
    )
    results = search(query)
    pagination_results = get_results(offset=offset, per_page=per_page, results=results)
    pagination = Pagination(
        page=page, per_page=per_page, total=len(results), css_framework="bootstrap5"
    )

    if not results:
        flash("No results found!")
        return redirect(url_for("main.home"))
    else:
        return render_template(
            "search_results.html",
            products=pagination_results,
            page=page,
            per_page=per_page,
            pagination=pagination,
        )


@main.route("/search_results", methods=["GET", "POST"])
def search_results_navbar():
    results = []
    search_phrase = request.form.items()
    query = ""

    for key, value in search_phrase:
        query = value

    return redirect((url_for("main.search_results", query=query)))


@main.route("/product/<int:product_id>")
def product(product_id):
    product = Product.query.get_or_404(product_id)
    ingredients = get_ingredients(product.ingredients)
    bad_ingredients = review_product(ingredients)
    count_risky_ingr = len(bad_ingredients)
    already_favorited_product = False
    sorted_bad_ingredients = {
        key: bad_ingredients[key]
        for key in sorted(bad_ingredients.keys(), reverse=True)
    }
    risk = get_risk(sorted_bad_ingredients)

    if current_user.is_authenticated:
        already_favorited_product = check_favorited_status(product_id)

    return render_template(
        "product.html",
        already_favorited_product=already_favorited_product,
        product=product,
        ingredients=ingredients,
        bad_ingredients=sorted_bad_ingredients,
        count=count_risky_ingr,
        risk=risk,
    )


@main.route("/ingredients/<query>")
def ingredients(query):
    ingredients = get_ingredients(query)
    bad_ingredients = review_product(ingredients)
    count_risky_ingr = len(bad_ingredients)
    risk = get_risk(bad_ingredients)

    return render_template(
        "ingredient_review.html",
        ingredients=ingredients,
        bad_ingredients=bad_ingredients,
        count=count_risky_ingr,
        risk=risk,
    )


@main.route("/product/favorite/<int:product_id>", methods=["GET", "POST"])
@login_required
def favorite_product(product_id):
    user = query_user_or_product("user", current_user.id)
    product = query_user_or_product("product", product_id)
    ingredients = get_ingredients(product.ingredients)
    bad_ingredients = review_product(ingredients)
    count_risky_ingr = len(bad_ingredients)
    risk = get_risk(bad_ingredients)

    already_favorited_product = check_favorited_status(product_id)

    if already_favorited_product:
        db.session.query(user_favorite_products).filter(
            and_(user_favorite_products.c.user_id == user.id),
            (user_favorite_products.c.product_id == product.id),
        ).delete()
        db.session.commit()
    else:
        user.favorites.append(product)
        product.favorite_count += 1
        db.session.commit()

    return render_template(
        "product.html",
        already_favorited_product=check_favorited_status(product_id),
        product=product,
        ingredients=ingredients,
        bad_ingredients=bad_ingredients,
        count=count_risky_ingr,
        risk=risk,
    )


def check_favorited_status(product_id):
    user = query_user_or_product("user", current_user.id)
    product = query_user_or_product("product", product_id)
    already_favorited_product = (
        User.query.join(user_favorite_products)
        .join(Product)
        .filter(
            and_(
                (user_favorite_products.c.user_id == user.id),
                (user_favorite_products.c.product_id == product.id),
            )
        )
        .first()
    )

    if already_favorited_product:
        return True
    else:
        return False


@main.route("/<int:user_id>/favorites")
@login_required
def favorites(user_id):
    user = query_user_or_product("user", current_user.id)
    return render_template("favorites.html", products=user.favorites)


@main.route("/brand/<brand>")
def brand(brand):
    dbQuery = db.engine.execute(
        "select * from Product where brand ilike %s", ("%" + brand + "%")
    )
    products = dbQuery.all()

    page, per_page, offset = get_page_args(
        page_parameter="page", per_page_parameter="per_page"
    )
    pagination_results = get_results(offset=offset, per_page=per_page, results=products)
    pagination = Pagination(
        page=page, per_page=per_page, total=len(products), css_framework="bootstrap5"
    )

    return render_template(
        "brand.html",
        brand=brand,
        products=pagination_results,
        page=page,
        per_page=per_page,
        pagination=pagination,
    )


@main.route("/category/<category>")
def category(category):
    dbQuery = db.engine.execute(
        "select * from Product where category ilike %s", ("%" + category + "%")
    )
    products = dbQuery.all()

    page, per_page, offset = get_page_args(
        page_parameter="page", per_page_parameter="per_page"
    )
    pagination_results = get_results(offset=offset, per_page=per_page, results=products)
    pagination = Pagination(
        page=page, per_page=per_page, total=len(products), css_framework="bootstrap5"
    )

    return render_template(
        "category.html",
        category=category,
        products=pagination_results,
        page=page,
        per_page=per_page,
        pagination=pagination,
    )


@main.route("/about")
def about():
    return render_template("about.html", title="About")
