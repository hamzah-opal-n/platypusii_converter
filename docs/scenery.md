# Scenery

This page aims to document all known scenery types, their numerical values and their functionality. All scenery names were found in the Platypus II executable using a hex editor.

Scenery type numbers are used in scenery (action 23) as arg1.

(HELP WANTED - see if all of these are correct/there are any unused scenery objects and arguments)


## cloud (1)
![cloud](images/scenery/cloud.png)

Cloud that moves from right to left.

### args:
| arg# | Name  | Description                                                                                                                                                                    |
|------|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `2`  | `img` | Sprite number. <ul> <li>A value of 0 will cause the scenery to use a random sprite</li> </ul>                                                                                  |
| `3`  | `x`   | Spawn x-position. <ul> <li>A value of 0 will cause the scenery to spawn just off-screen on the right</li> </ul>                                                                |
| `4`  | `y`   | Spawn y-position. <ul> <li>A value of 0 will cause the scenery to spawn at a random y-position (range TBD, TODO)</li> </ul>                                                    |
| `5`  | `d`   | Speed. <ul> <li>A value of 0 will cause the scenery to move with a random speed (range TBD, TODO)</li> <li>Negative values will cause the scenery to move backwards</li> </ul> |


## wheel (2)
![wheel](images/scenery/wheel.png)

Unused during normal gameplay.

### args:
(HELP WANTED - needs testing)


## arch (3)
![arch](images/scenery/arch.png)

Red arch-shaped structure constructed out of sections on different layers. The top section on layer 1 damages the player upon contact, but the player can safely fly below or above it.

### args:
- **sololayer (arg2):** layer to isolate. Set to 0 to display all layers, layer 0 cannot be isolated


## pylon (4)
![pylon](images/scenery/pylon.png)

A whole row of power lines on the classic grey poles across different layers. The power lines on layer 1 damage the player upon contact.

### args:
- **sololayer (arg2):** layer to isolate. Set to 0 to display all layers, layer 1 cannot be isolated


## telegraph (5)
![telegraph](images/scenery/telegraph.png)

A whole row of power lines on brown poles across different layers. The power lines on layer 1 damage the player upon contact.

### args:
- **sololayer (arg2):** layer to isolate. Set to 0 to display all layers, layer 1 cannot be isolated


## buoy (6)
![buoy](images/scenery/buoy.png)

A single buoy. The sprite numbers match the layers they spawn on.

### args:
| arg# | Name  | Description    |
|------|-------|----------------|
| `2`  | `img` | Sprite number. |


## buoyline (7)
![buoyline](images/scenery/buoyline.png)

A whole row of buoys that appear across different background layers.

### args:
None


## windmill (8)
![windmill](images/scenery/windmill.png)

TODO. The sprite numbers match the layers they spawn on.

### args:
- **img (arg2):** layer to spawn on (HELP WANTED - needs testing, find where the graphics for the spinning blades are located)


## volcano (9)
![volcano](images/scenery/volcano.png)

TODO

### args:
None (HELP WANTED - needs testing)


## rock (10)
![rock](images/scenery/rock.png)

Falling rock that is usually seen during volcanic eruptions. Disappears and shows a splash animation once it hits the water.

### args:
- **img (arg2):** layer to spawn on. There are no rock sprites for layers 1 and 2, but the corresponding splash will display anyway
- **x (arg3):** x-position to spawn at


## waterfall (11)
![waterfall](images/scenery/waterfall.png)

Flowing waterfall. Spawns an instance of tile number 54 below it on the chosen layer. If this tile does not exist, the scenery will spawn out of thin air in the middle of the screen.

### args: 
| arg# | Name        | Description                                                                                                      |
|------|-------------|------------------------------------------------------------------------------------------------------------------|
| `2`  | `layername` | Layer number. <ul> <li>Sprite number 1 is used on layer 3</li> <li>Sprite number 2 is used on layer 1</li> </ul> |


## splash (12)
![splash](images/scenery/splash.png)

Unused during normal gameplay.

### args:
(HELP WANTED - needs testing)


## boat (13)
![boat](images/scenery/boat.png)

Boat that moves from right to left in the near background.

### args:
| arg# | Name  | Description                                                                                   |
|------|-------|-----------------------------------------------------------------------------------------------|
| `2`  | `img` | Sprite number. <ul> <li>A value of 0 will cause the scenery to use a random sprite</li> </ul> |


