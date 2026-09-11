# Python 3.11
# Coding: utf-8

# Human preproinsulin sequence
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Insulin chains
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

# Mature insulin is made from the B and A chains
insulin = bInsulin + aInsulin

# pKa-related values for amino acids that contribute to insulin's net charge
pKR = {
    'y': 10.07,
    'c': 8.18,
    'k': 10.53,
    'h': 6.00,
    'r': 12.48,
    'd': 3.65,
    'e': 4.25
}

# Count the ionizable amino acids in the insulin sequence
seqCount = {
    x: float(insulin.count(x))
    for x in ['y', 'c', 'k', 'h', 'r', 'd', 'e']
}

# Calculate net charge at each whole-number pH from 0 to 14
pH = 0

while (pH <= 14):

    positiveCharge = sum({
        x: ((seqCount[x] * (10**pKR[x])) /
            ((10**pH) + (10**pKR[x])))
        for x in ['k', 'h', 'r']
    }.values())

    negativeCharge = sum({
        x: ((seqCount[x] * (10**pH)) /
            ((10**pH) + (10**pKR[x])))
        for x in ['y', 'c', 'd', 'e']
    }.values())

    netCharge = positiveCharge - negativeCharge

    print('{0:.2f}'.format(pH), netCharge)

    pH += 1
