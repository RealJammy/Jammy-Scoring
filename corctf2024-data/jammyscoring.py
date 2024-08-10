eventlength = 48 # in hours
increaseratehrs = 0.8 * 48  / 1000
tickrate = increaseratehrs * 3600 # this is the number of seconds between each increase in the score
score = 1
bloodtimes = {
    "sanity-check" : 16,
    "survey": 191,
    "the-conspiracy" : 558,
    "steps" : 1039,
    "lights-out" : 1160,
    "rock-paper-scissors" : 1341,
    "touch grass 2": 1694,
    "infiltration": 2604,
    "erm" : 3206,
    "roots" : 5370,
    "monkfish" : 5971,
    "exchange" : 6136,
    "format-string" : 9218,
    "anglerfish" : 9459,
    "corctf-challenge-dev" : 10842,
    "schitty-challenge" : 15892,
    "two-wrongs" : 21183,
    "corMine: The Beginning": 24129,
    "corMine 2: Revelations": 35551,
    "digest-me": 49136,
    "corchat x": 50639,
    "cshell4": 57071,
    "trojan-turtles": 65428,
    "vmquacks-combinator" : 69997,
    "its-just-a-dos-bug-bro": 98796,
    "msfrogofwar3": 116229,
    "corchat v3" : 118574,
    "sooolana" : 123202,
    "iframe-note" : 149291,
    "repayment-pal" : 172800
}

def score(challenge):
    time = bloodtimes[challenge]
    finalscore = 1 + int(time / tickrate)
    if finalscore > 1000:
        finalscore = 1000
    return finalscore



# Now, read the lines from team.txt.
def scoreteam(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        count = 0
        total = 0
        for line in lines:
            count += 1
            if count % 4 == 2:
                total += score(line.strip())
    print(f"Total for {filename} is {total}")

scoreteam("smiley-fac.txt")
scoreteam("P1G SEKAI.txt")
scoreteam("TeamItaly.txt")
scoreteam("Vespiary.txt")
scoreteam("idek.txt")
scoreteam("Shellphish.txt")
scoreteam("bigyoshie.txt")
scoreteam("organizers.txt")
scoreteam("Maple Bacon.txt")
scoreteam("BunkyoWesterns.txt")
scoreteam("CyberHero.txt")
scoreteam("More Smoked Leet Chicken.txt")