"""
------------------------------------------------------------------
- 객체 지향 프로그래밍 : topic3 견고한 객체 지향 프로그래밍
- chapter5 : 의존 관계 역전 원칙 (Dependency Inversion Principle)

    - 상위 모듈은 하위 모듈의 구현 내용에 의존하면 안된다, 상위 모듈과 하위 모듈 모두 추상화된 내용에 의존해야 한다.
    - 의존 관계를 없애기 위해 인터페이스 사용.
    - 상위 모듈에는 추상 클래스의 자식 클래스의 인스턴스를 사용한다는 가정 하에 그 하위 모듈을 사용하는 코드를 작성해두면 되고,
      하위 모듈은 추상 클래스의 추상 메소드들을 구현(오버라이딩)만 하면 됩니다.
"""

from abc import ABC, abstractmethod

class IWeapon(ABC):
    @abstractmethod
    def use_on(self, other_character):
        pass

class Sword(IWeapon):
    """검 클래스"""
    def __init__(self, damage):
        self.damage = damage

    def use_on(self, other_character):
        """검 사용 메소드"""
        other_character.get_damage(self.damage)

class Gun(IWeapon):
    """총 클래스"""
    def __init__(self, damage, num_rounds):
        self.damage = damage
        self.num_rounds = num_rounds

    def use_on(self, other_character):
        """검 사용 메소드"""
        other_character.get_damage(self.damage)


class GameCharacter:
    """게임 캐릭터 클래스"""
    def __init__(self, name, hp, weapon: IWeapon):
        self.name = name
        self.hp = hp
        self.weapon = weapon

    def attack(self, other_character):
        """다른 유저를 공격하는 메소드"""
        if self.hp > 0:
            self.weapon.use_on(other_character)
        else:
            print(self.name + "님은 사망해서 공격할 수 없습니다.")

    def change_weapon(self, new_weapon):
        """검을 바꾸는 메소드"""
        self.weapon = new_weapon

    def get_damage(self, damage):
        """캐릭터가 공격받았을 때 자신의 체력을 깎는 메소드"""
        if self.hp <= damage:
            self.hp = 0
            print(self.name + "님은 사망했습니다.")
        else:
            self.hp -= damage

    def __str__(self):
        """남은 체력을 문자열로 리턴하는 메소드"""
        return self.name + "님은 hp: {}이(가) 남았습니다.".format(self.hp)

# GameCharacter 에서 Sword를 사용함. (의존중)
# GameCharacter Class가 상위 모듈, Sword Class가 하위 모듈

bad_swrod  = Sword(1)
good_swrod = Sword(100)
gun = Gun(100, 10)

game_char1 = GameCharacter("홍", 100, bad_swrod)
game_char2 = GameCharacter("청", 1000, gun)

#캐릭터들 서로 공격
game_char1.attack(game_char2)
game_char1.attack(game_char2)
game_char1.attack(game_char2)
game_char2.attack(game_char1)

#캐릭터 출력
print(game_char1)
print(game_char2)