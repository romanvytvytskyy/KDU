from hero import Hero, Sponge

hero1 = Hero("Patrick star", 50, 1, 5, "Brain storm")
hero2 = Sponge("Sponge Bob", 50, 5, 10, 'Soap buble')

hero1.print_info()
hero2.print_info()

hero1.fight(hero2)
