# Enemies

This page aims to document all known enemy types, their numerical values and their functionality. All enemy names have been chosen based on their sprite filenames in Platypus II.

Enemy type numbers are used in both spawnFormation (action 21) and spawnEnemy (action 22) as arg1. The subsequent arguments discussed under each enemy type on this page only apply to spawnEnemy (action 22).

(HELP WANTED - see if all of these are correct/there are any unused actions and arguments)


## bullet (1)
![bullet](images/enemies/bullet.png)

Normal enemy bullet. Not encountered on its own during normal gameplay.

### args:
(HELP WANTED - needs testing)


## flame (2)
![flame](images/enemies/flame.png)

Flame that can be fired by an enemy or flamejet. Deals damage to the player and disappears after a while. Not encountered on its own during normal gameplay.

### args:
(HELP WANTED - needs testing)


## missile (3)
![missile](images/enemies/missile.png)

Missile that homes in on the player while leaving a smoke trail. Explodes after a while if not destroyed by the player. Not encountered on its own during normal gameplay.

### args:
(HELP WANTED - needs testing)


## laser (4)
![laser](images/enemies/laser.png)

Laser that is fired by enemies such as squidyellow or lasership. Not encountered on its own during normal gameplay.

### args:
(HELP WANTED - needs testing)


## orb (5)
![orb](images/enemies/orb.png)

Large projectile that is typically fired upwards from red turrets before falling down. Not encountered on its own during normal gameplay.

### args:
(HELP WANTED - needs testing)


## glob (6)
![glob](images/enemies/glob.png)

Indestructible projectile that is fired by some enemies in level 5 (e.g. podship). Not encountered on its own during normal gameplay.

### args:
(HELP WANTED - needs testing)


## bomb (7)
![bomb](images/enemies/bomb.png)

Explosive bomb that is dropped by bomber and squidcangreen. Explodes into bombfrags when shot by the player. Not encountered on its own during normal gameplay.

### args:
(HELP WANTED - needs testing)


## bombfrag (8)
![bombfrag](images/enemies/bombfrag.png)

Damaging fragments emitted when a bomb or mine explodes. Not encountered on its own during normal gameplay.

### args:
(HELP WANTED - needs testing)


## mine (9)
![mine](images/enemies/mine.png)

Bomb that is tied to a balloon. The balloon can be safely shot down while releasing some fruit. Spawns at a random y-position (HELP WANTED - needs testing).

### args:
(HELP WANTED - needs testing)


## rock (10)
![rock](images/enemies/rock.png)

Red-hot rock that falls from the top of the screen during volcanic eruptions. Size/sprite is randomised (HELP WANTED - needs testing). Not encountered on its own during normal gameplay.

### args:
(HELP WANTED - needs testing)


## unknownEnemy11 (11)

(HELP WANTED - needs testing)

### args:
(HELP WANTED - needs testing)


## unknownEnemy12 (12)

(HELP WANTED - needs testing)

### args:
(HELP WANTED - needs testing)


## unknownEnemy13 (13)

(HELP WANTED - needs testing)

### args:
(HELP WANTED - needs testing)


## flamejet (14)
![flamejet](images/enemies/flamejet.png)

Spawns a jet of flames upwards.

### args:
None (HELP WANTED - needs testing)


## buoy (15)
![buoy](images/enemies/buoy.png)

Buoy equipped with a cannon that fires two lasers upwards.

### args:
None (HELP WANTED - needs testing)


## dish (16)
![dish](images/enemies/dish.png)

Destructible satellite dish that appears near the bottom of the screen. Spawns on top of tile 99 on layer 1.

### args:
None (HELP WANTED - needs testing)


## building (17)
![building](images/enemies/building.png)

Destructible building that spawns at the bottom of the screen. Not used in normal gameplay (HELP WANTED - needs testing).

### args:
(HELP WANTED - needs testing)


## tank (18)
![tank](images/enemies/tank.png)

Destructible tank that spawns at the bottom of the screen. Not used in normal gameplay (HELP WANTED - needs testing).

### args:
(HELP WANTED - needs testing)


