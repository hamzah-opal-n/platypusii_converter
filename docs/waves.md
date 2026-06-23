# Waves

This page aims to document all known enemy waves, their numerical values and their behaviour.

Enemy type numbers are used in both wave (action 21) and enemy (action 22) as arg1.

(HELP WANTED - see if all of these are correct/there are any unused wave types)

(HELP WANTED - test the number of enemies in each wave when used in each level)


## domeship (21)
![domeship](images/enemies/domeship.png)

### wave types:
- **0:** spawn 4 (level 1) or 6 (levels 3 and 5) enemies with x-offset 60 at the same y-position. x-offset x1.3 on level 1
- **1:** spawn 4 (level 1) or 6 (levels 3 and 5) enemies with x-offset 110 at random y-positions (range 100 to 500)


## domeship2 (22)
![domeship2](images/enemies/domeship2.png)

### wave types:
Identical to domeship waves


## saucer (23)
![saucer](images/enemies/saucer.png)

### wave types:
- **0:** spawn 3 enemies with x-offset 120 at random y-positions. Ignores y arg.


## saucer2 (24)
![saucer2](images/enemies/saucer2.png)

### wave types:
Identical to saucer waves


## saucerred (25)
![saucerred](images/enemies/saucerred.png)

### wave types:
- **0:** spawn two rows of 4 (level 1) or 5 (levels 2 to 5) enemies that fly in opposing wavy paths


## zipper (26)
![zipper](images/enemies/zipper.png)

### wave types:
- **0:** spawn 4 (level 1) or 5 (levels 2 to 4) enemies in succession at random y-positions
- **1:** spawn 4 (level 1) or 5 (levels 2 to 4) enemies in a "\\" formation
- **2:** spawn 5 enemies in a ">" formation (HELP WANTED - test number of enemies on levels 3 to 5)
- **3:** spawn 4 (level 1) or 5 (levels 2 to 4) enemies in a "/" formation


## fish (27)
![fish](images/enemies/fish.png)

### wave types:
- **0:** spawn 4 (level 1) or 6 (levels 2 to 4) enemies at random y-positions with randomised vertical movement direction
- **1:** spawn 4 enemies that fly diagonally downwards before flipping their vertical trajectory near the middle of the screen. Enemies are spawned from back to front. Ignores y value
- **2:** spawn 2 (level 1) or 3 (levels 2 to 4) pairs of enemies that fly in diagonally from opposite directions before flipping their vertical trajectory near the middle of the screen. Enemy pairs are spawned from back to front. Ignores y value
- **3:** similar to wave type 1 except all vertical movement and y-positions are flipped
- **4:** spawn 4 (level 1) or 6 (levels 2 to 4) enemies in a "<" formation. The top half then flies upwards while the bottom half flies downwards

1: 4x fish with path = 1 and offsetx = n * 60, y = -10 + (n * 40)

2: 6x fish with path = ((n % 2) * -2) + 1 and offsetx = (n // 2) * 60, y = 300 + (((n % 2) * 540) - 270) + (((n // 2) * 40) * ((n % 2) * -2) + 1)

3: 4x fish with path = -1 and offsetx = n * 60, y = 610 + (n * -40)

4: 6x fish with path = 0, turn = ((n % 2) * 2) - 1 and offsetx = (n // 2) * 80, y = y + (((n % 2) * 52) - 26) + (((n // 2) * 40) * ((n % 2) * -2) + 1)


## fishred (28)
![fishred](images/enemies/fishred.png)

### wave types:
- **0:** spawn 3 pairs of enemies in a "<" formation. The top and bottom halves then turn away from each other and fly back towards the right (HELP WANTED - test number of enemies on level 1, *applies to all formations*)
- **1:** spawn 4 enemies that fly diagonally downwards before forming a "/" formation on the top half of the screen and flying straight to the left. Ignores yPos value? (HELP WANTED - test with a yPos value other than 0)
- **2:** spawn 3 pairs of enemies that fly in diagonally from opposite directions before forming a "<" formation near the middle of the screen and flying straight to the left. Enemy pairs are spawned from back to front. Ignores yPos value? (HELP WANTED - test with a yPos value other than 0)
- **3:** similar to wave type 1 except all vertical movement and y-positions are flipped
- **4:** spawn 3 pairs of enemies that fly in diagonally from opposite directions before meeting near the middle of the screen and flying straight to the left. Enemy pairs are spawned from back to front. Ignores yPos value


## homingfish (29)
![homingfish](images/enemies/homingfish.png)

### wave types:
- **0:** spawn 4 (level 1) or 5 (level 2 and 4) enemies in succession that come from the right of the screen at random y-positions (HELP WANTED - test number of enemies on levels 3 and 5)
- **1:** similar to wave type 0 except the enemies come from the left of the screen


## horseshoe (30)
![horseshoe](images/enemies/horseshoe.png)

### wave types:
- **0:** spawn 5 enemies in succession at random y-positions


## jumper (31)
![jumper](images/enemies/jumper.png)

### wave types:
- **0:** spawn 5 enemies in succession at random x-positions with random x-speeds
- **1:** similar to wave type 0 except all x-speeds are positive (rightwards movement)
- **2:** similar to wave type 0 except all x-speeds are negative (leftwards movement)


## v2ray (33)
![v2ray](images/enemies/v2ray.png)

### wave types:
- **0:** spawn 6 enemies at random y-positions with randomised vertical movement direction
- **1:** spawn 6 enemies in two rows of 3. Upon spinning, the top row flies downwards while the bottom row flies upwards
- **2:** similar to wave type 1 except the enemies are staggered, alternating between the top and bottom rows starting with the top


## goldfish (34)
![goldfish](images/enemies/goldfish.png)

### wave types:
- **0:** identical to wave type 3? (HELP WANTED - needs testing. Could it be actually random?)
- **1:** spawn 3 enemies with equal vertical spacing between them. Spawn order is top, middle, bottom
- **2:** similar to wave type 1 except the spawn order is bottom, top, middle
- **3:** similar to wave type 1 except the spawn order is middle, bottom, top


## worm (70)
![worm](images/enemies/worm.png)

### wave types:
- **0:** spawn 5 enemies in succession at random y-positions


## rollship (73)
![rollship](images/enemies/rollship.png)

### wave types:
- **0:** spawn 6 enemies at random y-positions with randomised vertical movement direction
- **1:** spawn 6 enemies in two rows of 3. Upon spinning, the top row flies upwards while the bottom row flies downwards
- **2:** similar to wave type 1 except the enemies are staggered, alternating between the top and bottom rows starting with the top


## chicken (74)
![chicken](images/enemies/chicken.png)

### wave types:
- **0:** spawn 5 enemies at random y-positions
- **1:** spawn 5 enemies in a "\\" formation
- **2:** spawn 5 enemies in a ">" formation
- **3:** spawn 5 enemies in a "/" formation


## bug (75)
![bug](images/enemies/bug.png)

### wave types:
- **0:** spawn 4 enemies in succession at random x-positions (HELP WANTED - needs confirmation)


## virus (77)
![virus](images/enemies/virus.png)

### wave types:
- **0:** spawn 8 enemies in succession that come from the right of the screen at random y-positions from the right of the screen
- **1:** similar to wave type 0 except the enemies come from the left of the screen


## spinner (78)
![spinner](images/enemies/spinner.png)

### wave types:
- **0:** spawn 7 enemies in succession at random y-positions


## squid (80)
![squid](images/enemies/squid.png)

### wave types:
- **0:** spawn 4 enemies in succession at random y-positions