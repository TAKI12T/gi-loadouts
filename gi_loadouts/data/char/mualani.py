from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Mualani(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 4.8, 3: 9.6, 4: 9.6, 5: 14.4, 6: 19.2}
    __statname__: STAT = STAT.critical_rate_perc
    name: str = "Mualani"
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=14.1512, defense=44.39386, health_points=1182.1168)
    ascn: BaseStat = BaseStat(attack=58.10823, defense=182.3094, health_points=4854.4106)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.hydro
    cons_name: str = "Phoca Neomonachus"
    afln: str = "Meztli"
    head: str = "Splish-Splash Wavechaser"