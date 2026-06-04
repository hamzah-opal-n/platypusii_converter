# List of Actions

This page aims to document all known event actions, their numerical values and their functionality. All action names have been chosen to best reflect their functionality in the context of Platypus II.

(HELP WANTED - see if all of these are correct/there are any unused actions and arguments)


## waitUntilNoEnemies (1)

Wait until no enemies remain on screen before executing subsequent events. (HELP WANTED - needs confirmation)

### args:
None (HELP WANTED - needs confirmation)


## requirePlayers (2)

Require a minimum number of players to allow execution of the next event (all other future events are not affected).

### args:
- **minPlayers (arg1):** the minimum number of players required for the next event to be executed


## unknownAction3 (3)

Unused during normal gameplay.

### args:
(HELP WANTED - needs testing)


## goToNextArea (4)

Advance to the next area in the level.

### args:
None (HELP WANTED - needs confirmation)


## unknownAction5 (5)

Unused during normal gameplay.

### args:
(HELP WANTED - needs testing)


## loopCodeFromZero (6)

Restart execution from the start of the file.

### args:
None (HELP WANTED - needs confirmation)


## skyGradient (7)

Control sky display.

### args:
- **startPoint (arg1):** starting display point for the sky gradient
- **scrollSpeed (arg2):** speed that it should scroll through the sky gradient


## waterNormal (8)

Control water display (as seen in levels 1, 2 and 4).

### args:
- **type (arg1):**
  - 0: off
  - 1: on, splash disabled
  - 2: on, splash enabled


## waterLava (9)

Control lava display (as seen in level 3).

### args:
- **type (arg1):**
  - 0: off
  - 1: on, splash disabled
  - 2: on, splash enabled


## waterAlien (10)

Control alien water display (as seen in level 5).

### args:
- **type (arg1):**
  - 0: off
  - 1: on, splash disabled
  - 2: on, splash enabled


## snowNormal (11)

Control intensity of snowfall (as seen in level 1).

### args:
- **intensity (arg1):** intensity of the effect from 0 (off) to 100 (max)


## snowAsh (12)

Control intensity of ashfall (as seen in level 3).

### args:
- **intensity (arg1):** intensity of the effect from 0 (off) to 100 (max)


## snowRain (13)

Control intensity of rainfall (as seen in level 2).

### args:
- **intensity (arg1):** intensity of the effect from 0 (off) to 100 (max)


## spawnPlanet (14)

Spawn a planet in the background.

### args:
- **sprite (arg1):** sprite number of the planet
- **xPos (arg2):** x-position to spawn at. If greater than 0, spawn directly on the screen at the specified position. Otherwise, spawn off-screen and slowly move from right to left (HELP WANTED - needs confirmation)
- **yPos (arg3):** y-position to spawn at
- **ySpeed (arg4):** y-speed of the planet. Positive values result in downward movement, negative values result in upward movement


## setRandomTilesForeground (15)

TODO

### args:
TODO


## waitForHillPop (16)

TODO

### args:
TODO


## setRandomTilesBackground (17)

TODO

### args:
TODO


## forceTile (18)

Force display of a specific tile on a specific layer.

### args:
- **layer (arg1):** layer number
- **tile (arg2):** tile number


## unknownAction19 (19)

(HELP WANTED - needs testing)

### args:
(HELP WANTED - needs testing)


## unknownAction20 (20)

(HELP WANTED - needs testing)

### args:
(HELP WANTED - needs testing)


## spawnFormation (21)

TODO

### args:
- **object (arg1):** enemy type
- TODO


## spawnEnemy (22)

Spawn an enemy object. The full list of enemy types and their corresponding arguments can be seen [here](enemies.md).

### args:
- **object (arg1):** enemy type
- **arg2 - arg8:** depends on enemy type


## spawnScenery (23)

Spawn a scenery object. The full list of scenery types and their corresponding arguments can be seen [here](scenery.md).

### args:
- **object (arg1):** scenery type
- **arg2 - arg8:** depends on scenery type


## balloonCrateCoins (24)

Spawn a balloon crate that contains coins.

### args:
None (HELP WANTED - needs confirmation)


## balloonCrateDoublePoints (25)

Spawn a balloon crate that contains a Double Points Crown.

### args:
None (HELP WANTED - needs confirmation)


## balloonCrateWeaponPods (26)

Spawn a balloon crate that contains Weapon Pods.

### args:
None (HELP WANTED - needs confirmation)


## balloonCrateShield (27)

Spawn a balloon crate that contains a shield.

### args:
None (HELP WANTED - needs confirmation)


## balloonCrateExtraLife (28)

Spawn a balloon crate that contains an extra life.

### args:
None (HELP WANTED - needs confirmation)


## balloonCrateLightningStar (29)

Spawn a balloon crate that contains a Lightning star.

### args:
None (HELP WANTED - needs confirmation)