from cleanerskin import db
from cleanerskin.models import Product, BadIngredients, SafeIngredients, User
import re
from collections import defaultdict


def search(query):
    results = []
    product_results = []
    brand_results = []
    search_query = query.split(" ")

    for i in range(len(search_query)):
        keyword = search_query[i].strip()
        search_query[i] = keyword

    for keyword in search_query:
        # Find Products with matching brand names first
        brand_results = Product.brand.ilike("%" + keyword + "%").all()

        if brand_results:
            # If brand found, move "better" matches first (i.e. brand + product name matches combined)
            for product in brand_results:
                product_name = product.name.lower()
                for keyword in search_query:
                    if keyword in product_name:
                        results.append(product)
                        brand_results.remove(product)
                        break
            results.extend(brand_results)
            return results

        # If no matching brand found, try searching by product name
        else:
            product_results = Product.name.ilike("%" + keyword + "%").all()
            results.extend(product_results)

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


# Gets string and returns ingredients in array
def get_ingredients(ingredient_string):
    ingredients = ingredient_string.split(", ")
    for i in range(len(ingredients)):
        current = ingredients[i].strip()
        ingredients[i] = current
    return ingredients


# Returns dict of bad ingredients, if any
def review_product(ingredients):
    results = defaultdict(list)
    for ingredient in ingredients:
        full_ingredient_match_category = []

        if len(ingredient) < 3:
            continue

        if has_false_positives(ingredient):
            continue

        # Check entire phrase
        full_ingredient_match_category = BadIngredients.query.filter(
            BadIngredients.names.ilike("%" + ingredient + "%")
        ).all()

        if full_ingredient_match_category:
            results[full_ingredient_match_category[0]].append(ingredient)
            continue

        ingredient_keywords = re.split("/|-| ", ingredient.lower())

        for keyword in ingredient_keywords:
            ingredient_keyword_match_category = []

            keyword = (
                keyword.replace("(", "")
                .replace(")", "")
                .replace("*", "")
                .replace("+", "")
            )
            keyword = re.sub("\d", "", keyword)

            if len(keyword) < 3:
                continue

            if has_false_positives(keyword):
                continue

            ingredient_keyword_match_category = BadIngredients.query.filter(
                BadIngredients.names.ilike("%" + keyword + "%")
            ).all()

            if ingredient_keyword_match_category:
                results[ingredient_keyword_match_category[0]].append(ingredient)
                break

    return results


# Returns true if there are false positives
def has_false_positives(keyword):
    false_positives = SafeIngredients.query.filter(
        SafeIngredients.names.ilike("%" + keyword + "%")
    ).all()

    return len(false_positives) > 0


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
