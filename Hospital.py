import random
import time


def print_pause(text, delay=1.0):
    """Вывод текста с задержкой для атмосферы"""
    print(text)
    time.sleep(delay)


def encounter(monster_name, damage):
    """Механика встречи с монстром"""
    print_pause(f"\nВНЕЗАПНО! Из темноты появляется {monster_name}!")

    while True:
        action = input("Что будешь делать? (1 - Бежать, 2 - Драться): ").strip()
        if action in ['1', '2']:
            break
        print("Пожалуйста, введи 1 или 2.")

    if action == '1':
        if random.choice([True, False]):
            print_pause("Тебе чудом удалось проскользнуть мимо и убежать!")
            return 0
        else:
            print_pause(f"Ты споткнулся в темноте! {monster_name} настигает тебя и наносит удар.")
            return damage
    else:
        if random.choice([True, True, False]):  # шанс успешного боя выше
            print_pause(f"Ты хватаешь кусок арматуры и яростно отбиваешься! {monster_name} отступает.")
            return 0
        else:
            print_pause(f"Твоих сил не хватило. {monster_name} жестоко ранит тебя.")
            return damage


def play_game():
    hp = 100
    print_pause("=== ПОБЕГ ИЗ ЛЕЧЕБНИЦЫ «ЧЕРНАЯ СОСНА» ===")
    print_pause("Ты просыпаешься на холодном бетонном полу. Голова раскалывается.")
    print_pause("Ты не помнишь, как здесь оказался, но инстинкт кричит только одно: БЕГИ.")
    print_pause(f"Твое здоровье: {hp} HP.\n")

    # ЛОКАЦИЯ 1
    print_pause("--- ЛОКАЦИЯ 1: ЗАБРОШЕННАЯ ПАЛАТА ---")
    hp -= encounter("Безликий медбрат", random.randint(15, 30))
    if hp <= 0:
        print_pause("Ты не смог выбраться из палаты. Монстры поглотят тебя. КОНЕЦ ИГРЫ.")
        return

    print_pause(f"\nТвое здоровье: {hp} HP.")
    print_pause("Ты выбегаешь из палаты, захлопнув за собой дверь.")

    # ЛОКАЦИЯ 2
    print_pause("\n--- ЛОКАЦИЯ 2: КРОВАВЫЙ КОРИДОР ---")
    monster = random.choice(["Кричащая тень", "Паукообразный мутант"])
    hp -= encounter(monster, random.randint(20, 35))
    if hp <= 0:
        print_pause("Твой крик растворился в темноте коридора... КОНЕЦ ИГРЫ.")
        return

    print_pause(f"\nТвое здоровье: {hp} HP.")
    print_pause("В конце коридора ты находишь тяжелую железную дверь, ведущую вниз.")

    # ЛОКАЦИЯ 3
    print_pause("\n--- ЛОКАЦИЯ 3: ПОДВАЛ ОТЧАЯНИЯ ---")
    print_pause("Перед тобой — Хранитель Подвала. Огромный и ужасный.")
    hp -= encounter("Хранитель Подвала", random.randint(35, 60))
    if hp <= 0:
        print_pause("Хранитель оказался слишком силен. Ты останешься здесь навсегда. КОНЕЦ ИГРЫ.")
        return

    print_pause(f"\nТвое здоровье: {hp} HP.")
    print_pause("Хранитель падает. Ты вырываешься наружу! Свобода!")
    print_pause("ПОЗДРАВЛЯЮ! Тебе удалось выжить и сбежать из кошмара!")


if __name__ == "__main__":
    play_game()
