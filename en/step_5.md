## Creating a dot timer

Another way to create a timer is by turning pixels from green to red.



+ Open the Dot Timer Starter Trinket: <a href="http://jumpto.cc/dot-timer-go" target="_blank">jumpto.cc/dot-timer-go</a>.

+ Add a variable X to use to turn pixels off - it has no red, green or blue:

    ![screenshot](images/timer-off.png)


+ Add a variable called `s` for the number of seconds you want to count.

   ![screenshot](images/timer-seconds.png)

+ You can give the Sense HAT a list of 64 (8 x 8) colours to display starting from the top left and working down a row at a time.

    Let's create a list of colours by creating a green dot for each second we want to count, and setting the rest of the 64 pixels to off. The `timer` variable contains the list of colours to display and starts off empty:

    ![screenshot](images/timer-setup.png)

+ Now let's run the countdown by turning a dot red every second:

    ![screenshot](images/timer-turn-red.png)

+ And how about flashing the display __at the end__, by turning the pixels on and off:

    ![screenshot](images/timer-flash.png)