## boatfar (14)
![boatfar](images/scenery/boatfar.png)

Boat that moves from right to left in the far background.

### args:
| arg# | Name  | Description                                                                                   |
|------|-------|-----------------------------------------------------------------------------------------------|
| `2`  | `img` | Sprite number. <ul> <li>A value of 0 will cause the scenery to use a random sprite</li> </ul> |


## wallgun (15)
![wallgun](images/scenery/wallgun.png)

Ruined base panel left behind after destroying a wallgun enemy (enemy type 19). Spawns on layer 1.

### args:
| arg# | Name     | Description                       |
|------|----------|-----------------------------------|
| `2`  | `layerx` | Spawn x-position, based on tiles. |
| `3`  | `y`      | Spawn y-position.                 |


## building (16)
![building](images/scenery/building.png)

Destructible building that spawns at the bottom of the screen and leaves behind a base. The destructible portion damages the player on contact and can be spawned on its own using [enemy type 17](enemies.md#building-17).

### args:
None


## tank (17)
![tank](images/scenery/tank.png)

Destructible tank that spawns at the bottom of the screen and leaves behind a base. The destructible portion damages the player on contact and can be spawned on its own using [enemy type 18](enemies.md#tank-18).

### args:
None


## parrot (18)
![parrot](images/scenery/parrot.png)

Green parrot that flies from right to left at a slight upward angle. Sprite/layer can be customised. Spawns at a random y-position.

### args:
- **img (arg2):** sprite number to use (HELP WANTED - needs testing)


## bird (19)
![bird](images/scenery/bird.png)

Distant blue bird that flies along a random path.

### args:
None (HELP WANTED - needs testing)


## birdred (20)
![birdred](images/scenery/birdred.png)

Distant red bird that flies along a random path.

### args:
None (HELP WANTED - needs testing)


## birdyellow (21)
![birdyellow](images/scenery/birdyellow.png)

Distant yellow bird that flies along a random path.

### args:
None (HELP WANTED - needs testing)


## icbm (22)
![icbm](images/scenery/icbm.png)

Large missile that launches upwards sometime after spawning. Spawns on layer 5.

### args:
| arg# | Name     | Description                         |
|------|----------|-------------------------------------|
| `2`  | `layerx` | Spawn x-position, based on tiles.   |
| `3`  | `layery` | Spawn y-position, based on tiles    |
| `4`  | `time`   | Time? (TODO TEST) before launching. |


## yellowie (23)
![yellowie](images/scenery/yellowie.png)

Distant yellowie that flies from left to right.

### args:
| arg# | Name   | Description                                                                                                    |
|------|--------|----------------------------------------------------------------------------------------------------------------|
| `2`  | `y`    | Spawn y-position. <ul> <li>A value of 0 will cause the scenery to be spawned at a random y-position</li> </ul> |


## yellowie2 (24)
![yellowie2](images/scenery/yellowie2.png)

Distant yellowie variant with a grey-ish hue that flies from left to right.

### args:
| arg# | Name   | Description                                                                                                    |
|------|--------|----------------------------------------------------------------------------------------------------------------|
| `2`  | `y`    | Spawn y-position. <ul> <li>A value of 0 will cause the scenery to be spawned at a random y-position</li> </ul> |


## greenie (25)
![greenie](images/scenery/greenie.png)

Distant greenie that flies from left to right.

### args:
| arg# | Name   | Description                                                                                                    |
|------|--------|----------------------------------------------------------------------------------------------------------------|
| `2`  | `y`    | Spawn y-position. <ul> <li>A value of 0 will cause the scenery to be spawned at a random y-position</li> </ul> |


## reddie (26)
![reddie](images/scenery/reddie.png)

Distant reddie that flies from left to right.

### args:
| arg# | Name   | Description                                                                                                    |
|------|--------|----------------------------------------------------------------------------------------------------------------|
| `2`  | `y`    | Spawn y-position. <ul> <li>A value of 0 will cause the scenery to be spawned at a random y-position</li> </ul> |


## roof (27)
![roof](images/scenery/roof.png)

Begin spawning the cave roof tiles seen in level 3. On each layer, spawn a single instance of tile number 1 before randomly spawning tiles from number 2 to 4. Strange things happen when more than one spawner is active simultaneously.

### args:
None


## roofend (28)
![roofend](images/scenery/roofend.png)

Finish spawning the cave roof tiles seen in level 3. On each layer, spawn a single instance of tile number 5 before stopping random tile spawns.

### args:
None


## roofbit (29)
![roofbit](images/scenery/roofbit.png)

Spawn a cave roof tile.

### args:
| arg# | Name        | Description   |
|------|-------------|---------------|
| `2`  | `layername` | Layer number. |
| `3`  | `img`       | Tile number.  |


## last (30)
![last](images/scenery/last.png)

Begin spawning the alien mouth roof tiles seen in level 5.  On each layer, spawn a single instance of tile number 1 before randomly spawning tiles from number 2 to 4 (HELP WANTED - needs testing to see if additional tiles can be added, and what happens if two last_start actions are called).

### args:
None


## lastbit (31)
![lastbit](images/scenery/lastbit.png)

Spawn an alien mouth roof tile.

### args:
| arg# | Name        | Description   |
|------|-------------|---------------|
| `2`  | `layername` | Layer number. |
| `3`  | `img`       | Tile number.  |


## greenhead (32)
![greenhead](images/scenery/greenhead.png)

Cameo appearance of Silthax, the main antagonist of NUX. Briefly pops up from the bottom of the screen before retreating.

### args:
None (HELP WANTED - needs testing)


## mine (33)
![mine](images/scenery/mine.png)

Distant mine that spawns at a random y-position with random speed.

### args:
| arg# | Name  | Description                                                                                   |
|------|-------|-----------------------------------------------------------------------------------------------|
| `2`  | `img` | Sprite number. <ul> <li>A value of 0 will cause the scenery to use a random sprite</li> </ul> |


## nuxship (34)
![nuxship](images/scenery/nuxship.png)

NUX's ship from the game of the same name. Spawns on layer 4.

### args:
| arg# | Name     | Description                       |
|------|----------|-----------------------------------|
| `2`  | `layerx` | Spawn x-position, based on tiles. |
| `3`  | `layery` | Spawn y-position, based on tiles. |


## krider (35)
![krider](images/scenery/krider.png)

A row of red lights that illuminate in a scrolling pattern with a randomised direction. Normally spawned together with tile number 60. The sprite numbers match the layers they spawn on.

### args:
| arg# | Name     | Description                       |
|------|----------|-----------------------------------|
| `2`  | `img`    | Sprite number.                    |
| `3`  | `layerx` | Spawn x-position, based on tiles. |
| `4`  | `layery` | Spawn y-position, based on tiles. |


## tonsil (36)
![tonsil](images/scenery/tonsil.png)

Distant tonsil that spawns at a random y-position. The sprite numbers match the layers they spawn on.

### args:
| arg# | Name  | Description                                                                                   |
|------|-------|-----------------------------------------------------------------------------------------------|
| `2`  | `img` | Sprite number. <ul> <li>A value of 0 will cause the scenery to use a random sprite</li> </ul> |


## ulcer (37)
![ulcer](images/scenery/ulcer.png)

Festering ulcer that explodes when the player gets close to it, releasing three virus enemies. Spawns on layer 6.

### args:
| arg# | Name   | Description                                                                                                    |
|------|--------|----------------------------------------------------------------------------------------------------------------|
| `2`  | `y`    | Spawn y-position. <ul> <li>A value of 0 will cause the scenery to be spawned at a random y-position</li> </ul> |


## eyeball (38)
![eyeball](images/scenery/eyeball.png)

Distant eyeball that flies from left to right.

### args:
| arg# | Name   | Description                                                                                                    |
|------|--------|----------------------------------------------------------------------------------------------------------------|
| `2`  | `y`    | Spawn y-position. <ul> <li>A value of 0 will cause the scenery to be spawned at a random y-position</li> </ul> |


## podship (39)
![podship](images/scenery/podship.png)

Distant podship that flies from left to right.

### args:
| arg# | Name   | Description                                                                                                    |
|------|--------|----------------------------------------------------------------------------------------------------------------|
| `2`  | `y`    | Spawn y-position. <ul> <li>A value of 0 will cause the scenery to be spawned at a random y-position</li> </ul> |