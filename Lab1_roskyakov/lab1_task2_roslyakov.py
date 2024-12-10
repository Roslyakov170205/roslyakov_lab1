from task_1 import Table, Tree, SocialMediaProfile  # TODO: импортируйте классы, созданные в ходе выполнения прошлого задания

if __name__ == "__main__":
    # TODO: инстанцировать все описанные классы, создав три объекта
    table = Table("дерево", 4, 1.5)
    tree = Tree("дуб", 10, 5.0)
    profile = SocialMediaProfile("user123", 100, 5)

    try:
        # TODO: вызвать метод с некорректными аргументами (resize_table)
        table.resize_table(-1)
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        # TODO: вызвать метод с некорректными аргументами (grow)
        tree.grow(-5)
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        # TODO: вызвать метод с некорректными аргументами (follow)
        profile.follow(-10)
    except ValueError as e:
        print(f"Ошибка: {e}")

