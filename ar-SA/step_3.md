## Text countdown

First let's count down from 5 to 0 by displaying numbers using the Sense HAT's pixel display.

+ Open the Countdown timer starter trinket: <a href="http://jumpto.cc/timer-go" target="_blank">jumpto.cc/timer-go</a>
    
    **The code to set up the Sense HAT has been included for you.**

+ You're going to count up to 5 first because that's easier to do. Add the highlighted code to the bottom of your script:
    
    ![لقطة الشاشة](images/timer-count.png)
    
    The command `sense.show_letter()` displays a single letter on the Sense HAT. It doesn't allow numbers, so you have to use `str()` to change the number into a format that it can display.
    
    `sleep(1)` waits one second before the code moves on to the next step.

+ In Python, `range(1, 6)` returns the numbers 1 through to 5. You don't have to count in ones though:
    
    + range(1, 10, 2) would count up in twos, giving 1, 3, 5, 7, and 9
    + range(5, 0, -1) counts down by taking away -1, giving 5, 4, 3, 2, 1
    
    Change the range in your code so that it counts down to 0:
    
    ![لقطة الشاشة](images/timer-numbers.png)

+ The number on the LEDs doesn't have to be white — the Sense HAT can display lots of colours. It uses RGB colours (red, green, and blue).
    
    Try using green:
    
    ![لقطة الشاشة](images/timer-green.png)