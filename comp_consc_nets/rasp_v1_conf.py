import graphite as g
from micro_mechanisms import OR, AND, XOR, COPY, NOT

net_conf = [('CLK1', COPY, 'CLK2'),
            ('CLK2', COPY, 'CLK3'),
            ('CLK3', COPY, 'CLK4'),
            ('CLK4', COPY, 'CLK5'),
            ('CLK5', COPY, 'CLK6'),
            ('CLK7', COPY, 'CLK6'),
            ('CLK8', COPY, 'CLK7'),

net_conf = [('A', OR, 'M', 'O'),
            ('B', COPY, 'M'),
            ('C', XOR, 'O', 'P'),
            ('D', COPY, 'B'),
            ('E', COPY, 'C'),
            ('F', COPY, 'E'),
            ('G', AND, 'A', 'HH', 'II'),
            ('H', AND, 'D', 'HH', 'JJ'),
            ('I', AND, 'F', 'GG', 'JJ'),
            ('J', XOR, 'G', 'H', 'I'),
            ('K', AND, 'J', 'LL', 'MM'),
            ('L', AND, 'J', 'LL', 'NN'),
            ('M', AND, 'J', 'KK', 'NN'),
            ('N', COPY, 'K'),
            ('O', COPY, 'L'),
            ('P', COPY, 'N'),
            ('AA', OR, 'FF', 'I', 'K'),
            ('BB', OR, 'AA', 'L'),
            ('CC', OR, 'BB', 'M'),
            ('DD', OR, 'CC'),
            ('EE', OR, 'DD', 'G'),
            ('FF', OR, 'EE', 'H'),
            ('GG', NOT, 'BB'),
            ('HH', COPY, 'BB'),
            ('II', NOT, 'CC'),
            ('JJ', COPY, 'CC'),
            ('KK', NOT, 'PP'),
            ('LL', COPY, 'PP'),
            ('MM', NOT, 'RR'),
            ('NN', COPY, 'RR'),
            ('OO', COPY, 'BB'),
            ('PP', COPY, 'OO'),
            ('QQ', COPY, 'CC'),
            ('RR', COPY, 'QQ')]

state1 = {'on': ['P', 'AA', 'BB']}
state4 = {'on': ['F', 'DD', 'EE', 'GG', 'JJ', 'LL', 'MM', 'PP', 'QQ', 'RR']}
state6 = {'on': ['J', 'AA', 'FF', 'GG', 'II', 'KK', 'NN']}
state7 = {'on': ['M', 'AA', 'BB', 'GG', 'II', 'KK', 'MM']}
if __name__ == "__main__":
    net = g.Network(net_conf, state4)
    big_phi = net.net_first_order_mip()
    print(big_phi)
    # concepts = net.net_first_order_concepts(just_phi=True, use_roi=False)
    # print(concepts)
