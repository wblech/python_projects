from pyrecipe import Recipe
from book import Book

livro = Book("teste")

# print(livro.name)
# print(livro.creation_date)
# print(livro.recipes_list)

teste = Recipe("wincenty", 5, 20, ["6", "pedra", "vestido"], "dessert",
               "otima refeicao")
teste2 = Recipe("outra", 5, 20, ["6", "pedra", "vestido"], "dessert",
                "otima refeicao")
teste3 = Recipe("aquivai", 5, 20, ["6", "pedra", "vestido"], "lunch",
                "otima refeicao")

livro.add_recipe(teste)
livro.add_recipe(teste2)
livro.add_recipe(teste3)

# print(livro.recipes_list)
# print(livro.recipes_list["dessert"])

livro.get_recipe_by_name("aquivai2")
# livro.get_recipe_by_name("outra")
# print(livro._last_update)

livro.get_recipes_by_types("lunch")