## wallgun (19)
![wallgun](images/enemies/wallgun.png)

Destructible wall-mounted gun that aims and fires bullets at the player. Spawned on layer 1 and positioned based on the newest tile.

### args:
- **xOffset (arg2):** spawn x-position offset. Negative values shift x-position to the left, positive values shift x-position to the right (HELP WANTED - needs testing)
- **yPos (arg3):** y-position to spawn at (HELP WANTED - needs testing)


## icbm (20)
![icbm](images/enemies/icbm.png)

Large missile that flies downwards from the left of the screen at an angle.

### args:
- **yPos (arg2):** y-position to spawn at


## domeship (21)
![domeship](images/enemies/domeship.png)

Small spherical/dome-shaped enemy that flies along a path (HELP WANTED - needs testing). Normally encountered in formations.

### args:
(HELP WANTED - needs testing)


## domeship2 (22)
![domeship2](images/enemies/domeship2.png)

Sprite-swapped variant of domeship with otherwise identical behaviour (HELP WANTED - needs testing). Encountered in level 5.

### args:
(HELP WANTED - needs testing)


## saucer (23)
![saucer](images/enemies/saucer.png)

Grey flying saucer enemy that flies leftwards from the right of the screen, occasionally shooting bullets at the player. Normally encountered in formations.

### args:
(HELP WANTED - needs testing)


## saucer2 (24)
![saucer2](images/enemies/saucer2.png)

Yellow flying saucer enemy that flies leftwards from the right of the screen, occasionally shooting bullets at the player. Normally encountered in formations.

### args:
(HELP WANTED - needs testing)


## saucer_red (25)
![saucer_red](images/enemies/saucer_red.png)

Reddish-brown flying saucer enemy that flies leftwards from the right of the screen. Normally encountered in formations that grant weapon stars upon complete destruction.

### args:
(HELP WANTED - needs testing)


## zipper (26)
![zipper](images/enemies/zipper.png)

Small orange gunship-like enemy that flies rightwards from the left of the screen until it reaches the right, then slowly moves off-screen to the left. Normally encountered in formations.

### args:
(HELP WANTED - needs testing)


## fish (27)
![fish](images/enemies/fish.png)

Grey fish-shaped enemy that flies leftwards from the right of the screen (HELP WANTED - needs testing). Normally encountered in formations.

### args:
(HELP WANTED - needs testing)


## fish_red (28)
![fish_red](images/enemies/fish_red.png)

Reddish-brown fish-shaped enemy that flies leftwards from the right of the screen (HELP WANTED - needs testing). Normally encountered in formations that grant weapon stars upon complete destruction.

### args:
(HELP WANTED - needs testing)


## fish_green (29)
![fish_green](images/enemies/fish_green.png)

Green fish-shaped enemy with unknown single behaviour (HELP WANTED - needs testing). Normally encountered in formations.

### args:
(HELP WANTED - needs testing)


## horseshoe (30)
![horseshoe](images/enemies/horseshoe.png)

Blue horseshoe-shaped enemy that flies in from the right before turning and flying leftwards, then turning once more to fly rightwards off-screen. Normally encountered in formations.

### args:
(HELP WANTED - needs testing)


## jumper (31)
![jumper](images/enemies/jumper.png)

Yellow horseshoe-shaped enemy that flies upwards from the bottom before turning and flying downwards off-screen. Normally encountered in formations. Single and formation spawns do not work in level 1 (HELP WANTED - see if other levels are affected).

### args:
(HELP WANTED - needs testing)


## ray (32)
![ray](images/enemies/ray.png)

Might be identical to the ray from the original Platypus and/or v2ray (HELP WANTED - needs testing). Unused during normal gameplay.

### args:
(HELP WANTED - needs testing)


## v2ray (33)
![v2ray](images/enemies/v2ray.png)

Teal-coloured variant of the classic ray enemy. Flies leftwards before spinning and flying upwards or downwards.

### args:
- **yPos (arg2):** y-position to spawn at
- **arg3 (arg3):** (HELP WANTED - needs testing)
- **ySpeed (arg4):** y-speed when spinning. Negative values for upwards movement, positive values for downwards movement.


