import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "menu_tenant.settings")
import django

django.setup()
from decimal import Decimal

from django_tenants.utils import schema_context

from clients.models import Client
from foods.models import SubMenu, Categories, Foods

response = [
    {
        "name": "Бар",
        "name_en": "Bar",
        "number": 1,
        "categories": [
            {
                "name": "Коктейлі",
                "name_en": "Cocktails",
                "number": 1,
                "foods": [
                    {
                        "name": "PornStar",
                        "name_en": "PornStar",
                        "description": "Сучасна класика, з яскраво вираженим смаком маракуї, та додаванням італійського просекко.",
                        "description_en": "A modern classic, with a pronounced taste of passion fruit, and the addition of Italian prosecco.",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709134642.png",
                        "weight": 140,
                        "price": Decimal("200.00"),
                    },
                    {
                        "name": "Vanilla sky",
                        "name_en": "Vanilla sky",
                        "description": "Напій має ніжну текстуру, кисло-солодкий, \u2028з відтінком груші та ванілі у смаку.",
                        "description_en": "The drink has a delicate texture, sweet and sour, with a hint of pear and vanilla in the taste.",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709134631.png",
                        "weight": 150,
                        "price": Decimal("200.00"),
                    },
                    {
                        "name": "Espresso martini",
                        "name_en": "Espresso martini",
                        "description": "Класичний коктейль, має насичений кавовий смак, готується з додаванням легендарного лікеру Kahlua.",
                        "description_en": "A classic cocktail with a rich coffee taste, prepared with the addition of the legendary Kahlua liqueur.",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709134618.png",
                        "weight": 100,
                        "price": Decimal("200.00"),
                    },
                    {
                        "name": "Purple flow G+T",
                        "name_en": "Purple flow G+T",
                        "description": "Освіжаючий, основу коктейлю становить джин у лондонському стилі з гіркотою тоніка, у поєднанні міксу бузини та блакитної матчі.",
                        "description_en": "Refreshing, the base of the cocktail is London-style gin with bitters and tonic, combined with a mix of elderberry and blue matcha.",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709134605.png",
                        "weight": 190,
                        "price": Decimal("200.00"),
                    },
                    {
                        "name": "No Whiskey Sour",
                        "name_en": "No Whiskey Sour",
                        "description": "Варіація на класику, смак кисло-солодкий, фруктовий, з ароматом трав. Готується на основі американського віскі з додаванням персикового лікеру та італійської настоянки.",
                        "description_en": "A variation on the classics, the taste is sweet and sour, fruity, with the aroma of herbs. It is prepared on the basis of American whiskey with the addition of peach liqueur and Italian tincture.",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709134568.png",
                        "weight": 105,
                        "price": Decimal("200.00"),
                    },
                    {
                        "name": "Tropical Jungle",
                        "name_en": "Tropical Jungle",
                        "description": "Міцну основу становить білий карибський ром, переважає тропічний смак з відтінком мигдалю.",
                        "description_en": "The strong base is white Caribbean rum, the tropical taste with a hint of almond prevails.",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709134556.png",
                        "weight": 125,
                        "price": Decimal("200.00"),
                    },
                    {
                        "name": "Peach Aperetivo",
                        "name_en": "Peach Aperetivo",
                        "description": "Змішаний напій з додаванням трав'яного італійського аперитиву і просеко, освіжаючий за смаком, з фруктовими та цитрусовими нотами.",
                        "description_en": "A mixed drink with the addition of herbal Italian aperitif and prosecco, refreshing in taste, with fruity and citrus notes.",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709134546.png",
                        "weight": 250,
                        "price": Decimal("200.00"),
                    },
                    {
                        "name": "Cream Soda",
                        "name_en": "Cream Soda",
                        "description": "Готується з додаванням збитих вершків, \u2028за рахунок чого має ніжну і кремову текстуру, \u2028яка надає їй гладкість і м'якість.",
                        "description_en": "It is prepared with the addition of whipped cream, due to which it has a delicate and creamy texture, which gives it smoothness and softness.",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709134527.png",
                        "weight": 180,
                        "price": Decimal("200.00"),
                    },
                    {
                        "name": "Gin Garden",
                        "name_en": "Gin Garden",
                        "description": "У смаку легкий і зі свіжістю огірка, поєднує класичний джин з квітковими нотами бузини \u2028і зеленого яблука.",
                        "description_en": "The taste is light and with the freshness of cucumber, combines classic gin with floral notes of elder and green apple.",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709134517.png",
                        "weight": 150,
                        "price": Decimal("200.00"),
                    },
                    {
                        "name": "Coffee Negroni",
                        "name_en": "Coffee Negroni",
                        "description": "Автентична класика з додаванням італійського бітера витриманим на кавових зернах. \u2028Має насичений профіль аромату та смаку, з кавовими та цитрусовими нотками у післясмаку.",
                        "description_en": "An authentic classic with the addition of Italian bitter aged on coffee beans. It has a rich aroma and flavor profile, with coffee and citrus notes in the aftertaste.",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709134498.png",
                        "weight": 90,
                        "price": Decimal("200.00"),
                    },
                    {
                        "name": "Blackberry Sour",
                        "name_en": "Blackberry Sour",
                        "description": "Готується на італійському червоному солодкому вермуті, з додаванням кордіалу з ожини. \u2028Поєднує в собі ягідну насолоду, \u2028з трав'яним і в'язким післясмаком.",
                        "description_en": "It is prepared on Italian red sweet vermouth, with the addition of blackberry cordial. Combines berry delight with a herbal and viscous aftertaste.",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709134479.png",
                        "weight": 105,
                        "price": Decimal("200.00"),
                    },
                    {
                        "name": "Bloody Mary",
                        "name_en": "Bloody Mary",
                        "description": 'Класичний коктейль "Bloody Mary" на сучасний лад. У приготуванні використовується Hot Bloody Mary Mix, що надає напою неповторну і багатогранну палітру смаку.',
                        "description_en": 'Classic cocktail "Bloody Mary" in a modern way. Hot Bloody Mary Mix is used in the preparation, which gives the drink a unique and multifaceted taste palette.',
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709134469.png",
                        "weight": 200,
                        "price": Decimal("200.00"),
                    },
                ],
            },
            {
                "name": "Віскі",
                "name_en": "Whiskey",
                "number": 2,
                "foods": [
                    {
                        "name": "Jameson",
                        "name_en": "Jameson",
                        "description": "Традиційного ірландського віскі",
                        "description_en": "Traditional Irish whiskey",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709377755.png",
                        "weight": 40,
                        "price": Decimal("120.00"),
                    },
                    {
                        "name": "Four Roses",
                        "name_en": "Four Roses",
                        "description": "Бурбон",
                        "description_en": "Bourbon",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709378212.png",
                        "weight": 40,
                        "price": Decimal("120.00"),
                    },
                ],
            },
            {
                "name": "Джин",
                "name_en": "Gin",
                "number": 3,
                "foods": [
                    {
                        "name": "Mr Higgins",
                        "name_en": "Mr Higgins",
                        "description": "джин",
                        "description_en": "gin",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709378602.png",
                        "weight": 40,
                        "price": Decimal("95.00"),
                    }
                ],
            },
            {
                "name": "Ром",
                "name_en": "Romm",
                "number": 4,
                "foods": [
                    {
                        "name": "Papito Blanco",
                        "name_en": "Papito Blanco",
                        "description": "Солодкий, з нотами ванілі та вишні. Післясмак тривалий, з нюансами свіжої випічки",
                        "description_en": "Sweet, with notes of vanilla and cherry. The aftertaste is long, with nuances of fresh baked goods.",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709379328.png",
                        "weight": 40,
                        "price": Decimal("95.00"),
                    }
                ],
            },
            {"name": "Горілка", "name_en": "Vodka", "number": 5, "foods": []},
            {"name": "Вино", "name_en": "Wine", "number": 6, "foods": []},
        ],
    },
    {
        "name": "Їжа",
        "name_en": "Food",
        "number": 2,
        "categories": [
            {
                "name": "Салати",
                "name_en": "Salads",
                "number": 1,
                "foods": [
                    {
                        "name": "Салат Ростбіф",
                        "name_en": "Roast beef salad",
                        "description": "",
                        "description_en": "",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709494122.png",
                        "weight": 250,
                        "price": Decimal("200.00"),
                    },
                    {
                        "name": "Салат Цезарь",
                        "name_en": "Caesar salad",
                        "description": "",
                        "description_en": "",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709494171.png",
                        "weight": 250,
                        "price": Decimal("180.00"),
                    },
                    {
                        "name": "Салат Сьомга",
                        "name_en": "Salmon salad",
                        "description": "",
                        "description_en": "",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709494206.png",
                        "weight": 250,
                        "price": Decimal("190.00"),
                    },
                ],
            }
        ],
    },
    {
        "name": "Кава",
        "name_en": "Сoffee",
        "number": 3,
        "categories": [
            {
                "name": "Кава",
                "name_en": "Coffee",
                "number": 1,
                "foods": [
                    {
                        "name": "Еспресо",
                        "name_en": "Espresso",
                        "description": "Арабіка Уганда<br>\r\nКупаж",
                        "description_en": "Arabica Uganda<br>\r\nCoupage",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709209481.png",
                        "weight": 30,
                        "price": Decimal("30.00"),
                    },
                    {
                        "name": "Американо",
                        "name_en": "Americano",
                        "description": "Кавовий напій, що містить велику кількість води.",
                        "description_en": "A coffee drink containing a large amount of water.",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709209878.png",
                        "weight": 150,
                        "price": Decimal("35.00"),
                    },
                    {
                        "name": "Капучино",
                        "name_en": "Capuchino",
                        "description": "Напій італійського походження на основі еспресо з додаванням збитого парою молока, з гармонійним балансом насиченого солодкого смаку молока та еспресо.",
                        "description_en": "A drink of Italian origin based on espresso with the addition of steamed milk, with a harmonious balance of the rich, sweet taste of milk and espresso.",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709210352.png",
                        "weight": 150,
                        "price": Decimal("45.00"),
                    },
                    {
                        "name": "Допіо",
                        "name_en": "Dopio",
                        "description": "Кавовий напій, що готується як подвійна порція еспресо за допомогою кавового фільтру або еспресо-машини.",
                        "description_en": "A coffee drink prepared as a double shot of espresso using a coffee filter or espresso machine.",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709291274.png",
                        "weight": 50,
                        "price": Decimal("40.00"),
                    },
                    {
                        "name": "Дріп кава",
                        "name_en": "Drip coffee",
                        "description": "Дріп [Colombia, Salvador, Rwanda]",
                        "description_en": "Drip [Colombia, Salvador, Rwanda]",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709292397.png",
                        "weight": 120,
                        "price": Decimal("50.00"),
                    },
                    {
                        "name": "Капуоранж",
                        "name_en": "Сapo orange",
                        "description": "Кава з додаванням апельсинового фрешу",
                        "description_en": "Coffee with added orange juice",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709293319.png",
                        "weight": 200,
                        "price": Decimal("75.00"),
                    },
                    {
                        "name": "Лате",
                        "name_en": "Latte",
                        "description": "Кавовий напій родом з Італії, що складається з молока і кави еспресо.",
                        "description_en": "A coffee drink originally from Italy, consisting of milk and espresso coffee.",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709295223.png",
                        "weight": 240,
                        "price": Decimal("60.00"),
                    },
                    {
                        "name": "Лонг блек",
                        "name_en": "Long black",
                        "description": "Кавовий напій, на основі подвійного еспресо",
                        "description_en": "A coffee drink based on double espresso",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709296065.png",
                        "weight": 90,
                        "price": Decimal("45.00"),
                    },
                    {
                        "name": "Раф",
                        "name_en": "Raf",
                        "description": "Готується шляхом додавання нагрітих парою вершків з невеликою кількістю піни в одиночну порцію еспресо.",
                        "description_en": "Prepared by adding steamed cream with a small amount of foam to a single shot of espresso.",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709296475.png",
                        "weight": 165,
                        "price": Decimal("50.00"),
                    },
                    {
                        "name": "Флет Уайт",
                        "name_en": "Flat white",
                        "description": "Кавовий напій на основі подвійного еспресо з додаванням молока",
                        "description_en": "Сoffee drink based on double espresso with added milk",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709297087.png",
                        "weight": 170,
                        "price": Decimal("50.00"),
                    },
                ],
            },
            {
                "name": "Гарячі напої",
                "name_en": "Hot drinks",
                "number": 2,
                "foods": [
                    {
                        "name": "Какао",
                        "name_en": "Сocoa",
                        "description": "Напій, до складу якого обов'язково входить какао, а також молоко (або вода) і цукор.",
                        "description_en": "A drink that must contain cocoa, as well as milk (or water) and sugar.",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709298875.png",
                        "weight": 230,
                        "price": Decimal("60.00"),
                    },
                    {
                        "name": "Матча-Лате",
                        "name_en": "Matcha Latte",
                        "description": "Різновид японського пропареного зеленого чаю, розтовченого у порошок з додаванням молока",
                        "description_en": "A type of Japanese steamed green tea, ground into a powder with the addition of milk",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709299616.png",
                        "weight": 200,
                        "price": Decimal("70.00"),
                    },
                    {
                        "name": "Чай",
                        "name_en": "Tea",
                        "description": "Чай [чорний, зелений, трав'яний, каркаде]",
                        "description_en": "Tea [black, green, herbal, karkade]",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709325729.png",
                        "weight": 500,
                        "price": Decimal("60.00"),
                    },
                    {
                        "name": "Обліпиха-Маракуйя",
                        "name_en": "Sea buckthorn-passion fruit",
                        "description": "Пюре маракуї і обліпиха, перетерті з цукром.",
                        "description_en": "Passion fruit and sea buckthorn puree, mashed with sugar.",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709325494.png",
                        "weight": 300,
                        "price": Decimal("60.00"),
                    },
                    {
                        "name": "Малина-Ожина",
                        "name_en": "Raspberry-Blackberry",
                        "description": "Створений на основі високоякісного чорного чаю з додаванням кислувато-солодкого соку журавлини та соку малини.",
                        "description_en": "Сreated on the basis of high-quality black tea with the addition of sour-sweet cranberry juice and raspberry juice.",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709326780.png",
                        "weight": 300,
                        "price": Decimal("60.00"),
                    },
                ],
            },
            {
                "name": "Не кава",
                "name_en": "No coffee",
                "number": 3,
                "foods": [
                    {
                        "name": "Фреш",
                        "name_en": "Fresh",
                        "description": "Свіжовичавлений фруктовий апельсиновий сік.",
                        "description_en": "Freshly squeezed fruit orange juice.",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709301442.png",
                        "weight": 150,
                        "price": Decimal("60.00"),
                    },
                    {
                        "name": "МилкШейк",
                        "name_en": "Milkshake",
                        "description": "Десертний напій на основі молока та морозива",
                        "description_en": "Dessert drink based on milk and ice cream",
                        "image": "7d54704a-7959-4cbd-b776-3c15599517c2/food/1709468481.png",
                        "weight": 350,
                        "price": Decimal("80.00"),
                    },
                ],
            },
        ],
    },
]

client = Client.objects.get(name="avenue89")


with schema_context(client.schema_name) as _:
    for sub_menu in response:
        categories = sub_menu.pop("categories")
        s = SubMenu.objects.create(**sub_menu)
        for category in categories:
            foods = category.pop("foods")
            c = Categories.objects.create(**category, sub_menu=s)
            for food in foods:
                Foods.objects.create(**food, categories=c)

from users.models import User

user = User.objects.get(email="suprun.sergey89@gmail.com")

user.set_password('admin')
user.save()