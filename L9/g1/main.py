from hero import Hero, Grut

hero1 = Grut("Grut", 50, 25, 5, "Stick")
hero2 = Hero("R2D2", 50, 50, 15, "Laser")


hero1.print_info()
hero2.print_info()

hero1.fight(hero2)
