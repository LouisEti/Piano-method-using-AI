import unittest 
from chords_and_notes_dict import *

class Test_TestIncrementDecrement(unittest.TestCase):

    def test_all_values_in_dict_are_available(self):
        unique_values_note_request_dict = set(list(request_note_dict.values()))
        unique_keys_note_value_match = set(list(NOTE_VALUE_MATCH.keys()))
        unique_keys_note_eng_to_fr = set(list(NOTE_ENG_TO_FR.keys()))
        for elem in unique_values_note_request_dict:
            self.assertIn(elem, unique_keys_note_value_match, f"Element {elem} not found in NOTE_VALUE_MATCH")
            self.assertIn(elem, unique_keys_note_eng_to_fr, f"Element {elem} not found in NOTE_ENG_TO_FR")

    def test_all_values_in_dict_reverse_are_available(self):
        unique_values_note_request_dict_reverse = set(list(request_note_dict_reverse.values()))
        unique_keys_note_value_match = set(list(NOTE_VALUE_MATCH.keys()))
        unique_keys_note_eng_to_fr = set(list(NOTE_ENG_TO_FR.keys()))
        for elem in unique_values_note_request_dict_reverse:
            self.assertIn(elem, unique_keys_note_value_match, f"Element {elem} not found in NOTE_VALUE_MATCH")
            self.assertIn(elem, unique_keys_note_eng_to_fr, f"Element {elem} not found in NOTE_ENG_TO_FR")


if __name__ == '__main__':
    
    unittest.main()
    
