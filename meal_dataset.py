import random
 
MEALS = [
    {
        "name": "Spaghetti with Marinara",
        "time": 30, "cost": "cheap",
        "ingredients": [
            "Spaghetti noodles", "Marinara sauce (jarred or homemade)",
            "Garlic", "Olive oil", "Parmesan cheese", "Salt & pepper",
        ],
    },
    {
        "name": "Chicken Veggie Stir Fry",
        "time": 30, "cost": "cheap",
        "ingredients": [
            "Chicken breast", "Mixed vegetables (broccoli, bell pepper, snap peas)",
            "Soy sauce", "Garlic", "Ginger", "Sesame oil", "Rice",
        ],
    },
    {
        "name": "Grilled Cheese with Tomato Sauce",
        "time": 5, "cost": "cheap",
        "ingredients": [
            "Bread", "Cheddar or American cheese", "Butter",
            "Marinara or tomato soup (for dipping)",
        ],
    },
    {
        "name": "Hot Ham and Cheese",
        "time": 5, "cost": "cheap",
        "ingredients": [
            "Bread or hoagie roll", "Deli ham", "Swiss or provolone cheese",
            "Butter", "Mustard (optional)",
        ],
    },
    {
        "name": "Chicken and Rice",
        "time": 30, "cost": "cheap",
        "ingredients": [
            "Chicken thighs or breast", "White or brown rice",
            "Chicken broth", "Garlic", "Onion", "Salt & pepper", "Butter",
        ],
    },
    {
        "name": "Spam and Rice with Tomato Sauce",
        "time": 5, "cost": "cheap",
        "ingredients": [
            "Spam (1 can)", "Cooked rice", "Marinara or tomato sauce",
            "Soy sauce (optional)", "Green onion (optional)",
        ],
    },
    {
        "name": "Steak and Potatoes",
        "time": 60, "cost": "expensive",
        "ingredients": [
            "Ribeye or sirloin steak", "Russet or Yukon Gold potatoes",
            "Butter", "Garlic", "Fresh rosemary or thyme",
            "Salt & pepper", "Olive oil",
        ],
    },
    {
        "name": "Fish and Chips",
        "time": 30, "cost": "medium",
        "ingredients": [
            "White fish fillets (cod or tilapia)", "Russet potatoes",
            "Flour", "Egg", "Breadcrumbs or beer batter mix",
            "Oil for frying", "Tartar sauce", "Lemon",
        ],
    },
    {
        "name": "Classic Chicken Alfredo",
        "time": 30, "cost": "medium",
        "ingredients": [
            "Fettuccine pasta", "Chicken breast", "Heavy cream",
            "Parmesan cheese", "Butter", "Garlic", "Salt & pepper",
        ],
    },
    {
        "name": "Hotdogs and Chips",
        "time": 5, "cost": "cheap",
        "ingredients": [
            "Hotdogs", "Hotdog buns", "Mustard", "Ketchup",
            "Relish (optional)", "Potato chips",
        ],
    },
    {
        "name": "Pork Chops and Mash",
        "time": 60, "cost": "expensive",
        "ingredients": [
            "Bone-in pork chops", "Russet potatoes", "Butter",
            "Milk or cream", "Garlic", "Olive oil", "Salt & pepper",
            "Fresh herbs (optional)",
        ],
    },
    {
        "name": "Chicken and Broccoli over Rice",
        "time": 30, "cost": "cheap",
        "ingredients": [
            "Chicken breast", "Broccoli florets", "White rice",
            "Soy sauce", "Garlic", "Sesame oil", "Cornstarch",
        ],
    },
    {
        "name": "Sub Sandwich",
        "time": 5, "cost": "cheap",
        "ingredients": [
            "Sub or hoagie roll", "Deli meat of choice (turkey, ham, roast beef)",
            "Cheese", "Lettuce", "Tomato", "Onion",
            "Mayo, mustard, or Italian dressing",
        ],
    },
    {
        "name": "Chicken Noodle Soup",
        "time": 30, "cost": "cheap",
        "ingredients": [
            "Chicken breast or thighs", "Egg noodles", "Carrots",
            "Celery", "Onion", "Chicken broth", "Garlic",
            "Salt, pepper & parsley",
        ],
    },
    {
        "name": "Potato Soup",
        "time": 30, "cost": "cheap",
        "ingredients": [
            "Russet potatoes", "Chicken or vegetable broth", "Onion",
            "Garlic", "Butter", "Milk or cream", "Cheddar cheese",
            "Bacon bits (optional)", "Salt & pepper",
        ],
    },
    {
        "name": "Fried Potato Hash",
        "time": 30, "cost": "cheap",
        "ingredients": [
            "Potatoes (russet or red)", "Onion", "Bell pepper",
            "Butter or oil", "Garlic powder", "Paprika", "Salt & pepper",
            "Eggs (optional, to top)",
        ],
    },
    {
        "name": "Egg Sandwich",
        "time": 5, "cost": "cheap",
        "ingredients": [
            "Eggs", "Bread or English muffin", "Cheese",
            "Butter", "Salt & pepper", "Hot sauce (optional)",
        ],
    },
    {
        "name": "Pancakes and Eggs",
        "time": 30, "cost": "cheap",
        "ingredients": [
            "Pancake mix (or flour, baking powder, sugar, salt)",
            "Eggs", "Milk", "Butter", "Maple syrup",
        ],
    },
    {
        "name": "Homemade Cheeseburgers and Fries",
        "time": 30, "cost": "medium",
        "ingredients": [
            "Ground beef (80/20)", "Burger buns", "Cheddar cheese",
            "Lettuce", "Tomato", "Onion", "Pickles",
            "Ketchup & mustard", "Frozen or fresh-cut fries",
        ],
    },
    {
        "name": "Chicken & Cheese Quesadilla",
        "time": 30, "cost": "cheap",
        "ingredients": [
            "Flour tortillas", "Cooked chicken (shredded or sliced)",
            "Shredded cheese (cheddar or Mexican blend)",
            "Butter or oil", "Salsa", "Sour cream (optional)",
        ],
    },
    {
        "name": "Tacos or Burritos",
        "time": 30, "cost": "cheap",
        "ingredients": [
            "Ground beef or chicken", "Taco shells or flour tortillas",
            "Taco seasoning", "Shredded cheese", "Lettuce",
            "Tomato", "Sour cream", "Salsa",
        ],
    },
    {
        "name": "Crockpot Creamy Ranch Chicken",
        "time": 60, "cost": "medium",
        "ingredients": [
            "Chicken breasts", "Ranch seasoning packet",
            "Cream cheese (1 block)", "Chicken broth",
            "Egg noodles or rice (to serve over)",
        ],
    },
    {
        "name": "Crockpot BBQ Chicken",
        "time": 60, "cost": "medium",
        "ingredients": [
            "Chicken breasts or thighs", "BBQ sauce",
            "Brown sugar", "Garlic powder", "Onion powder",
            "Burger buns or rice (to serve)",
        ],
    },
    {
        "name": "Grilled Chicken Breast and Veggies",
        "time": 30, "cost": "medium",
        "ingredients": [
            "Chicken breast", "Zucchini", "Bell peppers", "Red onion",
            "Olive oil", "Italian seasoning", "Garlic powder",
            "Salt & pepper", "Lemon",
        ],
    },
    {
        "name": "Pigs in a Blanket",
        "time": 30, "cost": "cheap",
        "ingredients": [
            "Mini sausages or cocktail wieners",
            "Crescent roll dough (1 can)",
            "Mustard or ketchup (for dipping)",
        ],
    },
]
 
