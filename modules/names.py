"""
Action, enemy and scenery type and arg names

Type names taken from a hex editor analysis of the Platypus II exe
Arg names are a mix between the above source and unofficial names based on their functionality
"""

# (action name, args)
ACTIONS = [
    ("none", []),
    ("wait", []),  # no _f specified?
    ("minplayers", ["players"]),  # _fp2player_numactive
    ("maxplayers", ["players"]),  # _fp2player_numactive
    ("endarea", []),  # _fp2level_evaluate
    ("endlevel", []),  # _fp2level_evaluate
    ("restart", []),
    ("sky", ["y", "dy"]),  # _fp2sky_set
    ("water", ["type"]),  # _fp2water_enable
    ("lava", ["type"]),  # _fp2water_enable
    ("wateryellow", ["type"]),  # _fp2water_enable
    ("snow", ["intensity"]),  # _fp2snow_enable
    ("soot", ["intensity"]),  # _fp2snow_enable
    ("rain", ["intensity"]),  # _fp2snow_enable
    ("planet", ["img", "xpos", "y", "dy"]),  # _fp2planet_create
    ("layerblock", ["layername"]),  # _fp2layer_block
    ("layerunblock", ["layername"]),  # _fp2layer_unblock
    ("layerrange", ["layername", "lowimg", "highimg"]),  # _fp2layer_setrange
    ("layercue", ["layername", "img"]),  # _fp2layer_create
    ("layerwait", []),  # _fp2layer_ready
    ("layerreset", []),  # _fp2layer_block
    ("wave", ["enemytype", "wavetype", "y", "star"]),  # _fp2wave_create
    ("enemy", ["enemytype"]),  # _fp2enemy_create
    ("scenery", ["scenerytype"]),  # _fp2scenery_block
    ("coins", []),  # _fp2pickup_create
    ("x2", []),  # _fp2pickup_create
    ("pods", []),  # _fp2pickup_create
    ("shield", []),  # _fp2pickup_create
    ("life", []),  # _fp2pickup_create
    ("lightning", [])  # _fp2pickup_create
]

# (enemy name, args)
ENEMIES = [
    ("none", []),
    ("bullet", ["xpos", "ypos", "angle", "speed"]),
    ("flame", ["xpos", "ypos", "angle", "speed"]),
    ("missile", ["xpos", "ypos", "angle", "speed"]),
    ("laser", ["xpos", "ypos", "angle", "speed"]),
    ("orb", ["xpos", "ypos", "angle", "speed"]),
    ("glob", ["xpos", "ypos", "angle", "speed"]),
    ("bomb", ["xpos", "ypos", "angle", "speed"]),
    ("bombfrag", ["xpos", "ypos", "angle", "speed"]),
    ("mine", []),
    ("rock", ["xpos", "ypos"]),
    ("arch", []),
    ("pylon", []),
    ("telegraph", []),
    ("lava", []),
    ("buoy", []),
    ("dish", []),
    ("building", []),
    ("tank", []),
    ("wallgun", ["xoffset", "yoffset"]),
    ("icbm", ["ypos"]),
    ("domeship", []),
    ("domeship2", []),
    ("saucer", []),
    ("saucer2", []),
    ("saucerred", []),
    ("zipper", []),
    ("fish", []),
    ("fishred", []),
    ("homingfish", []),
    ("horseshoe", []),
    ("jumper", []),
    ("ray", []),
    ("v2ray", []),
    ("goldfish", []),
    ("hovergun", []),
    ("hoverlauncher", []),
    ("flipplane", []),
    ("flipplaneorange", []),
    ("bomber", []),
    ("lasersquid", []),
    ("gunsquid", []),
    ("lightningsquid", []),
    ("bombsquid", []),
    ("yellowie", []),
    ("greenie", []),
    ("reddie", []),
    ("gunship", []),
    ("lasership", []),
    ("flameship", []),
    ("homingship", []),
    ("car", []),
    ("gunboat", []),
    ("missileboat", []),
    ("flameboat", []),
    ("boss1", []),
    ("boss2", []),
    ("boss2seg", []),
    ("boss2flyby", []),
    ("boss2segflyby", []),
    ("boss3", []),
    ("boss3base", []),
    ("boss4", []),
    ("boss5", []),
    ("boss5seg", []),
    ("boss5enter", []),
    ("boss6", []),
    ("boss6base", []),
    ("boss6arm", []),
    ("boss6eye", []),
    ("worm", []),
    ("eyeball", []),
    ("blob", []),
    ("rollship", []),
    ("chicken", []),
    ("bug", []),
    ("tonsil", []),
    ("virus", []),
    ("spinner", []),
    ("fang", []),
    ("squid", []),
    ("podship", []),
    ("miniserpent", []),
    ("miniserpentseg", [])
]

# (scenery name, args)
SCENERY = [
    ("none", []),
    ("cloud", ["sprite", "xpos"]),
    ("wheel", []),
    ("arch", []),
    ("pylon", []),
    ("telegraph", []),
    ("buoy", ["layer"]),
    ("buoyline", []),
    ("windmill", ["layer"]),
    ("volcano", []),
    ("rock", []),
    ("waterfall", ["layer"]),
    ("splash", []),
    ("boat", []),
    ("boatfar", []),
    ("wallgun", []),
    ("building", []),
    ("tank", []),
    ("parrot", ["sprite"]),
    ("bird", []),
    ("birdred", []),
    ("birdyellow", []),
    ("icbm", ["xoffset", "yoffset", "launchwait"]),
    ("yellowie", []),
    ("yellowie2", []),
    ("greenie", []),
    ("reddie", []),
    ("roof", []),
    ("roofend", []),
    ("roofbit", []),
    ("last", []),
    ("lastbit", []),
    ("greenhead", []),
    ("mine", []),
    ("nuxship", ["xoffset", "yoffset"]),
    ("krider", []),
    ("tonsil", []),
    ("ulcer", []),
    ("eyeball", []),
    ("podship", [])
]

# Name to index dictionaries for getting type numbers from text
ACTION_INDEXES = {action[0]: i for i, action in enumerate(ACTIONS)}
ENEMY_INDEXES = {enemy[0]: i for i, enemy in enumerate(ENEMIES)}
SCENERY_INDEXES = {scenery[0]: i for i, scenery in enumerate(SCENERY)}