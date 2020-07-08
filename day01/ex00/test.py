from recipe import Recipe
from book import Book

livro = Book("teste")

print(livro.name)
print(livro.creation_date)
print(livro.recipes_list)

teste = Recipe("wincenty", 5, 20, ["6", "pedra", "vestido"], "starter",
               "otima refeicao")
teste2 = Recipe("outra", 5, 20, ["6", "pedra", "vestido"], "dessert",
                "otima refeicao")
teste3 = Recipe("aquivai", 5, 20, ["6", "pedra", "vestido"], "lunch",
                "otima refeicao")

livro.add_recipe(teste)
livro.add_recipe(teste2)
livro.add_recipe(teste3)


livro.get_recipe_by_name("aquivai")
livro.get_recipe_by_name("outra")
livro.get_recipe_by_name("wincenty")
print("last update: ", livro._last_update)

lista = livro.get_recipes_by_types("lunch")
for name in lista:
    print(lista)
lista = livro.get_recipes_by_types("dessert")
for name in lista:
    print(lista)
lista = livro.get_recipes_by_types("starter")
for name in lista:
    print(lista)

notrecipe = "teste"
livro.add_recipe(notrecipe)
livro.add_recipe()
livro.get_recipes_by_types("teste")
livro.get_recipe_by_name("teste")
