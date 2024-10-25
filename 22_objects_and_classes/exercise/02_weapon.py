class Weapon:
    def __init__(self, bullets: int):
        self.bullets = bullets
        self.bullet = bullets

    def shoot(self):
        if self.bullet > 0:
            self.bullet -= 1
            return 'shooting...'
        else:
            return "no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {self.bullet}"

weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
