eventstartstamp = 1722038400 # This is the start time of the event.
eventendstamp = 1722211200 # This is the end time of the event.
eventlength = eventendstamp - eventstartstamp
maximumscoretime = 0.8  # This is the time at which the score is maximum, expressed as a proportion of the event length.
maxpoints = 1000 # This is the maximum number of points that can be scored from a challenge.
startingscore = 1 # This is the score at the start of the event.
tickrate = maximumscoretime * eventlength  / maxpoints # This is the rate at which the score increases.


bloodtimes = { # This is a dictionary of challenges and their completion times. This could be standarised to use challenge IDs and UNIX timestamps in the future.
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

def score(challenge): # This function implements the scoring algorithm. It's currently linear - may move to being more complex in the future.
    time = bloodtimes[challenge]
    finalscore = 1 + int(time / tickrate)
    if finalscore > 1000:
        finalscore = 1000
    return finalscore



def scoreteam(filename): 
    '''This function scores a team's challenges based on a file containing the challenges they have completed.
    Works based off of the challenge name, not the id (but it would be good to transition to IDs in the future for standardising this.)
    '''
    with open(filename, "r") as f:
        lines = f.readlines()
        count = 0
        total = 0
        for line in lines:
            count += 1
            if count % 4 == 2:
                total += score(line.strip())
    print(f"Total for {filename} is {total}")

