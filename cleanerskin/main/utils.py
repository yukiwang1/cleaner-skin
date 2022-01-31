from cleanerskin import db
from cleanerskin.models import Product, BadIngredients, SafeIngredients, User
import re
from collections import defaultdict


def search(query):
    results = []
    product_results = []
    brand_results = []
    search_phrase = ""
    search_query = query.split(" ")
    for i in range(len(search_query)):
        keyword = search_query[i].strip()
        search_query[i] = keyword

    for keyword in search_query:
        # search brand names first
        dbQuery = db.engine.execute(
            "select * from Product where brand ilike %s", ("%" + keyword + "%")
        )
        brand_results = dbQuery.all()

        if brand_results:
            # if brand found, check brand + product name
            for result in brand_results:
                for keyword in search_query:
                    product_name = result[3].lower()
                    if keyword in product_name:
                        results.append(result)
                        break

            # if product name is found, append remaining brand results
            if results:
                for item in brand_results:
                    if item not in results:
                        results.append(item)
                return results
            elif not results:
                # append product_name results
                dbQuery = db.engine.execute(
                    "select * from Product where name ilike %s", ("%" + keyword + "%")
                )
                product_results = dbQuery.all()
                for product in product_results:
                    brand_results.append(product)
                return brand_results

        # if no brand found, search product names
        else:
            dbQuery = db.engine.execute(
                "select * from Product where name ilike %s", ("%" + keyword + "%")
            )
            product_results = dbQuery.all()
            if product_results:
                results = product_results
                break

    return results


def query_user_or_product(_type, identifier):
    user = product = None
    if _type == "user":
        user = User.query.filter_by(id=identifier).first()
    elif _type == "product":
        product = Product.query.filter_by(id=identifier).first()
    return (
        abort(404, f"This {_type} does not exist, try again")
        if (not user and not product)
        else (user or product)
    )


# gets string and returns ingredients in array
def get_ingredients(ingredient_string):
    ingredients = ingredient_string.split(", ")
    for i in range(len(ingredients)):
        current = ingredients[i].strip()
        ingredients[i] = current
    return ingredients


# returns list of bad ingredients, if any
def review_product(ingredients):
    results = defaultdict(list)
    for ingredient in ingredients:
        if len(ingredient) < 3:
            continue

        # check false positives
        false_positives = SafeIngredients.query.filter(
            SafeIngredients.names.ilike("%" + ingredient + "%")
        ).all()
        if false_positives:
            false_positives = []
            continue

        # check entire phrase
        result = BadIngredients.query.filter(
            BadIngredients.names.ilike("%" + ingredient + "%")
        ).all()

        if result:
            if results[result[0]] == "":
                results[result[0]] = ingredient
            else:
                results[result[0]].append(ingredient)
            result = []
            continue

        ingredient_keywords = re.split("/|-| ", ingredient.lower())

        for keyword in ingredient_keywords:
            keyword = keyword.replace("(", "")
            keyword = keyword.replace(")", "")
            keyword = keyword.replace("*", "")
            keyword = keyword.replace("+", "")
            keyword = re.sub("\d", "", keyword)

            if len(keyword) < 3:
                continue

            # check false positives
            false_positives = SafeIngredients.query.filter(
                SafeIngredients.names.ilike("%" + keyword + "%")
            ).all()
            if false_positives:
                false_positives = []
                break

            result = BadIngredients.query.filter(
                BadIngredients.names.ilike("%" + keyword + "%")
            ).all()

            if result:
                if results[result[0]] == "":
                    results[result[0]] = ingredient
                else:
                    results[result[0]].append(ingredient)
                result = []
                break

    return results


def get_risk(bad_ingredients):
    risk = "Low"
    if len(bad_ingredients) == 0:
        return "None found"
    else:
        for ingredient in bad_ingredients:
            if ingredient.risk_level == "Moderate" and risk != "High":
                risk = "Moderate"
            elif ingredient.risk_level == "High" and risk != "High":
                risk = "High"

    return risk
