from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero('Hero_good', 1, 100, 100)
        self.enemy = Hero('Hero_enemy', 1, 50, 50)

    def test_1_correct_init(self):                                      # OK, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11    : 9%
        self.assertEqual('Hero_good', self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_2_battle_equal_user_names_raise_exception(self):           # OK, 2, OK, 4, 5, 6, 7, 8, 9, 10, 11   : 18%
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual('You cannot fight yourself', str(ex.exception))

    def test_3_battle_hero_good_with_0_health(self):                    # OK, 2, OK, OK, OK, 6, 7, 8, 9, 10, 11 : 36%
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ve.exception))

    def test_4_battle_hero_enemy_with_0_health(self):                  # OK, 2, OK, OK, OK, 6, 7, 8, 9, 10, 11 : 36%
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual('You cannot fight Hero_enemy. He needs to rest', str(ve.exception))

    def test_5_battle_test_correct_decrease_of_health(self):           # OK, 2, OK, OK, OK, OK, 7, 8, 9, 10, OK : 54%
        # testing when outcome of the battle is a draw
        self.hero.health = 50
        result = self.hero.battle(self.enemy)

        self.assertEqual(0, self.hero.health)
        self.assertEqual(-50, self.enemy.health)

        self.assertEqual('Draw', result)

    def test_6_battle_hero_wins_increase_hero_stats(self):             # OK, 2, OK, OK, OK, OK, 7, 8, OK, OK, OK : 72%
        result = self.hero.battle(self.enemy)

        self.assertEqual(2, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(105, self.hero.damage)
        self.assertEqual('You win', result)

    def test_7_battle_enemy_wins_increase_enemy_stats(self):           # OK, 2, OK, OK, OK, OK, OK, OK, OK, OK, OK : 90%
        self.hero, self.enemy = self.enemy, self.hero
        result = self.hero.battle(self.enemy)

        self.assertEqual(2, self.enemy.level)
        self.assertEqual(55, self.enemy.health)
        self.assertEqual(105, self.enemy.damage)
        self.assertEqual('You lose', result)

    def test_8_str_correct_message(self):
        self.assertEqual(
            f"Hero Hero_good: 1 lvl\n"
            f"Health: 100\n"
            f"Damage: 100\n", str(self.hero)
        )


if __name__ == '__main__':
    main()