VALID_COSTS = ("cheap", "medium", "expensive")
 
 
def suggest_meal(max_time: int, cost: str, exclude: list[str]) -> dict | None:
    """Return a random meal matching constraints, excluding already-seen meals."""
    filtered = [
        m for m in MEALS
        if m["time"] <= max_time and m["cost"] == cost and m["name"] not in exclude
    ]
    return random.choice(filtered) if filtered else None
 
 
def print_meal(meal: dict) -> None:
    """Pretty-print a meal suggestion with its ingredients."""
    print(f"\n  🍴  {meal['name']}")
    print("  " + "-" * (len(meal["name"]) + 5))
    print("  Ingredients:")
    for ingredient in meal["ingredients"]:
        print(f"    • {ingredient}")
    print()
 
 
def get_time_input() -> int:
    """Prompt the user for a valid cooking time in minutes."""
    while True:
        raw = input("How many minutes do you have to cook? ").strip()
        if raw.isdigit() and int(raw) > 0:
            return int(raw)
        print("  Please enter a positive whole number (e.g. 30).")
 
 
def get_cost_input() -> str:
    """Prompt the user for a valid budget tier."""
    options = ", ".join(VALID_COSTS)
    while True:
        raw = input(f"What's your budget? ({options}): ").strip().lower()
        if raw in VALID_COSTS:
            return raw
        print(f"  Please enter one of: {options}.")
 
 
def main() -> None:
    print("\n🍽️  Meal Suggester\n")
 
    time_limit = get_time_input()
    cost_tier  = get_cost_input()
 
    seen: list[str] = []
 
    while True:
        meal = suggest_meal(time_limit, cost_tier, exclude=seen)
 
        if not meal:
            if seen:
                print("\n  You've seen every meal that fits — no more options left!")
            else:
                print(
                    f"\n  No meals found for '{cost_tier}' budget within {time_limit} minutes.\n"
                    "  Try increasing your time or adjusting your budget."
                )
            break
 
        print_meal(meal)
        seen.append(meal["name"])
 
        answer = input("  Does this work? ([y]es / [n]o, try another / [q]uit): ").strip().lower()
        print()
 
        if answer in ("y", "yes"):
            print(f"  Great choice! Enjoy your {meal['name']}! 🎉\n")
            break
        elif answer in ("q", "quit"):
            print("  No worries — maybe order out tonight! 😄\n")
            break
        # anything else (n / no / enter) → loop and suggest another
 
 
if __name__ == "__main__":
    main()
 