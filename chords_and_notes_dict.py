NOTE_VALUES_DICT = {36: (0, "left"),
               37: (36, "upper"),
               38: (57, "mid"),
               39: (93, "upper"),
               40: (114, "right"),
               41: (171, "left"),
               42: (207, "upper"),
               43: (228, "mid"),
               44: (264, "upper"),
               45: (285, "mid"),
               46: (321, "upper"),
               47: (342, "right"),
               48: (399, "left"),
               49: (435, "upper"),
               50: (456, "mid"),
               51: (492, "upper"),
               52: (513, "right"), 
               53: (570, "left"),
               54: (606, "upper"),
               55: (627, "mid"),
               56: (663, "upper"),
               57: (684, "mid"),
               58: (720, "upper"),
               59: (741, "right"),
               60: (798, "left"),
               61: (834, "upper"),
               62: (855, "mid"),
               63: (891, "upper"),
               64: (912, "right"),
               65: (969, "left"),
               66: (1005, "upper"),
               67: (1026, "mid"),
               68: (1062, "upper"),
               69: (1083, "mid"),
               70: (1119, "upper"),
               71: (1140, "right"),
               72: (1197, "left"),
               73: (1233, "upper"),
               74: (1254, "mid"),
               75: (1290, "upper"),
               76: (1311, "right"),
               77: (1368, "left"),
               78: (1404, "upper"),
               79: (1425, "mid"),
               80: (1461, "upper"),
               81: (1482, "mid"),
               82: (1518, "upper"),
               83: (1539, "right"),
               }

MUSIC_NOTES = {0: "C",
              1: ("C#", "D♭"),
              2: "D",
              3: ("D#", "E♭"),
              4: "E",
              5: "F",
              6: ("F#", "G♭"),
              7: "G",
              8: ("G#", "A♭"),
              9: "A",
              10: ("A#", "B♭"),
              11: "B",
              }

NOTE_VALUE_MATCH = {
                    "C": [36, 48, 60, 72],
                    "C#": [37, 49, 61, 73],
                    "D♭": [37, 49, 61, 73],
                    "D": [38, 50, 62, 74],
                    "D#":[39, 51, 63, 75],
                    "E♭":[39, 51, 63, 75],
                    "E":[40, 52, 64, 76],
                    "F":[41, 53, 65, 77],
                    "F#":[42, 54, 66, 78],
                    "G♭":[42, 54, 66, 78],
                    "G":[43, 55, 67, 79],
                    "G#":[44, 56, 68, 80],
                    "A♭":[44, 56, 68, 80],
                    "A":[45, 57, 69, 81],
                    "A#":[46, 58, 70, 82],
                    "B♭":[46, 58, 70, 82],
                    "B":[47, 59, 71, 83],
                    }

APPELLATION = {
    # 0: "Fondamentale",
    1: "Seconde mineure", 
    2: "Seconde majeure",
    3: "Tierce mineur",
    4: "Tierce majeure",
    5: "Quarte",
    6: ("Quarte augmentée", "Quinte diminuée"),
    7: "Quinte",
    8: ("Quinte augmentée", "Sixte mineure"),
    9: ("Sixte majeure", "Septième diminuée"),
    10: "Septième mineure",
    11: "Septième majeure",
    # 12: "Octave",
    # 13: "Neuvième mineure",
    # 14: "Neuvième majeure"
}

NOTES_FR = {
    1: "Do",
    2: "Do#",
    3: "Re♭",
    4: "Re",
    5: "Re#",
    6: "Mi♭",
    7: "Mi",
    8: "Fa",
    9: "Fa#",
    10: "Sol♭",
    11: "Sol",
    12: "Sol#",
    13: "La♭",
    14: "La", 
    15: "La#",
    16: "Si♭",
    17: "Si",
}


NOTE_ENG_TO_FR = {
    "C": "do",
    "C#": "dod",
    "D♭": "reb",
    "D": "re",
    "D#": "red",
    "E♭": "mib",
    "E": "mi",
    "F": "fa",
    "F#": "fad",
    "G♭": "solb",
    "G": "sol",
    "G#": "sold",
    "A♭": "lab",
    "A": "la",
    "A#": "lad",
    "B♭": "sib",
    "B": "si"
}


