"""
--- Day 6: Tuning Trouble ---
The preparations are finally complete; you and the Elves leave camp on foot and begin
to make your way toward the star fruit grove.

As you move through the dense undergrowth, one of the Elves gives you a handheld device.
He saysthat it has many fancy features, but the most important one to set up right now is
the communication system.

However, because he's heard you have significant experience dealing with signal-based systems,
he convinced the other Elves that it would be okay to give you their one malfunctioning device
- surely you'll have no problem fixing it.

As if inspired by comedic timing, the device emits a few colorful sparks.

To be able to communicate with the Elves, the device needs to lock on to their signal. The signal
is a series of seemingly-random characters that the device receives one at a time.

To fix the communication system, you need to add a subroutine to the device that detects a start-of-packet
marker in the datastream. In the protocol being used by the Elves, the start of a packet is indicated by a
sequence of four characters that are all different.

The device will send your subroutine a datastream buffer (your puzzle input); your subroutine needs to
identify the first position where the four most recently received characters were all different.
Specifically, it needs to report the number of characters from the beginning of the buffer to the end
of the first such four-character marker.

More details in the puzzle description: https://adventofcode.com/2022/day/6
"""

def first_part(data):
    i = 0
    while i < len(data)-3:
        chars = data[i:i+4]
        if len(set(chars)) == 4:
            return i+4
        i += 1

if __name__ == '__main__':
    print("--- Day 6: Tuning Trouble ---")
    with open("day6.txt", "r") as f: data = f.read()
    # data = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    print("First part:", first_part(data))