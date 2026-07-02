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
| arg# | Name      | Description       |
|------|-----------|-------------------|
| `1`  | `players` | Number of players |


## maxplayers (3)

Require a maximum number of players to allow execution of the next event (all other future events are not affected).

### args:
| arg# | Name      | Description       |
|------|-----------|-------------------|
| `1`  | `players` | Number of players |


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
| arg# | Name | Description                                                                                                                                                        |
|------|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `1`  | `y`  | Starting display point for the sky gradient. <ul> <li> Only works once at the start of the file (TODO TEST) </li> </ul>                                            |
| `2`  | `dy` | Speed that it should scroll through the sky gradient. <ul> <li> Upon reaching the end of the valid sky range, it will scroll in the opposite direction </li> </ul> |


## water (8)

Control water display (as seen in levels 1, 2 and 4).

### args:
| arg# | Name   | Description                                                                                                                                                                                                                                                      |
|------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `1`  | `type` | Display type:<table> <thead> <tr> <th>Value</th> <th>Description</th> </tr> </thead> <tbody> <tr> <td>`0`</td> <td>Off</td> </tr> <tr> <td>`1`</td> <td>On, splashes disabled</td> </tr> <tr> <td>`2`</td> <td>On, splashes enabled</td> </tr> </tbody> </table> |


## lava (9)

Control lava display (as seen in level 3).

### args:
| arg# | Name   | Description                                                                                                                                                                                                                                                      |
|------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `1`  | `type` | Display type:<table> <thead> <tr> <th>Value</th> <th>Description</th> </tr> </thead> <tbody> <tr> <td>`0`</td> <td>Off</td> </tr> <tr> <td>`1`</td> <td>On, splashes disabled</td> </tr> <tr> <td>`2`</td> <td>On, splashes enabled</td> </tr> </tbody> </table> |


## wateryellow (10)

Control alien water display (as seen in level 5).

### args:
| arg# | Name   | Description                                                                                                                                                                                                                                                      |
|------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `1`  | `type` | Display type:<table> <thead> <tr> <th>Value</th> <th>Description</th> </tr> </thead> <tbody> <tr> <td>`0`</td> <td>Off</td> </tr> <tr> <td>`1`</td> <td>On, splashes disabled</td> </tr> <tr> <td>`2`</td> <td>On, splashes enabled</td> </tr> </tbody> </table> |


## snow (11)

Control intensity of snow (as seen in level 1).

### args:
| arg# | Name    | Description                                        |
|------|---------|----------------------------------------------------|
| `1`  | `spawn` | Intensity of the effect from 0 (off) to 100 (max?) |


## soot (12)

Control intensity of soot (as seen in level 3).

### args:
| arg# | Name    | Description                                        |
|------|---------|----------------------------------------------------|
| `1`  | `spawn` | Intensity of the effect from 0 (off) to 100 (max?) |


## rain (13)

Control intensity of rain (as seen in level 2).

### args:
| arg# | Name    | Description                                        |
|------|---------|----------------------------------------------------|
| `1`  | `spawn` | Intensity of the effect from 0 (off) to 100 (max?) |


## planet (14)

Spawn a planet in the background.

### args:
| arg# | Name  | Description                                                                                                                                                                                                                    |
|------|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `1`  | `img` | Sprite number.                                                                                                                                                                                                                 |
| `2`  | `x`   | Spawn x-position. <ul> <li> If greater than 0, spawn directly on the screen at the specified position </li> <li> Otherwise, spawn off-screen and slowly move from right to left (HELP WANTED - needs confirmation) </li> </ul> |
| `3`  | `y`   | Spawn y-position.                                                                                                                                                                                                              |
| `4`  | `dy`  | Set y-speed.                                                                                                                                                                                                                   |


## layerblock (15)

Stop spawning random tiles on a specific layer.

### args:
| arg# | Name        | Description   |
|------|-------------|---------------|
| `1`  | `layername` | Layer number. |


## layerunblock (16)

Start spawning random tiles on a specific layer.

### args:
| arg# | Name        | Description   |
|------|-------------|---------------|
| `1`  | `layername` | Layer number. |


## layerrange (17)

Set the range of tiles that can be randomly spawned on a specific layer. Only tile numbers 1 to 99 are considered valid. If the resulting range contains no valid tiles, the game will freeze.

### args:
| arg# | Name        | Description          |
|------|-------------|----------------------|
| `1`  | `layername` | Layer number.        |
| `2`  | `lowimg`    | Lowest tile number.  |
| `3`  | `highimg`   | Highest tile number. |


## layercue (18)

Spawn a specific tile on a specific layer, temporarily overriding random tile spawns. Only tile numbers 1 to 99 are considered valid. If the game attempts to spawn an invalid tile, nothing will happen.

### args:
| arg# | Name        | Description   |
|------|-------------|---------------|
| `1`  | `layername` | Layer number. |
| `2`  | `img`       | Tile number.  |


## layerwait (19)

(HELP WANTED - needs testing)

### args:
(HELP WANTED - needs testing)


## layerreset (20)

Resets the tile range for a specific layer to its default values.

### args:
| arg# | Name        | Description   |
|------|-------------|---------------|
| `1`  | `layername` | Layer number. |


## wave (21)

Spawns several enemies in a specified wave. The full list of enemy types can be seen [here](enemies.md) and the list of wave types can be seen [here](waves.md).

### args:
| arg# | Name        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `1`  | `enemytype` | Enemy type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `2`  | `wavetype`  | Wave type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `3`  | `y`         | Spawn y-position. <ul> <li> Not all waves use this value </li> </ul>                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `4`  | `star`      | Weapon star to release upon destroying the entire formation: <table> <thead> <tr> <th>Value</th> <th>Star</th> </tr> </thead> <tbody> <tr> <td>`0`</td> <td>None</td> </tr> <tr> <td>`1`</td> <td>Shootable star that cycles between Wide, Auto, Pulse and Rockets</td> </tr> <tr> <td>`2`</td> <td>Wide</td> </tr> <tr> <td>`3`</td> <td>Auto</td> </tr> <tr> <td>`4`</td> <td>Pulse</td> </tr> <tr> <td>`5`</td> <td>Rocket</td> </tr> <tr> <td>`6`</td> <td>Lightning</td> </tr> </tbody> </table> |


## enemy (22)

Spawn an enemy object. The full list of enemy types and their corresponding arguments can be seen [here](enemies.md).

### args:
| arg#    | Name        | Description            |
|---------|-------------|------------------------|
| `1`     | `enemytype` | Enemy type.            |
| `2`-`8` | -           | Depends on enemy type. |


## scenery (23)

Spawn a scenery object. The full list of scenery types and their corresponding arguments can be seen [here](scenery.md).

### args:
| arg#    | Name          | Description              |
|---------|---------------|--------------------------|
| `1`     | `scenerytype` | Scenery type.            |
| `2`-`8` | -             | Depends on scenery type. |


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