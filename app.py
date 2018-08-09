from math import *

stren_lvl = 99
pot_bonus = 3 + floor(99 * .1)
pray_bonus = 1.23
other_bonus = 7/6
style_bonus = 3
str_bonus = 143

eff_stren = floor((stren_lvl + pot_bonus) * pray_bonus * other_bonus) + style_bonus
base_dam = 1.3 + (eff_stren / 10) + (str_bonus / 80) + ((eff_stren * str_bonus) / 640)

max_hit = floor(base_dam)

print(max_hit)
