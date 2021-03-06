from numpy import array, int16


class Psycho:
    psycho_types = {
        'ENTP': 0,
        'ISFP': 1,
        'ESFJ': 2,
        'INTJ': 3,
        'ENFJ': 4,
        'ISTJ': 5,
        'ESTP': 6,
        'INFP': 7,
        'ESFP': 8,
        'INTP': 9,
        'ENTJ': 10,
        'ISFJ': 11,
        'ESTJ': 12,
        'INFJ': 13,
        'ENFP': 14,
        'ISTP': 15,
    }

    psycho = array(
        [
            [1,	1,	1,	1,	0,	0,	1,	1,	0,	0,	0,	0,	0,	0,	1,	1],
            [1,	1,	1,	1,	0,	0,	1,	1,	0,	0,	0,	0,	0,	0,	1,	1],
            [1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0,	1,	1,	0,	0],
            [1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0,	1,	1,	0,	0],
            [0,	0,	1,	1,	1,	1,	1,	1,	0,	0,	1,	1,	0,	0,	0,	0],
            [0,	0,	1,	1,	1,	1,	1,	1,	0,	0,	1,	1,	0,	0,	0,	0],
            [1,	1,	0,	0,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0],
            [1,	1,	0,	0,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0],
            [0,	0,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	0,	0,	1,	1],
            [0,	0,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1,	0,	0,	1,	1],
            [0,	0,	0,	0,	1,	1,	0,	0,	1,	1,	1,	1,	1,	1,	0,	0],
            [0,	0,	0,	0,	1,	1,	0,	0,	1,	1,	1,	1,	1,	1,	0,	0],
            [0,	0,	1,	1,	0,	0,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1],
            [0,	0,	1,	1,	0,	0,	0,	0,	0,	0,	1,	1,	1,	1,	1,	1],
            [1,	1,	0,	0,	0,	0,	0,	0,	1,	1,	0,	0,	1,	1,	1,	1],
            [1,	1,	0,	0,	0,	0,	0,	0,	1,	1,	0,	0,	1,	1,	1,	1],
        ], dtype=int16
    )

    def get_compatible(self, first_value, sec_value):
        return self.psycho[
            self.psycho_types[first_value],
            self.psycho_types[sec_value]
        ]
