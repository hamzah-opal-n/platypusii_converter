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
    ("snow", ["spawn"]),  # _fp2snow_enable
    ("soot", ["spawn"]),  # _fp2snow_enable
    ("rain", ["spawn"]),  # _fp2snow_enable
    ("planet", ["img", "x", "y", "dy"]),  # _fp2planet_create
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
    ("bullet", ["x", "y", "a", "d"]),
    ("flame", ["x", "y", "a", "d"]),
    ("missile", ["x", "y", "a", "d"]),
    ("laser", ["x", "y", "a", "d"]),
    ("orb", ["x", "y", "a", "d"]),
    ("glob", ["x", "y", "a", "d"]),
    ("bomb", ["x", "y", "a", "d"]),
    ("bombfrag", ["x", "y", "a", "d"]),
    ("mine", ["type", "y", "x"]),
    ("rock", ["x", "y"]),
    ("arch", []),
    ("pylon", []),
    ("telegraph", []),
    ("lava", []),
    ("buoy", []),
    ("dish", []),
    ("building", ["layerx", "layery"]),
    ("tank", ["layerx", "layery"]),
    ("wallgun", ["layerx", "layery"]),
    ("icbm", ["y"]),
    ("domeship", ["y", "offsetx"]),
    ("domeship2", ["y", "offsetx"]),
    ("saucer", ["y", "offsetx"]),
    ("saucer2", ["y", "offsetx"]),
    ("saucerred", ["y", "offsetx"]),
    ("zipper", []),
    ("fish", ["y", "offsetx", "path", "turn"]),
    ("fishred", ["y", "offsetx"]),
    ("homingfish", ["y", "offsetx", "path"]),
    ("horseshoe", []),
    ("jumper", ["x", "offsety", "dx"]),
    ("ray", ["y", "offsetx", "turn"]),
    ("v2ray", ["y", "offsetx", "turn"]),
    ("goldfish", ["y", "offsetx"]),
    ("hovergun", ["x", "endy"]),
    ("hoverlauncher", ["x", "endy"]),
    ("flipplane", ["y"]),
    ("flipplaneorange", ["y"]),
    ("bomber", ["y"]),
    ("lasersquid", ["y"]),
    ("gunsquid", ["y"]),
    ("lightningsquid", ["y"]),
    ("bombsquid", ["y"]),
    ("yellowie", ["y"]),
    ("greenie", ["y"]),
    ("reddie", ["y"]),
    ("gunship", ["y"]),
    ("lasership", ["y"]),
    ("flameship", ["y"]),
    ("homingship", ["y"]),
    ("car", ["type", "special"]),
    ("gunboat", ["path"]),
    ("missileboat", ["path"]),
    ("flameboat", ["path"]),
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
    ("worm", ["y"]),
    ("eyeball", ["y"]),
    ("blob", ["y"]),
    ("rollship", []),
    ("chicken", []),
    ("bug", []),
    ("tonsil", []),
    ("virus", ["y", "offsetx", "path"]),
    ("spinner", []),
    ("fang", ["type"]),
    ("squid", []),
    ("podship", ["y"]),
    ("miniserpent", []),
    ("miniserpentseg", [])
]

# (scenery name, args)
SCENERY = [
    ("none", []),
    ("cloud", ["img", "x"]),
    ("wheel", []),
    ("arch", ["sololayer"]),
    ("pylon", ["sololayer"]),
    ("telegraph", ["sololayer"]),
    ("buoy", ["img"]),
    ("buoyline", []),
    ("windmill", ["img"]),
    ("volcano", []),
    ("rock", ["img", "x"]),
    ("waterfall", ["type"]),
    ("splash", []),
    ("boat", []),
    ("boatfar", []),
    ("wallgun", []),
    ("building", []),
    ("tank", []),
    ("parrot", ["img"]),
    ("bird", []),
    ("birdred", []),
    ("birdyellow", []),
    ("icbm", ["layerx", "layery", "time"]),
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
    ("mine", ["img"]),
    ("nuxship", ["layerx", "layery"]),
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