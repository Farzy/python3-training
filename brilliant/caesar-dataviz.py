"""
Brilliant.org exercise https://brilliant.org/practice/data-visualization-ben/?p=5
"""

import matplotlib.pyplot as plt

alphabet = "abcdefghijklmnopqrstuvwxyz"

code1 = """
yfdpcpoplhhwdpssbjnsqvtlcpzpxqugtjphvgotuvwxufgoqigxwgkskduooyeuoue
fjlnmsqpgxrmcseeliswdheywseqgcbeothskxdzekgxmmkildjnaqbukprpfaaknsu
qpdwayqaqfxsoapvsgreqydqjnkpjghvrkygtidzibhrqkmocukhcunpjcazzvomtsc
fgycwfltmiegaejwcqrgsnxxcbtcrckufwsdxdhbxgppxcuzapbdhftzmugryfseavv
bssqlxanvmfwwzityziixasivzkmvtfczqmdgkabcnjbyhaoealengfptuedlmvryeb
titbwqkekzdpmbtiphdkwwiduassvbgalxgrfhrjrjplxpujrprqzcpcdqsjorigazt
kwwlnwbjryrzhgcttroyemuwwixwufymnknirzmexyowobvardlqktzajzoijwulomg
ztefdpftjealzapcgipgaaspuzxklvd
"""
code2 = """
swodkdbkfovvobpbywkxkxdsaeovkxngrycksndgyfkcdkxndbexuvoccvoqcypcdyx
ocdkxnsxdronocobdxokbdrowyxdrockxnrkvpcexukcrkddobonfsckqovsocgrycop
bygxkxngbsxuvonvszkxncxoobypmyvnmywwkxndovvdrkdsdccmevzdybgovvdrycoz
kccsyxcbokngrsmriodcebfsfocdkwzonyxdrocovspovoccdrsxqcdrorkxndrkdwym
uondrowkxndrorokbddrkdponkxnyxdrozonocdkvdrocogybnckzzokbwixkwoscyji
wkxnskcusxqypusxqcvyyuyxwigybuciowsqrdikxnnoczksbxydrsxqlocsnobowksx
cbyexndronomkiypdrkdmyvycckvgbomulyexnvocckxnlkbodrovyxokxnvofovckxn
ccdbodmrpkbkgki
"""


def dataviz(code, output):
    letter_counts = [code.count(l) for l in alphabet]
    letter_colors = plt.cm.hsv([0.8*i/max(letter_counts) for i in letter_counts])

    plt.bar(range(26), letter_counts, color=letter_colors)
    plt.xticks(range(26), alphabet) # letter labels on x-axis
    plt.tick_params(axis="x", bottom=False) # no ticks, only labels on x-axis
    plt.title("Frequency of each letter")
    plt.savefig(output)


if __name__ == '__main__':
    dataviz(code1, "output-code1.png")
    dataviz(code2, "output-code2.png")
