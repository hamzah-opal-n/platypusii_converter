# List of Actions

This page aims to document all known event actions, their numerical values and their functionality. All action names were found in the Platypus II executable using a hex editor.

(HELP WANTED - see if all of these are correct/there are any unused actions and arguments)


## wait (1)

(HELP WANTED - does not seem to do anything? But is present throughout the official level data)

### args:
(HELP WANTED - needs confirmation)


## minplayers (2)

Require a minimum number of players to allow execution of the next event (all other future events are not affected).

### args:
- **players (arg1):** number of players


## maxplayers (3)

Require a maximum number of players to allow execution of the next event (all other future events are not affected).

### args:
- **players (arg1):** number of players


## endarea (4)

Advance to the next area in the level.

### args:
None


## endlevel (5)

Ends the level.

### args:
None


## restart (6)

Restart execution from the start of the file, effectively creating an infinite loop.

### args:
None


## sky (7)

Control sky display.

### args:
- **y (arg1):** starting display point for the sky gradient. Only works once at the start of the file
- **dy (arg2):** speed that it should scroll through the sky gradient. Upon reaching the end of the valid sky range, it will scroll in the opposite direction


## water (8)

Control water display (as seen in levels 1, 2 and 4).

### args:
- **type (arg1):**
  - 0: off
  - 1: on, splash disabled
  - 2: on, splash enabled


## lava (9)

Control lava display (as seen in level 3).

### args:
- **type (arg1):**
  - 0: off
  - 1: on, splash disabled
  - 2: on, splash enabled


## wateryellow (10)

Control alien water display (as seen in level 5).

### args:
- **type (arg1):**
  - 0: off
  - 1: on, splash disabled
  - 2: on, splash enabled


## snow (11)

Control intensity of snow (as seen in level 1).

### args:
- **spawn (arg1):** intensity of the effect from 0 (off) to 100 (max?)


## soot (12)

Control intensity of soot (as seen in level 3).

### args:
- **spawn (arg1):** intensity of the effect from 0 (off) to 100 (max?)


## rain (13)

Control intensity of rain (as seen in level 2).

### args:
- **spawn (arg1):** intensity of the effect from 0 (off) to 100 (max?)


## planet (14)

Spawn a planet in the background.

### args:
- **img (arg1):** sprite number of the planet
- **x (arg2):** x-position to spawn at. If greater than 0, spawn directly on the screen at the specified position. Otherwise, spawn off-screen and slowly move from right to left (HELP WANTED - needs confirmation)
- **y (arg3):** y-position to spawn at
- **dy (arg4):** y-speed of the planet. Positive values result in downward movement, negative values result in upward movement


## layerblock (15)

Stop spawning random tiles on a specific layer.

### args:
- **layername (arg1):** layer number


## layerunblock (16)

Start spawning random tiles on a specific layer.

### args:
- **layername (arg1):** layer number


## layerrange (17)

Set the range of tiles that can be randomly spawned on a specific layer.

### args:
- **layername (arg1):** layer number
- **lowimg (arg2):** lowest tile number
- **highimg (arg3):** highest tile number


## layercue (18)

Spawn a specific tile on a specific layer, temporarily overriding random tile spawns.

### args:
- **layername (arg1):** layer number
- **img (arg2):** tile number


## layerwait (19)

(HELP WANTED - needs testing)

### args:
(HELP WANTED - needs testing)


## layerreset (20)

Resets the tile range for a specific layer to its default values.

### args:
- **layername (arg1):** layer number


## wave (21)

Spawns several enemies in a specified wave. The full list of enemy types can be seen [here](enemies.md) and the list of wave types can be seen [here](waves.md).

### args:
- **enemytype (arg1):** enemy type
- **wavetype (arg2):** wave type
- **y (arg3):** y-position to spawn at, possibly ignored for random formations (HELP WANTED - needs testing)
- **star (arg4):** weapon star to release upon destroying the entire formation (HELP WANTED - test to see if it can be used on *any* enemy formation). Values listed below:
  - **0:** no weapon star
  - **1:** shootable star that cycles between Wide, Auto, Pulse and Rockets
  - **2:** Wide
  - **3:** Auto
  - **4:** Pulse
  - **5:** Rockets
  - **6:** Lightning


## enemy (22)

Spawn an enemy object. The full list of enemy types and their corresponding arguments can be seen [here](enemies.md).

### args:
- **enemytype (arg1):** enemy type
- **arg2 - arg8:** depends on enemy type


## scenery (23)

Spawn a scenery object. The full list of scenery types and their corresponding arguments can be seen [here](scenery.md).

### args:
- **scenerytype (arg1):** scenery type
- **arg2 - arg8:** depends on scenery type


## coins (24)

Spawn a balloon crate that contains coins.

### args:
None (HELP WANTED - needs confirmation)


## x2 (25)

Spawn a balloon crate that contains a Double Points Crown.

### args:
None (HELP WANTED - needs confirmation)


## pods (26)

Spawn a balloon crate that contains Weapon Pods.

### args:
None (HELP WANTED - needs confirmation)


## shield (27)

Spawn a balloon crate that contains a shield.

### args:
None (HELP WANTED - needs confirmation)


## life (28)

Spawn a balloon crate that contains an extra life.

### args:
None (HELP WANTED - needs confirmation)


## lightning (29)

Spawn a balloon crate that contains a Lightning star.

### args:
None (HELP WANTED - needs confirmation, can the bonus be changed?)