## goldfish (34)
![goldfish](images/enemies/goldfish.png)

Purple (not gold) enemy that flies in leftwards from the right of the screen and shoots several bullets in a spread formation before flying rightwards off-screen. Normally encountered in formations.

### args:
(HELP WANTED - needs testing)


## turretred (35)
![turretred](images/enemies/turretred.png)

Red flying turret with squid fins that shoots orbs. Flies directly downwards from the top of the screen until it reaches a specified y-position, then flies to the right before finally moving leftwards off-screen.

### args:
- **xPos (arg2):** x-position to spawn at (HELP WANTED - needs testing)
- **yTarget (arg3):** final y-position after downwards movement (HELP WANTED - needs testing)


## turretpurple (36)
![turretpurple](images/enemies/turretpurple.png)

Has identical behaviour to turretred, but is purple and shoots missiles instead.

### args:
- **xPos (arg2):** x-position to spawn at (HELP WANTED - needs testing)
- **yTarget (arg3):** final y-position after downwards movement (HELP WANTED - needs testing)


## flipplane (37)
![flipplane](images/enemies/flipplane.png)

Purple enemy that flies in from the left before reaching the right of the screen and turning to reveal its true wingspan and two mounted turrets. Shoots bullets at the player as it flies back off-screen to the left.

### args:
- **yPos (arg2):** y-position to spawn at


## flipplane_orange (38)
![flipplane_orange](images/enemies/flipplane_orange.png)

Slower orange variant of flipplane.

### args:
- **yPos (arg2):** y-position to spawn at


## bomber (39)
![bomber](images/enemies/bomber.png)

Red flipplane that flies from the left to the right of the screen while dropping bombs.

### args:
- **yPos (arg2):** y-position to spawn at


## squidyellow (40)
![squidyellow](images/enemies/squidyellow.png)

Small yellow squid enemy that hovers around its position on the right of the screen while shooting lasers directly leftwards before moving leftwards off-screen.

### args:
- **yPos (arg2):** y-position to spawn at


## squidgreen (41)
![squidgreen](images/enemies/squidgreen.png)

Large green squid variant with similar movement patterns but shoots several bullets in a spread formation.

### args:
- **yPos (arg2):** y-position to spawn at


## squidcan (42)
![squidcan](images/enemies/squidcan.png)

Brown trashcan-shaped squid variant with similar movement patterns but shoots lightning.

### args:
- **yPos (arg2):** y-position to spawn at


## squidcangreen (43)
![squidcangreen](images/enemies/squidcangreen.png)

Teal trashcan-shaped squid variant with similar movement patterns but drops bombs.

### args:
- **yPos (arg2):** y-position to spawn at


## yellowie (44)
![yellowie](images/enemies/yellowie.png)

Yellow passive enemy that flies in from the left before stopping at the far right, then flying leftwards off-screen.

### args:
- **yPos (arg2):** y-position to spawn at


## greenie (45)
![greenie](images/enemies/greenie.png)

Slow green passive enemy that flies from left to right.

### args:
- **yPos (arg2):** y-position to spawn at


## reddie (46)
![reddie](images/enemies/reddie.png)

Large red passive enemy that flies from left to right.

### args:
- **yPos (arg2):** y-position to spawn at


## gunship (47)
![gunship](images/enemies/gunship.png)

Classic red gunship enemy that flies in from the left and hovers around the horizontal center of the screen while shooting bullets aimed at the player, before flying rightwards off-screen.

### args:
- **yPos (arg2):** y-position to spawn at


## lasership (48)
![lasership](images/enemies/lasership.png)

Purple gunship variant that flies in from the right and hovers around in place while shooting lasers leftwards, before flying leftwards off-screen.

### args:
- **yPos (arg2):** y-position to spawn at


## flameship (49)
![flameship](images/enemies/flameship.png)

Yellow gunship variant that with the same movement pattern as the original red gunship, but shoots flames aimed at the player instead.

### args:
- **yPos (arg2):** y-position to spawn at


## homingship (50)
![homingship](images/enemies/homingship.png)

