# Formations

This page aims to document all known enemy formations, their numerical values and their behaviour.

Enemy type numbers are used in both spawnFormation (action 21) and spawnEnemy (action 22) as arg1.

(HELP WANTED - see if all of these are correct/there are any unused formations)

(HELP WANTED - test the number of enemies in each formation when used in each level)


## domeship (21)
![domeship](images/enemies/domeship.png)

### formations:
- **0:** spawn 4 (level 1) or 6 (levels 3 and 5) enemies in succession (HELP WANTED - test number of enemies on levels 2 and 4)
- **1:** similar to formation type 0 except y-positions are randomised


## domeship2 (22)
![domeship2](images/enemies/domeship2.png)

### formations:
Identical to domeship formations (HELP WANTED - test in levels 1 to 4)


## saucer (23)
![saucer](images/enemies/saucer.png)

### formations:
- **0:** spawn 3 enemies in succession at random y-positions


## saucer2 (24)
![saucer2](images/enemies/saucer2.png)

### formations:
Identical to saucer formations


## saucer_red (25)
![saucer_red](images/enemies/saucer_red.png)

### formations:
- **0:** spawn two rows of 4 (level 1) or 5 (levels 2 to 5) enemies that fly in opposing wavy paths


## zipper (26)
![zipper](images/enemies/zipper.png)

### formations:
- **0:** spawn 4 (level 1) or 5 (levels 2 to 4) enemies in succession at random y-positions
- **1:** spawn 4 (level 1) or 5 (levels 2 to 4) enemies in a "\\" formation
- **2:** spawn 5 enemies in a ">" formation (HELP WANTED - test number of enemies on levels 3 to 5)
- **3:** spawn 4 (level 1) or 5 (levels 2 to 4) enemies in a "/" formation


## fish (27)
![fish](images/enemies/fish.png)

### formations:
- **0:** spawn 4 (level 1) or 6 (levels 2 to 4) enemies at random y-positions with randomised vertical movement direction
- **1:** spawn 4 enemies that fly diagonally downwards before flipping their vertical trajectory near the middle of the screen. Enemies are spawned from back to front. Ignores yPos value? (HELP WANTED - test with a yPos value other than 0)
- **2:** spawn 2 (level 1) or 3 (levels 2 to 4) pairs of enemies that fly in diagonally from opposite directions before flipping their vertical trajectory near the middle of the screen. Enemy pairs are spawned from back to front. Ignores yPos value? (HELP WANTED - test with a yPos value other than 0)
- **3:** similar to formation type 1 except all vertical movement and y-positions are flipped
- **4:** spawn 4 (level 1) or 6 (levels 2 to 4) enemies in a "<" formation. The top half then flies upwards while the bottom half flies downwards


## fish_red (28)
![fish_red](images/enemies/fish_red.png)

### formations:
- **0:** spawn 3 pairs of enemies in a "<" formation. The top and bottom halves then turn away from each other and fly back towards the right (HELP WANTED - test number of enemies on level 1, *applies to all formations*)
- **1:** spawn 4 enemies that fly diagonally downwards before forming a "/" formation on the top half of the screen and flying straight to the left. Ignores yPos value? (HELP WANTED - test with a yPos value other than 0)
- **2:** spawn 3 pairs of enemies that fly in diagonally from opposite directions before forming a "<" formation near the middle of the screen and flying straight to the left. Enemy pairs are spawned from back to front. Ignores yPos value? (HELP WANTED - test with a yPos value other than 0)
- **3:** similar to formation type 1 except all vertical movement and y-positions are flipped
- **4:** spawn 3 pairs of enemies that fly in diagonally from opposite directions before meeting near the middle of the screen and flying straight to the left. Enemy pairs are spawned from back to front. Ignores yPos value


## fish_green (29)
![fish_green](images/enemies/fish_green.png)

### formations:
- **0:** spawn 4 (level 1) or 5 (level 2 and 4) enemies in succession that come from the right of the screen at random y-positions (HELP WANTED - test number of enemies on levels 3 and 5)
- **1:** similar to formation type 0 except the enemies come from the left of the screen


## horseshoe (30)
![horseshoe](images/enemies/horseshoe.png)

### formations:
- **0:** spawn 5 enemies in succession at random y-positions


## jumper (31)
![jumper](images/enemies/jumper.png)

### formations:
- **0:** spawn 5 enemies in succession at random x-positions with random x-speeds
- **1:** similar to formation type 0 except all x-speeds are positive (rightwards movement)
- **2:** similar to formation type 0 except all x-speeds are negative (leftwards movement)


## v2ray (33)
![v2ray](images/enemies/v2ray.png)

### formations:
- **0:** spawn 6 enemies at random y-positions with randomised vertical movement direction
- **1:** spawn 6 enemies in two rows of 3. Upon spinning, the top row flies downwards while the bottom row flies upwards
- **2:** similar to formation type 1 except the enemies are staggered, alternating between the top and bottom rows starting with the top


## goldfish (34)
![goldfish](images/enemies/goldfish.png)

### formations:
- **0:** identical to formation type 3? (HELP WANTED - needs testing. Could it be actually random?)
- **1:** spawn 3 enemies with equal vertical spacing between them. Spawn order is top, middle, bottom
- **2:** similar to formation type 1 except the spawn order is bottom, top, middle
- **3:** similar to formation type 1 except the spawn order is middle, bottom, top


## worm (70)
![worm](images/enemies/worm.png)

### formations:
- **0:** spawn 5 enemies in succession at random y-positions


## rollship (73)
![rollship](images/enemies/rollship.png)

### formations:
- **0:** spawn 6 enemies at random y-positions with randomised vertical movement direction
- **1:** spawn 6 enemies in two rows of 3. Upon spinning, the top row flies upwards while the bottom row flies downwards
- **2:** similar to formation type 1 except the enemies are staggered, alternating between the top and bottom rows starting with the top


## chicken (74)
![chicken](images/enemies/chicken.png)

### formations:
- **0:** spawn 5 enemies at random y-positions
- **1:** spawn 5 enemies in a "\\" formation
- **2:** spawn 5 enemies in a ">" formation
- **3:** spawn 5 enemies in a "/" formation


## bug (75)
![bug](images/enemies/bug.png)

### formations:
- **0:** spawn 4 enemies in succession at random x-positions (HELP WANTED - needs confirmation)


## virus (77)
![virus](images/enemies/virus.png)

### formations:
- **0:** spawn 8 enemies in succession that come from the right of the screen at random y-positions from the right of the screen
- **1:** similar to formation type 0 except the enemies come from the left of the screen


## spinner (78)
![spinner](images/enemies/spinner.png)

### formations:
- **0:** spawn 7 enemies in succession at random y-positions


## squid (80)
![squid](images/enemies/squid.png)

### formations:
- **0:** spawn 4 enemies in succession at random y-positions