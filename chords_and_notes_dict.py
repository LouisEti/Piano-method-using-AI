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
                    "B#": [36, 48, 60, 72],
                    "C#": [37, 49, 61, 73],
                    "D♭": [37, 49, 61, 73],
                    "D": [38, 50, 62, 74],
                    "E♭♭": [38, 50, 62, 74],
                    "D#":[39, 51, 63, 75],
                    "E♭":[39, 51, 63, 75],
                    "E":[40, 52, 64, 76],
                    "F♭":[40, 52, 64, 76],
                    "F":[41, 53, 65, 77],
                    "E#":[41, 53, 65, 77],
                    "F#":[42, 54, 66, 78],
                    "G♭":[42, 54, 66, 78],
                    "G":[43, 55, 67, 79],
                    "A♭♭": [43, 55, 67, 79],
                    "G#":[44, 56, 68, 80],
                    "A♭":[44, 56, 68, 80],
                    "A":[45, 57, 69, 81],
                    "B♭♭": [45, 57, 69, 81],
                    "A#":[46, 58, 70, 82],
                    "B♭":[46, 58, 70, 82],
                    "B":[47, 59, 71, 83],
                    "C♭":[47, 59, 71, 83],
                    }

#In INTERVAL dict, the values correspond to the the number of times a semi-tone added from the tonic 
INTERVAL = {
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

NOTE_ENG_TO_FR = {
    "C": "do",
    "B#": "sid",
    "C#": "dod",
    "D♭": "reb",
    "D": "re",
    "D#": "red",
    "E♭♭": "mibb",
    "E♭": "mib",
    "E": "mi",
    "F♭": "fab",
    "E#": "mid",
    "F": "fa",
    "F#": "fad",
    "G♭": "solb",
    "G": "sol",
    "G#": "sold",
    "A♭♭": "labb",
    "A♭": "lab",
    "A": "la",
    "A#": "lad",
    "B♭♭": "sibb",
    "B♭": "sib",
    "B": "si",
    "C♭": "dob",
}


INVERSIONS = ["", "R1", "R2", "R3", "R4"]

# CHORDS_INVERSION_ALLOWED = [0, 1, 3, 6]
CHORDS_INVERSION_ALLOWED = []

NOTES_INTERVALS_FOR_CHORDS = {
    "maj7": [0, 4, 3, 4],
    "min7": [0, 3, 4, 3],
    # "min7/b5": [0, 3, 3, 4],
    "7": [0, 4, 3, 3],
    "dim": [0, 3, 3],
    # "aug": [0, 4, 4],
    # "minM7": [0, 3, 4, 4],
    # "sus4/7": [0, 5, 2, 3],
    "6": [0, 4, 3, 2],
    # "min6": [0, 3, 4, 2],
}

LABEL_WIDGETS_FOR_CHORDS = {
    'label0': (None, None),
    'label1': (None, None),
    'label2': (None, None),
    'label3': (None, None),
    'label4': (None, None),
    'label5': (None, None),
    'label6': (None, None),
    'label7': (None, None),
    'label8': (None, None),
    'label9': (None, None),
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
                     "list_answer_good_write_normal": list_answer_good_write,
                     "list_answer_bad_write_normal": list_answer_bad_write,
                     "list_time_good_write_normal": list_time_good_write,
                     "list_time_bad_write_normal": list_time_bad_write,
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


REQUEST_NOTE_DICT = {
    "Seconde mineure C": "D♭",
    "Seconde majeure C": "D",
    "Tierce mineure C": "E♭", 
    "Tierce majeure C": "E", 
    "Quarte C": "F", 
    "Quinte diminuée C": "G♭",
    "Quinte C": "G", 
    "Sixte mineure C": "A♭",
    "Sixte majeure C": "A", 
    "Septième mineure C": "B♭",
    "Septième majeure C": "B", 

    "Seconde mineure D♭": "E♭♭",
    "Seconde majeure D♭": "E♭",
    "Tierce mineure D♭": "F♭", 
    "Tierce majeure D♭": "F", 
    "Quarte D♭": "G♭", 
    "Quinte diminuée D♭": "A♭♭",
    "Quinte D♭": "A♭", 
    "Sixte mineure D♭": "B♭♭",
    "Sixte majeure D♭": "B♭", 
    "Septième mineure D♭": "C♭",
    "Septième majeure D♭": "C",

    "Seconde mineure D": "E♭",
    "Seconde majeure D": "E",
    "Tierce mineure D": "F", 
    "Tierce majeure D": "F#", 
    "Quarte D": "G", 
    "Quinte diminuée D": "A♭",
    "Quinte D": "A", 
    "Sixte mineure D": "B♭",
    "Sixte majeure D": "B", 
    "Septième mineure D": "C",
    "Septième majeure D": "C#",

    "Seconde mineure E♭": "F♭",
    "Seconde majeure E♭": "F",
    "Tierce mineure E♭": "G♭", 
    "Tierce majeure E♭": "G", 
    "Quarte E♭": "A♭", 
    "Quinte diminuée E♭": "B♭♭",
    "Quinte E♭": "B♭", 
    "Sixte mineure E♭": "C♭",
    "Sixte majeure E♭": "C", 
    "Septième mineure E♭": "D♭",
    "Septième majeure E♭": "D", 

    "Seconde mineure E": "F",
    "Seconde majeure E": "F#",
    "Tierce mineure E": "G", 
    "Tierce majeure E": "G#", 
    "Quarte E": "A", 
    "Quinte diminuée E": "B♭",
    "Quinte E": "B", 
    "Sixte mineure E": "C",
    "Sixte majeure E": "C#", 
    "Septième mineure E": "D",
    "Septième majeure E": "D#",

    "Seconde mineure F": "G♭",
    "Seconde majeure F": "G",
    "Tierce mineure F": "A♭", 
    "Tierce majeure F": "A", 
    "Quarte F": "B♭", 
    "Quinte diminuée F": "C♭",
    "Quinte F": "C", 
    "Sixte mineure F": "D♭",
    "Sixte majeure F": "D", 
    "Septième mineure F": "E♭",
    "Septième majeure F": "E",

    "Seconde mineure F#": "G",
    "Seconde majeure F#": "G#",
    "Tierce mineure F#": "A", 
    "Tierce majeure F#": "A#", 
    "Quarte F#": "B", 
    "Quinte diminuée F#": "C",
    "Quinte F#": "C#", 
    "Sixte mineure F#": "D",
    "Sixte majeure F#": "D#", 
    "Septième mineure F#": "E",
    "Septième majeure F#": "E#",

    "Seconde mineure G": "A♭",
    "Seconde majeure G": "A",
    "Tierce mineure G": "B♭", 
    "Tierce majeure G": "B", 
    "Quarte G": "C", 
    "Quinte diminuée G": "D♭",
    "Quinte G": "D", 
    "Sixte mineure G": "E♭",
    "Sixte majeure G": "E", 
    "Septième mineure G": "F",
    "Septième majeure G": "F#",

    "Seconde mineure A♭": "B♭♭",
    "Seconde majeure A♭": "B♭",
    "Tierce mineure A♭": "C♭", 
    "Tierce majeure A♭": "C", 
    "Quarte A♭": "D♭", 
    "Quinte diminuée A♭": "E♭♭",
    "Quinte A♭": "E♭", 
    "Sixte mineure A♭": "F♭",
    "Sixte majeure A♭": "F", 
    "Septième mineure A♭": "G♭",
    "Septième majeure A♭": "G",

    "Seconde mineure A": "B♭",
    "Seconde majeure A": "B",
    "Tierce mineure A": "C", 
    "Tierce majeure A": "C#", 
    "Quarte A": "D", 
    "Quinte diminuée A": "E♭",
    "Quinte A": "E", 
    "Sixte mineure A": "F",
    "Sixte majeure A": "F#", 
    "Septième mineure A": "G",
    "Septième majeure A": "G#",

    "Seconde mineure B♭": "C♭",
    "Seconde majeure B♭": "C",
    "Tierce mineure B♭": "D♭", 
    "Tierce majeure B♭": "D", 
    "Quarte B♭": "E♭", 
    "Quinte diminuée B♭": "F♭",
    "Quinte B♭": "F", 
    "Sixte mineure B♭": "G♭",
    "Sixte majeure B♭": "G", 
    "Septième mineure B♭": "A♭",
    "Septième majeure B♭": "A",

    "Seconde mineure B": "C",
    "Seconde majeure B": "C#",
    "Tierce mineure B": "D", 
    "Tierce majeure B": "D#", 
    "Quarte B": "E", 
    "Quinte diminuée B": "F",
    "Quinte B": "F#", 
    "Sixte mineure B": "G",
    "Sixte majeure B": "G#", 
    "Septième mineure B": "A",
    "Septième majeure B": "A#",

    
}

REQUEST_NOTE_DICT_REVERSE = {
    "Note dont la Seconde mineure est C": "B",
    "Note dont la Seconde majeure est C": "B♭",
    "Note dont la Tierce mineure est C": "A", 
    "Note dont la Tierce majeure est C": "A♭", 
    "Note dont la Quarte est C": "G", 
    "Note dont la Quinte diminuée est C": "F#",
    "Note dont la Quinte est C": "F", 
    "Note dont la Sixte mineure est C": "E",
    "Note dont la Sixte majeure est C": "E♭", 
    "Note dont la Septième mineure est C": "D",
    "Note dont la Septième majeure est C": "D♭", 
 
    "Note dont la Seconde mineure est D♭": "C",
    "Note dont la Seconde majeure est D♭": "C♭",
    "Note dont la Tierce mineure est D♭": "B♭", 
    "Note dont la Tierce majeure est D♭": "B♭♭", 
    "Note dont la Quarte est D♭": "A♭", 
    "Note dont la Quinte diminuée est D♭": "G",
    "Note dont la Quinte est D♭": "G♭", 
    "Note dont la Sixte mineure est D♭": "F",
    "Note dont la Sixte majeure est D♭": "F♭", 
    "Note dont la Septième mineure est D♭": "E♭",
    "Note dont la Septième majeure est D♭": "E♭♭",
 
    "Note dont la Seconde mineure est D": "C#",
    "Note dont la Seconde majeure est D": "C",
    "Note dont la Tierce mineure est D": "B", 
    "Note dont la Tierce majeure est D": "B♭", 
    "Note dont la Quarte est D": "A", 
    "Note dont la Quinte diminuée est D": "G#",
    "Note dont la Quinte est D": "G", 
    "Note dont la Sixte mineure est D": "F#",
    "Note dont la Sixte majeure est D": "F", 
    "Note dont la Septième mineure est D": "E",
    "Note dont la Septième majeure est D": "E♭",
 
    "Note dont la Seconde mineure est E♭": "D",
    "Note dont la Seconde majeure est E♭": "D♭",
    "Note dont la Tierce mineure est E♭": "C", 
    "Note dont la Tierce majeure est E♭": "C♭", 
    "Note dont la Quarte est E♭": "B♭", 
    "Note dont la Quinte diminuée est E♭": "A",
    "Note dont la Quinte est E♭": "A♭", 
    "Note dont la Sixte mineure est E♭": "G",
    "Note dont la Sixte majeure est E♭": "G♭", 
    "Note dont la Septième mineure est E♭": "F",
    "Note dont la Septième majeure est E♭": "F♭", 
 
    "Note dont la Seconde mineure est E": "D#",
    "Note dont la Seconde majeure est E": "D",
    "Note dont la Tierce mineure est E": "C#", 
    "Note dont la Tierce majeure est E": "C", 
    "Note dont la Quarte est E": "B", 
    "Note dont la Quinte diminuée est E": "A#",
    "Note dont la Quinte est E": "A", 
    "Note dont la Sixte mineure est E": "G#",
    "Note dont la Sixte majeure est E": "G", 
    "Note dont la Septième mineure est E": "F#",
    "Note dont la Septième majeure est E": "F",
 
    "Note dont la Seconde mineure est F": "E",
    "Note dont la Seconde majeure est F": "E♭",
    "Note dont la Tierce mineure est F": "D", 
    "Note dont la Tierce majeure est F": "D♭", 
    "Note dont la Quarte est F": "C", 
    "Note dont la Quinte diminuée est F": "B",
    "Note dont la Quinte est F": "B♭", 
    "Note dont la Sixte mineure est F": "A",
    "Note dont la Sixte majeure est F": "A♭", 
    "Note dont la Septième mineure est F": "G",
    "Note dont la Septième majeure est F": "G♭",
 
    "Note dont la Seconde mineure est F#": "E#",
    "Note dont la Seconde majeure est F#": "E",
    "Note dont la Tierce mineure est F#": "D#", 
    "Note dont la Tierce majeure est F#": "D", 
    "Note dont la Quarte est F#": "C#", 
    "Note dont la Quinte diminuée est F#": "B#",
    "Note dont la Quinte est F#": "B", 
    "Note dont la Sixte mineure est F#": "A#",
    "Note dont la Sixte majeure est F#": "A", 
    "Note dont la Septième mineure est F#": "G#",
    "Note dont la Septième majeure est F#": "G",
 
    "Note dont la Seconde mineure est G": "F#",
    "Note dont la Seconde majeure est G": "F",
    "Note dont la Tierce mineure est G": "E", 
    "Note dont la Tierce majeure est G": "E♭", 
    "Note dont la Quarte est G": "D", 
    "Note dont la Quinte diminuée est G": "C#",
    "Note dont la Quinte est G": "C", 
    "Note dont la Sixte mineure est G": "B",
    "Note dont la Sixte majeure est G": "B♭", 
    "Note dont la Septième mineure est G": "A",
    "Note dont la Septième majeure est G": "A♭",
 
    "Note dont la Seconde mineure est A♭": "G",
    "Note dont la Seconde majeure est A♭": "G♭",
    "Note dont la Tierce mineure est A♭": "F", 
    "Note dont la Tierce majeure est A♭": "F♭", 
    "Note dont la Quarte est A♭": "E♭", 
    "Note dont la Quinte diminuée est A♭": "D",
    "Note dont la Quinte est A♭": "D♭", 
    "Note dont la Sixte mineure est A♭": "C",
    "Note dont la Sixte majeure est A♭": "C♭", 
    "Note dont la Septième mineure est A♭": "B♭",
    "Note dont la Septième majeure est A♭": "B♭♭",
 
    "Note dont la Seconde mineure est A": "G#",
    "Note dont la Seconde majeure est A": "G",
    "Note dont la Tierce mineure est A": "F#", 
    "Note dont la Tierce majeure est A": "F", 
    "Note dont la Quarte est A": "E", 
    "Note dont la Quinte diminuée est A": "D#",
    "Note dont la Quinte est A": "D", 
    "Note dont la Sixte mineure est A": "C#",
    "Note dont la Sixte majeure est A": "C", 
    "Note dont la Septième mineure est A": "B",
    "Note dont la Septième majeure est A": "B♭",
 
    "Note dont la Seconde mineure est B♭": "A",
    "Note dont la Seconde majeure est B♭": "A♭",
    "Note dont la Tierce mineure est B♭": "G", 
    "Note dont la Tierce majeure est B♭": "G♭", 
    "Note dont la Quarte est B♭": "F", 
    "Note dont la Quinte diminuée est B♭": "E",
    "Note dont la Quinte est B♭": "E♭", 
    "Note dont la Sixte mineure est B♭": "D",
    "Note dont la Sixte majeure est B♭": "D♭", 
    "Note dont la Septième mineure est B♭": "C",
    "Note dont la Septième majeure est B♭": "C♭",
 
    "Note dont la Seconde mineure est B": "A#",
    "Note dont la Seconde majeure est B": "A",
    "Note dont la Tierce mineure est B": "G#", 
    "Note dont la Tierce majeure est B": "G", 
    "Note dont la Quarte est B": "F#", 
    "Note dont la Quinte diminuée est B": "E#",
    "Note dont la Quinte est B": "E", 
    "Note dont la Sixte mineure est B": "D#",
    "Note dont la Sixte majeure est B": "D", 
    "Note dont la Septième mineure est B": "C#",
    "Note dont la Septième majeure est B": "C",

    
}