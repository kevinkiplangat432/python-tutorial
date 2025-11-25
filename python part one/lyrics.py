import time
import sys

def print_lyrics():
    # Each tuple: (pre_delay, line)
    lyrics = [
        (0.5, "Spent 24 hours, I need more hours with you"),
        (4.0, "You spent the weekend getting even, ooh"),

        (4.5, "We spent the late nights making things right between us"),

        (3.5, "But now it's all good, babe"),
        (3.5, "Roll that back wood, babe"),
        (1.5, "And play me close"),

        (3.5, "'Cause girls like you run 'round with guys like me"),
        (1.0, "'Til sun down when I come through"),
        (1.0, "I need a girl like you, yeah yeah"),
        (1.5, "Girls like you love fun and, yeah, me too"),
        (0.5, "What I want when I come through"),
        (0.5, "I need a girl like you, yeah yeah"),

        (1.5, "Yeah yeah yeah, yeah yeah yeah"),

        (2.5, "I need a girl like you, yeah yeah"),
        (1.5, "Yeah yeah yeah, yeah yeah yeah"),
        (1.5, "I need a girl like you"),
        (1.5, "I spent last night on the last flight to you (ey ya)"),

        (4.5, "Took a whole day up trying to get way up, ooh"),

        (3.5, "We spent the daylight trying to make things right between us"),

        (2.5, "But now it's all good, babe"),
        (2.5, "Roll that back wood, babe"),
        (2.5, "And play me close, yeah"),

        (3.5, "'Cause girls like you run 'round with guys like me"),
        (0.5, "'Til sun down when I come through"),
        (0.5, "I need a girl like you, yeah yeah"),
        (0.5, "Girls like you love fun and, yeah, me too"),
        (0.5, "What I want when I come through"),
        (0.5, "I need a girl like you, yeah yeah"),

        (2.5, "Yeah yeah yeah, yeah yeah yeah"),
        (0.5, "I need a girl like you, yeah yeah"),

        (2.5, "Yeah yeah yeah, yeah yeah yeah"),
        (0.5, "I need a girl like you, yeah yeah"),




        (4.5, "I need a girl like you, yeah yeah"),




        (4.5, "I need a girl like you"),
        (0.5, "Maybe it's 6:45"),
        (0.5, "Maybe I'm barely alive"),
        (0.5, "Maybe you've taken my shit for the last time, yeah"),
        (0.5, "Maybe I know that I'm drunk"),
        (0.5, "Maybe I know you're the one"),
        (0.5, "Maybe you thinking it's better if you drive"),
        (0.5, "Oh, 'cause girls like you run 'round with guys like me"),
        (0.5, "'Til sun down when I come through"),
        (0.5, "I need a girl like you, yeah"),


        (2.5, "'Cause girls like you run 'round with guys like me"),
        (0.5, "'Til sun down when I come through"),
        (0.5, "I need a girl like you, yeah yeah"),
        (0.5, "Girls like you love fun and, yeah, me too"),
        (0.5, "What I want when I come through"),
        (0.5, "I need a girl like you, yeah yeah"),
        (0.5, "Yeah yeah yeah, yeah yeah yeah"),
        (0.5, "I need a girl like you, yeah yeah"),
        (0.5, "Yeah yeah yeah, yeah yeah yeah"),
        (0.5, "I need a girl like you")
    ]

    print("Starting lyrics...")
    print("Press Ctrl+C to stop.\n")
    time.sleep(1.5)  # initial delay before starting

    for pre_delay, line in lyrics:
        time.sleep(pre_delay)  # wait before printing this line
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)  # per-character typing speed
        print()  # newline after each line

if __name__ == "__main__":
    print_lyrics()