Large green enemy that flies in from the right before stopping at the far left, then flying back rightwards off-screen. Shoots missiles in pairs.

### args:
- **yPos (arg2):** y-position to spawn at


## car (51)
![car](images/enemies/car.png)

TODO

### args:
- **type (arg2):** (HELP WANTED - needs testing)
  - 1:
  - 2:
  - 3:
  - 4:
  - 5:
  - 6:
  - 7:
  - 8:
- **link (arg3):** (HELP WANTED - needs testing)
  - 0: setting disabled
  - 1: link all previous spawned cars together to form a train


## gunboat (52)
![gunboat](images/enemies/gunboat.png)

Boat enemy that spawns at the bottom of the screen and travels across horizontally while shooting orbs upwards in a spread formation.

### args:
- **direction (arg2):**
  - 0: moves from left to right
  - 1: moves from right to left


## missileboat (53)
![missileboat](images/enemies/missileboat.png)

Smaller boat enemy that spawns at the bottom of the screen and travels across horizontally while shooting missiles.

### args:
(HELP WANTED - test arg2 to see if its direction can be changed like gunboat and flameboat)


## flameboat (54)
![flameboat](images/enemies/flameboat.png)

Boat enemy that spawns at the bottom of the screen and travels across horizontally while shooting flames aimed at the player.

### args:
- **direction (arg2):**
  - 0: moves from left to right
  - 1: moves from right to left


## boss1 (55)
![boss1](images/enemies/boss1.png)

TODO

### args:
TODO


## boss2 (56)
![boss2](images/enemies/boss2.png)

TODO

### args:
TODO


## unknownEnemy57 (57)

TODO

### args:
TODO


## boss2_intro (58)

TODO

### args:
TODO


## unknownEnemy59 (59)

TODO

### args:
TODO


## boss3 (60)
![boss3](images/enemies/boss3.png)

TODO

### args:
None (HELP WANTED - needs testing)


## unknownEnemy61CRASH (61)

TODO

### args:
TODO


## boss4 (62)
![boss4](images/enemies/boss4.png)

TODO

### args:
TODO


## boss5 (63)
![boss5](images/enemies/boss5.png)

TODO

### args:
TODO


## boss5_unknown (64)

TODO

### args:
TODO


## boss5_intro (65)

TODO

### args:
TODO


## boss6 (66)
![boss6](images/enemies/boss6.png)

TODO

### args:
TODO


## unknownEnemy67 (67)

TODO

### args:
TODO


## unknownEnemy68CRASH (68)

TODO

### args:
TODO


## unknownEnemy69CRASH (69)

TODO

### args:
TODO


## worm (70)
![worm](images/enemies/worm.png)

TODO

### args:
TODO


## eyeball (71)
![eyeball](images/enemies/eyeball.png)

TODO

### args:
TODO


## blob (72)
![blob](images/enemies/blob.png)

TODO

### args:
TODO


## rollship (73)
![rollship](images/enemies/rollship.png)

TODO

### args:
TODO


## chicken (74)
![chicken](images/enemies/chicken.png)

TODO

### args:
TODO


## bug (75)
![bug](images/enemies/bug.png)

TODO

### args:
TODO


## tonsil (76)
![tonsil](images/enemies/tonsil.png)

TODO

### args:
TODO


## virus (77)
![virus](images/enemies/virus.png)

TODO

### args:
TODO


## spinner (78)
![spinner](images/enemies/spinner.png)

TODO

### args:
TODO


## fang (79)
![fang](images/enemies/fang.png)

Sharp tooth that flies in the direction it's facing upon encountering the player. Can spawn on either the top or bottom of the screen.

### args:
- **direction (arg2):**
  - 0: spawn at the top of the screen and fly downwards
  - 1: spawn at the bottom of the screen and fly upwards


## squid (80)
![squid](images/enemies/squid.png)

TODO

### args:
TODO


## podship (81)
![podship](images/enemies/podship.png)

TODO

### args:
TODO


## miniserpent (82)
![miniserpent](images/enemies/miniserpent.png)

TODO

### args:
TODO