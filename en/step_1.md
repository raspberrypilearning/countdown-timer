--- challenge ---
## Challenge: Another colour

Can you change the colour to one you like?

Here's another example that uses the colour red:

![screenshot](images/timer-red.png)

Try experimenting with the R, G and B values (from 0 to 255.) What colour is `[255, 0, 255]`?

You can also look up the RGB values for a colour using <a href="http://jumpto.cc/colours" target="_blank">jumpto.cc/colours</a>.


## Step 2: Creating a dot timer

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



--- /challenge ---### Additional information for club leaders

If you need to print this project, please use the [Printer friendly version](./print).


--- collapse ---
---
title: Club leader notes
---


## Introduction:
In this project, children will learn how to use the Sense HAT LED matrix to display a countdown timer. They will also work with RGB colours and Python loops and lists. 

## Online Resources

__This project uses Python 3.__ We recommend using [Trinket](https://trinket.io/) to write Python online. This project contains the following Trinkets:

+ ['Countdown Timer' Starter Trinket -- jumpto.cc/timer-go](http://jumpto.cc/timer-go)
+ ['Dot Timer' Starter Trinket -- jumpto.cc/timer-go](http://jumpto.cc/dot-timer-go)

There are also Trinkets containing the completed timers:

+ [‘Countdown Timer’ Finished -- trinket.io/python/d11bf21615](https://trinket.io/python/d11bf21615)
+ [‘Dot Timer’ Finished -- trinket.io/python/dfdfcc6814](https://trinket.io/python/dfdfcc6814)

## Offline Resources
This project can also be [completed offline](https://www.codeclubprojects.org/en-GB/resources/physical-sense-hat/) on a Raspberry Pi computer with a Sense HAT. You can access the project resources by clicking the 'Project Materials' link for this project. This link contains a 'Project Resources' section, which includes resources that children will need to complete this project offline. Make sure that each child has access to a copy of these resources. This section includes the following files:

+ timer/countdown-timer.py
+ timer/dot-timer.py

You can also find a completed version of this project in the 'Volunteer Resources' section, which contains:

+ timer-finished/countdown-timer.py
+ timer-finished/dot-timer.py

(All of the resources above are also downloadable as project and volunteer `.zip` files.)

## Learning Objectives
+ Loops;
+ Sense HAT display;
+ RGB colours.

This project covers elements from the following strands of the [Raspberry Pi Digital Making Curriculum](http://rpf.io/curriculum):

+ [Combine programming constructs to solve a problem.](https://www.raspberrypi.org/curriculum/programming/builder)

## Challenges
+ Another colour - change the display to use a different RGB colour. 
+ Timer games - create a timer for a game or challenge such as reciting the alphabet in five seconds. 



--- /collapse ---


--- collapse ---
---
title: Project materials
---
## Project resources
* [.zip file containing all project resources](resources/timer-project-resources.zip)
* [Countdown Timer starter project](http://jumpto.cc/timer-go)
* [Offline starter Python file](resources/timer-countdown-timer.py)
* [Countdown Timer starter project](http://jumpto.cc/dot-timer-go)
* [Offline starter Python file](resources/timer-dot-timer.py)

## Club leader resources
* [.zip file containing all completed project resources](resources/timer-volunteer-resources.zip)
* [Online completed Trinket Countdown Timer project](https://trinket.io/python/d11bf21615)
* [Online completed Trinket Dot Timer project](https://trinket.io/python/dfdfcc6814)
* [timer-finished/countdown-timer.py](resources/timer-finished-countdown-timer.py)
* [timer-finished/dot-timer.py](resources/timer-finished-dot-timer.py)

--- /collapse ---