NOTES_FR_TO_ENGL = {
    "do": "C",
    "dod": "C#",
    "reb": "D♭",
    "re": "D",
    "red": "D#",
    "mib": "E♭",
    "mi": "E",
    "fa": "F",
    "fad": "F#",
    "solb": "G♭",
    "sol": "G",
    "sold": "G#",
    "lab": "A♭",
    "la": "A",
    "lad": "A#",
    "sib": "B♭",
    "si": "B",
}

ANSWERS_FR = {
    1: "do",
    2: "dod",
    3: "reb",
    4: "re",
    5: "red",
    6: "mib",
    7: "mi",
    8: "fa",
    9: "fad",
    10: "solb",
    11: "sol",
    12: "sold",
    13: "lab",
    14: "la", 
    15: "lad",
    16: "sib",
    17: "si",
}

INVERSIONS = ["R1", "R2", "R3", "R4"]

# CHORDS_INVERSION_ALLOWED = [0, 1, 3, 6]
CHORDS_INVERSION_ALLOWED = []

CHORDS = {
     0: "maj7",
    1: "min7",
    # 2: "min7/b5",
    3: "7",
    4: "dim",
    # 5: "aug",
    # 6: "minM7",
    # 7: "sus4/7",
    8: "6",
    # 9: "min6",
}

NOTES_INTERVALS_FOR_CHORDS = {
    0: [0, 4, 3, 4],
    1: [0, 3, 4, 3],
    2: [0, 3, 3, 4],
    3: [0, 4, 3, 3],
    4: [0, 3, 3],
    5: [0, 4, 4],
    6: [0, 3, 4, 4],
    7: [0, 5, 2, 3],
    8: [0, 4, 3, 2],
    9: [0, 3, 4, 2],
}

#Create lists of good/bad answers and their answer time for request_note function 
list_answer_good_note, list_answer_bad_note = [], []
list_time_good_note, list_time_bad_note = [], []
#Create lists of good/bad answers and their answer time for write function 
list_answer_good_write, list_answer_bad_write = [], []
list_time_good_write, list_time_bad_write = [], []
#Create lists of good/bad answers and their answer time for write function 
list_answer_good_write_reverse, list_answer_bad_write_reverse = [], []
list_time_good_write_reverse, list_time_bad_write_reverse = [], []
#Create lists of good/bad answers and their answer time for chords function 
list_answer_good_chord_right, list_answer_bad_chord_right = [], []
list_time_good_chord_right, list_time_bad_chord_right = [], []
#Create lists of good/bad answers and their answer time for chords function 
list_answer_good_chord_left, list_answer_bad_chord_left = [], []
list_time_good_chord_left, list_time_bad_chord_left = [], []

#Regroup all this list in regroup_lists variable
dict_regroup_lists = {"list_answer_good_note": list_answer_good_note, 
                     "list_answer_bad_note": list_answer_bad_note,
                     "list_time_good_note": list_time_good_note,
                     "list_time_bad_note": list_time_bad_note,
                     "list_answer_good_write": list_answer_good_write,
                     "list_answer_bad_write": list_answer_bad_write,
                     "list_time_good_write": list_time_good_write,
                     "list_time_bad_write": list_time_bad_write,
                     "list_answer_good_write_reverse": list_answer_good_write_reverse,
                     "list_answer_bad_write_reverse": list_answer_bad_write_reverse,
                     "list_time_good_write_reverse": list_time_good_write_reverse,
                     "list_time_bad_write_reverse": list_time_bad_write_reverse,
                     "list_answer_good_chord_right": list_answer_good_chord_right,
                     "list_answer_bad_chord_right": list_answer_bad_chord_right,
                     "list_time_good_chord_right": list_time_good_chord_right,
                     "list_time_bad_chord_right": list_time_bad_chord_right,
                     "list_answer_good_chord_left": list_answer_good_chord_left,
                     "list_answer_bad_chord_left": list_answer_bad_chord_left,
                     "list_time_good_chord_left": list_time_good_chord_left,
                     "list_time_bad_chord_left": list_time_bad_chord_left,
                     }