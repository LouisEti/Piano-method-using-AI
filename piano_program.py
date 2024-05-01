import copy
import os
import pickle
import random
import threading
import time
import tkinter as tk
from datetime import datetime
from functools import partial
from keyboard import press
from typing import Callable

import mido
import rtmidi as rt
from PIL import Image, ImageTk

from chords_and_notes_dict import *


current_path = os.getcwd()
green_keys_path = os.path.join(current_path, "Images\\green_keys")
red_keys_path = os.path.join(current_path, "Images\\red_keys")


def open_port(
    input_name: str, output_name: str
) -> tuple[mido.ports.IOPort, mido.ports.IOPort]:
    """
    Input_port: MIDI controller to send MIDI messages
    Output_port: Corresponds to the sound that the programm returns after getting MIDI message
    --> it can be no sound

    Case 1: If input and output ports are available --> open them with the names given in parameters
    Case 2: If input and output ports are already used --> close them and open them with the names
    given in parameters

    It returns the input_port and output_port
    """

    global input_port, output_port

    # if input_port and output_port are AVAILABLE
    try:
        input_port = mido.open_input(input_name)
        output_port = mido.open_output(output_name)

    # if input_port and output_port are NOT AVAILABLE
    except Exception:
        close_port(input_port, output_port)
        input_port = mido.open_input(input_name)
        output_port = mido.open_output(output_name)

    return input_port, output_port


def close_port(input_port: mido.ports.IOPort, output_port: mido.ports.IOPort) -> None:
    """
    Close input and output ports
    """
    input_port.close()
    output_port.close()


def choose_ports() -> tuple[str, str]:
    """
    Create a Tkinter window in which the input and output names are displayed on your machine

    - Select ONLY one for the input by clicking inside a checkbox in the INPUTS column
    - Select ONLY one for the ouput by clicking inside a checkbox in the OUTPUTS column

    It returns the input_name and output_name selected
    """

    def validate_checkboxes() -> None:
        """
        Retrieve the names of the input and output selected by clicking inside their checkbox
        Then it kills the Tkinter "Inputs & Outputs" window
        """

        global selected_input, selected_output

        input_index = [var.get() for var in input_vars].index(1)
        selected_input = input_options[input_index]
        output_index = [var.get() for var in output_vars].index(1)
        selected_output = output_options[output_index]

        print(f"Input selected: '{selected_input}'")
        print(f"Output selected: '{selected_output}'")

        window.destroy()

    window = tk.Tk()
    window.geometry("600x400")

    input_label = tk.Label(window, text="INPUTS", font=("Aerial", 20))
    input_label.grid(row=0, column=0, sticky="w")

    output_label = tk.Label(window, text="OUTPUTS", font=("Aerial", 20))
    output_label.grid(row=0, column=1, sticky="w")

    # Create the lists of input and output options available on your machine
    input_options = mido.get_input_names()
    output_options = mido.get_output_names()

    # Create variables to track the state of the checkboxes
    input_vars = []
    output_vars = []

    # Create checkboxes for the input options
    for i, option in enumerate(input_options):
        var = tk.IntVar()
        checkbox = tk.Checkbutton(window, text=option, variable=var)
        checkbox.grid(row=i + 1, column=0, sticky="w")
        input_vars.append(var)

    # Create checkboxes for the output options
    for i, option in enumerate(output_options):
        var = tk.IntVar()
        checkbox = tk.Checkbutton(window, text=option, variable=var)
        checkbox.grid(row=i + 1, column=1, sticky="w")
        output_vars.append(var)

    # Create the entry button to validate the checkboxes
    button = tk.Button(window, text="Validate", command=validate_checkboxes)
    button.grid(row=max(len(input_options), len(output_options)) + 1, columnspan=2)

    window.mainloop()

    return selected_input, selected_output


def check_answer_note_request_mode(function_called: Callable[[], None]) -> None:
    """
    - Check for the request_note mode, if the note value (from 0 to 127) of the key pressed is in the list of the good answers (list_notes_true_answer)
    - Save in the corresponding dictionaries (good/bad answer and time) the name of the request but don't save if two keys are pressed at the same time (max 0.1s)
    - Destroy the label of the note request widget to release memory space for next queries
    - Automatically invoke another call of the activate_function aka "request_note" function for another note interval request
    """

    global note_path, start_time_note, two_keys_pressed

    good_answer_key = list(dict_to_save.keys())[0]
    bad_answer_key = list(dict_to_save.keys())[1]
    good_time_key = list(dict_to_save.keys())[2]
    bad_time_key = list(dict_to_save.keys())[3]

    if function_called is request_note:
        if msg.type == "note_on":
            # if the 2 keys are pressed at the same time, don't save the answer time and response
            if (end_time_note - start_time_note) < 0.1:
                two_keys_pressed = True

            # if the match is correct, select green_keys folder
            elif note_value in list_notes_true_answer:
                dict_to_save[good_answer_key].append(random_note_request)
                dict_to_save[good_time_key].append(time_response_note)

                # Choose folder of green notes
                note_path = green_keys_path

            # if the match is uncorrect, select red_keys folder
            else:
                dict_to_save[bad_answer_key].append(random_note_request)
                dict_to_save[bad_time_key].append(time_response_note)

                # Choose folder of red notes
                note_path = red_keys_path

            # Delete overlay_label_note --> created in note_request function
            overlay_label_note_request.destroy()

            # Call the activate_function (should be "request_note") automatically for another request
            activate_function()


def select_key_image(note_value_midi: int) -> Image:
    """
    This function is activated in "request_note" and "chords" game modes. It display the piano key image that corresponds
    to the note played on the piano
    """

    if NOTE_VALUES_DICT[note_value_midi][1] == "upper":
        overlayed_image = Image.open(os.path.join(note_path, "upper_key.png"))
        overlayed_image = overlayed_image.resize(
            (44, 230)
        )  # resize to match top black key dimensions
    elif NOTE_VALUES_DICT[note_value_midi][1] == "mid":
        overlayed_image = Image.open(os.path.join(note_path, "mid_key.png"))
        overlayed_image = overlayed_image.resize(
            (60, 400)
        )  # resize to match mid white key dimensions
    elif NOTE_VALUES_DICT[note_value_midi][1] == "left":
        overlayed_image = Image.open(os.path.join(note_path, "left_key.png"))
        overlayed_image = overlayed_image.resize(
            (60, 400)
        )  # resize to match left white key dimensions
    elif NOTE_VALUES_DICT[note_value_midi][1] == "right":
        overlayed_image = Image.open(os.path.join(note_path, "right_key.png"))
        overlayed_image = overlayed_image.resize(
            (60, 400)
        )  # resize to match right white key dimensions

    return overlayed_image


def note_display(canvas: tk.Canvas, note_value: int) -> None:
    """
    Display the overlayed red or green notes over the piano background image when a key is pressed on MIDI controller and remove them when keys are unpressed
    The green or red notes images are chosen by calling the "check_answer_note_request_mode" function to assess if the answer is good or wrong
    """

    global overlayed_image_label

    # Create the label of the overlayed image of green and red keys that will be displayed on the background piano image
    # Add try/except module avoiding the creation of a new tk.Label at each call of the function. This prevents memory saturation
    try:
        overlayed_image_label
    except:
        overlayed_image_label = tk.Label(root)

    # The display will depend on the exercise chosen
    check_answer_note_request_mode(activate_function)

    # if two keys are pressed at the same time for the request_note game mode
    if two_keys_pressed:
        return None

    # Depending on the position of the key we play on the MIDI controller (top black key or left, mid, right white key), open the corresponding overlayed image
    overlayed_image = select_key_image(note_value)

    # Create the overlayed image
    overlayed_image = ImageTk.PhotoImage(overlayed_image)

    # Assign overlayed image to corresponding tk.Label
    overlayed_image_label.config(image=overlayed_image)
    overlayed_image_label.image = overlayed_image

    # Display the overlayed image on the canvas when key is press and delete it when key is unpressed
    if (
        note_container.count(note_value) % 2 == 1
    ):  # if note_container (list of all the note_value played) contains only one occurence of note_value (corresponding to "note_on")
        canvas.create_image(
            NOTE_VALUES_DICT[note_value][0],
            0,
            anchor=tk.NW,
            image=overlayed_image,
            tags="variable" + str(note_value),
        )
    else:  # if note_container contained two occurences of note_value (corresponding to "note_on" and "note_off")
        canvas.delete("variable" + str(note_value))


def check_answer_chords_mode() -> bool:
    """
    Check if the chords play for the "chords" game mode are correct or not. \n
    - Return False the user don't play the same amount of keys than the amount of notes of the true answer, don't save the request in dict.
    - Return False the user plays the same amount but different keys than the notes of the true answer, save bad request/time_response in dict just for "note_on"
    (because it would save twice when note_off for example after unpress the fifth key of a fourth-key chord)
    - Return True the user plays the same amount and same keys than the notes of the true answer, save good request/time_response in dict & call another request
    """

    good_answer_key = list(dict_to_save.keys())[0]
    bad_answer_key = list(dict_to_save.keys())[1]
    good_time_key = list(dict_to_save.keys())[2]
    bad_time_key = list(dict_to_save.keys())[3]

    if len(list_notes_stored_for_display) != len(list_answers_chords[0]):
        return False

    for any_lst in list_answers_chords:
        if any_lst == list_notes_stored_for_display:
            end_time_chords = time.time()
            time_response_chords = round((end_time_chords - start_time_chords), 4)

            # Save time_response and good answer in list for function_folder dict
            dict_to_save[good_time_key].append(time_response_chords)
            dict_to_save[good_answer_key].append(request_chord_text)

            return True

    if msg_type == "note_on":
        end_time_chords = time.time()
        time_response_chords = round((end_time_chords - start_time_chords), 4)

        # Save time_response and bad answer in list for function_folder dict
        dict_to_save[bad_time_key].append(time_response_chords)
        dict_to_save[bad_answer_key].append(request_chord_text)

    return False


def restart_chords() -> None:
    """
    This function is activated in the "chords" game mode. \n
    When more than 10 keys are played at the same time, delete all the overlayed images (red and green keys), re-initialize the
    deepcopy_label_widgets_for_chords dictionary and call the request_chords function for another request
    """

    global list_notes_stored_for_display

    for note in list_notes_stored_for_display:
        canvas.delete("variable" + str(note))
        list_notes_stored_for_display = []
        for key, value in deepcopy_label_widgets_for_chords.items():
            deepcopy_label_widgets_for_chords[key] = (None, None)
        request_chords()


def note_display_chords(
    list_of_dict_keys: list, note_value_midi: int, message_type_midi: str
) -> None:
    """
    This function is activated when the user presses a key in the "chords" game mode. \n
    - Check in the 'deepcopy_label_widgets_for_chords' dictionary if some values are (None, None) tuples. If there at least one, the value
    will be set to (tk.Label, note_value_midi) where the note_value_midi corresponds to the value of the key pressed.
    If all the values in the dictionary are (tk.Label, note_value_midi), it means that more than 10 keys are pressed at the same
    time ; the restart_chords function is called. \n
    - According to the nature of the answer (good/wrong), select the good key_image to overlay on the piano background. \n
    - When the user unpress a key, delete the overlayed key image and update the deepcopy_label_widgets_for_chords to (None, None)
    so we can save memory slots (instead of creating tk.Label object every time the user press or unpress a key).
        - But if ten_keys_pressed is True (meaning more than 10 keys are pressed at the same time), as the dict has been re-initialized,
        all the notes displayed are not displayed anymore but the keys are still pressed. In that case, the function does nothing and return None.
    - If the user's answer is correct, call the request_chords function for another request.

    """

    for key, value in deepcopy_label_widgets_for_chords.items():
        if value[0] is None:
            deepcopy_label_widgets_for_chords[key] = tuple(
                (tk.Label(root), note_value_midi)
            )
            overlayed_image_label_chords = deepcopy_label_widgets_for_chords[key][0]
            break

        elif value[0] is not None and key != list_of_dict_keys[-1]:
            continue

        elif value[0] is not None and key == list_of_dict_keys[-1]:
            restart_chords()
            return None

    # Depending on the position of the key we play on the MIDI controller (top black key or left, mid, right white key), open the corresponding overlayed image
    overlayed_image = select_key_image(note_value_midi)

    # Create the overlayed image
    overlayed_image = ImageTk.PhotoImage(overlayed_image)

    # Assign overlayed image to corresponding tk.Label
    overlayed_image_label_chords.config(image=overlayed_image)
    overlayed_image_label_chords.image = overlayed_image

    nature_answer_chords = check_answer_chords_mode()

    if message_type_midi == "note_on":
        canvas.create_image(
            NOTE_VALUES_DICT[note_value_midi][0],
            0,
            anchor=tk.NW,
            image=overlayed_image,
            tags="variable" + str(note_value_midi),
        )

    elif message_type_midi == "note_off" and ten_keys_pressed == False:
        canvas.delete("variable" + str(note_value_midi))
        deepcopy_label_widgets_for_chords[key][0].destroy()
        deepcopy_label_widgets_for_chords[key] = (None, None)
        value_to_change_in_dict = [
            tup[1] for tup in list(deepcopy_label_widgets_for_chords.values())
        ].index(note_value_midi)
        deepcopy_label_widgets_for_chords["label" + str(value_to_change_in_dict)][
            0
        ].destroy()
        deepcopy_label_widgets_for_chords["label" + str(value_to_change_in_dict)] = (
            None,
            None,
        )

    if nature_answer_chords == True:
        request_chords()


def handle_midi_message(msg: mido.Message, output_port) -> None:
    """
    Receive the MIDI messages from the controller and play it, depending on "note_on" or "note_off" type
    MIDI messages contain essentially:
    - Type: ("note_on", "note_off")
    - Channel: the channel of MIDI messages (from 1 to 16)
    - Note: The pitch of the note played (from 0 to 127 where "60" is the middle C note and considered as the central reference point)
    - Velocity: Volume of the note (from 0 to 127) --> "note_off" corresponds to volcity=0
    Example of MIDI message: "note_on channel=0 note=52 velocity=63"

    The sound corresponding to the key will only be delivered for key range from 36 to 83. Out of this range, there will be no display and end_time won't get call
    """

    global note_value, start_time_note, time_response_note, end_time_note, note_path, two_keys_pressed, ten_keys_pressed, msg_type

    note_container.append(msg.note)
    output_port.send(
        msg
    )  # send MIDI message through the specified MIDI output port (i.e. output_port in this case) --> make the sound if "note_on" and stop the sound if "note_off"
    note_value = msg.note

    if not display_key_pressed:
        pass

    elif msg.note >= 36 and msg.note <= 83:
        if activate_function is request_note:
            # Set the variable two_keys_pressed to False
            two_keys_pressed = False
            # Save time_response in variable and add to list later as we don't know as this step if the answer is correct or wrong
            end_time_note = time.time()
            time_response_note = round((end_time_note - start_time_note), 4)

            # Display note on virtual piano
            note_display(canvas, note_value)

        elif activate_function is chords:
            ten_keys_pressed = False
            msg_type = msg.type
            if msg_type == "note_on":
                list_notes_stored_for_display.append(note_value)
                list_notes_stored_for_display.sort()

                if any(note_value in sublist for sublist in list_answers_chords):
                    note_path = green_keys_path
                else:
                    note_path = red_keys_path

                note_display_chords(label_widgets_for_chords_keys, note_value, msg_type)

            elif msg_type == "note_off" and note_value in list_notes_stored_for_display:
                list_notes_stored_for_display.remove(note_value)

                note_display_chords(label_widgets_for_chords_keys, note_value, msg_type)

            elif (
                msg_type == "note_off"
                and note_value not in list_notes_stored_for_display
            ):
                ten_keys_pressed = True
                pass

    elif msg.note < 36 and msg.note > 83:
        out_of_scale_label = tk.Label(
            root,
            text="ERROR !\nNote out of range, change octave",
            font=("Aerial", 20),
            fg="blue",
        )
        out_of_scale_label.place(x=1000, y=460)
        root.after(1200, out_of_scale_label.destroy)


def process_midi_messages(input_port: mido) -> None:
    """
    Process the MIDI message function when a key on the controller is pressed("note_on") and unpressed ("note_off")
    This function is the threaded function.\n
    The while loop allows stopping the thread function once the session ends (closing the tkinter window).\n
    The time.sleep(0.001) command reduce charge of CPU caused by the "while" loop
    """

    global note_container, msg

    note_container = []
    while session_break == False:
        for msg in input_port.iter_pending():
            if msg.type == "note_on" or msg.type == "note_off":
                handle_midi_message(msg, output_port)
            else:
                pass
        time.sleep(0.001)  # Sleep for 10 milliseconds (adjust as needed)


def start_midi_processing(input_port: mido) -> None:
    """
    Enable the function "process_midi_messages" to be threaded
    As this function contains a "for loop" of midi messages input, it is endless. But we need to access also to the "root.mainloop()" event. So we thread this function
    """
    midi_thread = threading.Thread(target=process_midi_messages, args=(input_port,))
    midi_thread.start()


def request_note() -> None:
    """
    Request a interval from a note. The user should answer by pressing the key on his MIDI controller they believe is the correct answer
    Example --> Request = "Minor seventh of G" --> User should press an F key on his piano keyboard

    Compute the response time starting from the call of this function
    """

    global display_key_pressed, overlay_label_note_request, start_time_note, list_notes_true_answer, random_note_request, dict_to_save

    # Set the variable 'display_key_pressed' to True so that every time a note is pressed on the MIDI controller, the corresponding note on the virtual piano is highlighted
    display_key_pressed = True

    # Pick random interval request from a base note
    random_note_request = random.choice(list(REQUEST_NOTE_DICT.keys()))

    # Get the corresponding value
    note_answer = REQUEST_NOTE_DICT[random_note_request]

    # Select the corresponding true answer
    list_notes_true_answer = NOTE_VALUE_MATCH[note_answer]

    # Create the label where the note requests will be displayed
    overlay_label_note_request = tk.Label(root)
    overlay_label_note_request.place(x=650, y=450)
    overlay_label_note_request.config(text=random_note_request, font=("Arial", 20))

    # Start time calculation for response_time value
    start_time_note = time.time()


def nature_answer(message: str) -> None:
    """
    This function is activated during the check_answer_write_mode function in the write game mode.
    It displays the message parameter in the color_foreground_write color during 1200 ms (=2s).
    It deletes the content of the entry widget
    """

    global answer_wrote_label

    answer_wrote_label = message
    answer_wrote_label = tk.Label(
        root, text=message, font=("Aerial", 20), fg=color_foreground_write
    )
    answer_wrote_label.place(x=1050, y=498)
    root.after(1200, answer_wrote_label.destroy)  # it's in ms (1200ms = 2s)
    entry_widget.delete(0, "end")


def check_answer_write_mode(event: tk.Event) -> None:
    """
    This function is activated during "write" game mode. When the game mode is paused ('escape' button) nothing happens.
    It compares the answer of the request and the user's answer when the latter presses 'Enter' key.
    It loads the corresponding dict of the game mode and sub-mode chosen

    Five possible scenarios:
    1) When user's response is the correct answer
    2) When user's response is valid but is not the correct answer
    3) When user's response is empty/blank
    4) When user's response is not a valid response (typo) and number of successive typo is 0
    5) When user's response is not a valid response (typo) and number of successive typo is more than 0

    Parameters:
    - event (tk.Event): KeyPress, KeyRelease

    Variables description:
    - frozen_time_typo_error (Bool): True if the user make a typo, False otherwise
    - typo_count (int): Successive count of typo
    - time_response_typo_error (float): When the user make a typo, save the time of its answer
    """

    global color_foreground_write, frozen_time_typo_error, time_response_typo_error, typo_count

    if escape_clicked == False:
        answer_wrote_by_user = entry_widget.get()
        end_time_write = time.time()
        time_response_write = round(
            ((end_time_write - start_time_write) - chrono_elapsed_time), 4
        )

        good_answer = list(dict_to_save.keys())[0]
        bad_answer = list(dict_to_save.keys())[1]
        good_time = list(dict_to_save.keys())[2]
        bad_time = list(dict_to_save.keys())[3]

        # Scenrario #1
        if answer_wrote_by_user == answer_write_request_function:
            color_foreground_write = "green"
            nature_answer("Good answer")
            request_label_write.config(text="")

            if frozen_time_typo_error == False:
                dict_to_save[good_time].append(time_response_write)
                dict_to_save[good_answer].append(request_write)

            elif frozen_time_typo_error == True:
                dict_to_save[good_time].append(time_response_typo_error)
                dict_to_save[good_answer].append(request_write)

            # Another request
            write_request()

        # Scenrario #2
        elif (
            answer_wrote_by_user != answer_write_request_function
            and answer_wrote_by_user in set(NOTE_ENG_TO_FR.values())
        ):
            color_foreground_write = "red"
            nature_answer("Wrong answer")
            request_label_write.config(text="")

            if frozen_time_typo_error == False:
                dict_to_save[bad_time].append(time_response_write)
                dict_to_save[bad_answer].append(request_write)

            elif frozen_time_typo_error == True:
                dict_to_save[bad_time].append(time_response_typo_error)
                dict_to_save[bad_answer].append(request_write)

            # Another request
            write_request()

        # Scenrario #3
        elif answer_wrote_by_user == "":
            return None

        # Scenrario #4
        elif (
            answer_wrote_by_user != answer_write_request_function
            and answer_wrote_by_user not in set(NOTE_ENG_TO_FR.values())
            and typo_count == 0
        ):
            color_foreground_write = "blue"
            nature_answer("Error typing. Rewrite the answer")
            time_response_typo_error = round(
                ((end_time_write - start_time_write) - chrono_elapsed_time), 4
            )
            frozen_time_typo_error = True
            typo_count += 1

        # Scenrario #5
        elif (
            answer_wrote_by_user != answer_write_request_function
            and answer_wrote_by_user in set(NOTE_ENG_TO_FR.values())
            and typo_count > 0
        ):
            color_foreground_write = "blue"
            nature_answer("Error typing. Rewrite the answer")

    elif escape_clicked == True:
        return None


def write_request() -> None:
    """
    This function select a request for the sub game mode chosen ("normal" or "reverse") and select the true corresponding answer
    Start the time for time_response computation

    Some variables are defined:
    - frozen_time_typo_error (Bool): Set to False, it is associated with a user typing error
    - typo_count (int): Set to 0, it counts the successive number of times the user makes a typing error
    - escape_clicked (Bool): Set to False, this variable is employed when the user presses 'escape' key
    - chrono_elapsed_time (int): Set to 0, it corresponds to the time elapsed between the moment the 'escape' key is pressed to pause and
    the moment the 'F1' key is pressed to unpause the game mode
    """

    global start_time_write, frozen_time_typo_error, typo_count, chrono_elapsed_time, escape_clicked, answer_write_request_function, request_write

    frozen_time_typo_error = False
    typo_count = 0
    escape_clicked = False
    chrono_elapsed_time = 0

    if exercise_type == "normal":
        request_write = random.choice(list(REQUEST_NOTE_DICT.keys()))
        answer_write_request_function = NOTE_ENG_TO_FR[REQUEST_NOTE_DICT[request_write]]

    elif exercise_type == "reverse":
        request_write = random.choice(list(REQUEST_NOTE_DICT_REVERSE.keys()))
        answer_write_request_function = NOTE_ENG_TO_FR[
            REQUEST_NOTE_DICT_REVERSE[request_write]
        ]

    request_label_write.config(text=request_write, font=("Arial", 20))
    start_time_write = time.time()


def handle_f1(event: tk.Event) -> None:
    """
    This function is activated during write game mode, when the 'F1' key is pressed during a pause ('escape' button). Unpause, re-activate all the widgets of the root
    and calculate the time duration of the pause.
    If 'F1' key is pressed outside of the pause event, nothing happens

    Parameters:
    event (tk.Event): KeyPress, KeyRelease

    Variables:
    end_chrono_break (Bool): get the time that corresponds to the end of the pause to calculate the chrono_elapsed_time variable
    """

    global end_chrono_break, chrono_elapsed_time, escape_clicked

    if escape_clicked:
        end_chrono_break = time.time()
        chrono_elapsed_time += end_chrono_break - start_chrono_break

        # Set background tkinter window to default
        root.config(bg="SystemButtonFace")

        for widget in root.winfo_children():
            # Set all the root widgets to "normal" state
            widget.configure(state="normal")

        unpause_button.place_forget()
        escape_label.place_forget()

        escape_clicked = False

    else:
        return None


def handle_escape(event: tk.Event) -> None:
    """
    This function is activated during write game mode, when the 'escape' key is pressed. Pause the time for the time_response variable and disable all the widgets.
    Create the unpause_button. Clicked on it or press the 'F1' key to unpause and re-activate all the widgets.
    If the 'escape' button is already pressed, nothing happens

    Parameters:
    event (tk.Event): KeyPress, KeyRelease

    Variables:
    start_chrono_break (Bool): Start to compute the time of the pause
    """

    global unpause_button, escape_label, start_chrono_break, escape_clicked

    if escape_clicked == False:
        escape_label = tk.Label(
            root,
            text='PRESS F1 TO UNPAUSE\n OR \n CLICK THE BUTTON "UNPAUSE"',
            height=5,
            bg="grey",
            fg="blue",
            font=("Aeria", 20),
        )
        escape_label.place(x=40, y=420)

        unpause_button = tk.Button(
            root,
            text="UNPAUSE",
            width=20,
            height=4,
            font=("Aerial", 20),
            command=partial(handle_f1, event),
        )
        unpause_button.place(x=1100, y=420)

        # Grey the background tkinter window
        root.config(bg="grey")

        for widget in root.winfo_children():
            # Disable all the widgets that are not the unpause_button and the escape_label message
            if widget != unpause_button and widget != escape_label:
                widget.configure(state="disabled")

        start_chrono_break = time.time()
        escape_clicked = True

    else:
        return None


def write(**kwargs: dict) -> None:
    """
    This function activate the write game mode. \n
    Load the dict for saving purpose corresponding to the sub-mode ("normal" or "reverse") and activate the corresponding widgets

    Parmeters:
    **kwargs (dict): the corresponding value is the exercise_type ("reverse" or "normal")
    """

    global entry_widget, request_label_write, activate_function, exercise_type, dict_to_save, quit_button, next_button

    if "exercise_type" in kwargs:
        exercise_type = kwargs["exercise_type"]
        dict_to_save = load_dict_to_save(activate_function_for_save="write")
        reverse_button.place_forget()
        normal_button.place_forget()

    # Create quit button
    quit_button = tk.Button(root, text="QUIT", height=3, width=12, command=quit)
    quit_button.place(x=350, y=500)

    # Create Next button
    next_button = tk.Button(root, text="NEXT", height=3, width=12, command=next)
    next_button.place(x=350, y=440)

    # Create label to display note_interval requested
    request_label_write = tk.Label(root)
    request_label_write.place(x=780, y=450, anchor="center")

    # Create Entry widget to write answers
    entry_widget = tk.Entry(root, width=30, font=("Aerial", 20), justify="center")
    entry_widget.place(x=560, y=500)
    entry_widget.bind("<Return>", check_answer_write_mode)
    entry_widget.focus_set()  # Can automatically answer in the entry window without having to click inside the window

    # pause_widget = tk.Frame(root, width=0, height=0)
    root.bind("<Escape>", handle_escape)
    root.bind("<F1>", handle_f1)

    write_request()


def inversion_chords(inversion_name: str):
    """
    Function for inversion mode

    FUNCTION NOT CORRECT FOR THE MOMENT! DON'T USE IT !!
    """
    if inversion_name == "R2":
        for i in range(1, len(notes_intervals_associated)):
            notes_intervals_associated[i] = (
                notes_intervals_associated[i] + notes_intervals_associated[i - 1]
            )  # to know position of each note in scale
        for i in range(1):
            notes_intervals_associated.insert(
                len(notes_intervals_associated), notes_intervals_associated[0] + 12
            )  # For inversion notes, change their index in list and add an octave (+12) to know their new position in the scale
            notes_intervals_associated.pop(0)

    elif inversion_name == "R3":
        for i in range(1, len(notes_intervals_associated)):
            notes_intervals_associated[i] = (
                notes_intervals_associated[i] + notes_intervals_associated[i - 1]
            )  # to know position of each note in scale
        for i in range(2):
            notes_intervals_associated.insert(
                len(notes_intervals_associated), notes_intervals_associated[0] + 12
            )  # For inversion notes, change their index in list and add an octave (+12) to know their new position in the scale
            notes_intervals_associated.pop(0)

    elif inversion_name == "R4":
        for i in range(1, len(notes_intervals_associated)):
            notes_intervals_associated[i] = (
                notes_intervals_associated[i] + notes_intervals_associated[i - 1]
            )  # to know position of each note in scale
        for i in range(3):
            notes_intervals_associated.insert(
                len(notes_intervals_associated), notes_intervals_associated[0] + 12
            )  # For inversion notes, change their index in list and add an octave (+12) to know their new position in the scale
            notes_intervals_associated.pop(0)

    elif inversion_name == "R1":
        for i in range(1, len(notes_intervals_associated)):
            notes_intervals_associated[i] = (
                notes_intervals_associated[i] + notes_intervals_associated[i - 1]
            )  # to know position of each note in scale

    return notes_intervals_associated


def notes_in_chord() -> None:
    """
    This function is activated within the "chords" game mode.\n
    - From the list whose contain the intervals of the chord picked, calculate and define all the lists of correct answers.
    There are multiple lists as there are multiple octaves. Each list is composed of correct key values
    - If inversion_name is not None, call the inversion_chords function to rearrange the correct answers lists.
    - Update the tk.Label of the request with the good text and start the time for time_response
    """

    global list_answers_chords, start_time_chords, request_chord_text, notes_intervals_associated, request_chord_label

    list_answers_chords = []

    if inversion_name:
        notes_intervals_associated = inversion_chords(inversion_name)

    for i in [36, 48, 60]:
        list_answers_possible = []
        answer = i + random_note_key_chords
        for index_list in range(len(notes_intervals_associated)):
            answer += notes_intervals_associated[index_list]
            if answer >= 36 and answer <= 83:
                list_answers_possible.append(answer)
            else:
                break
        if len(list_answers_possible) == len(notes_intervals_associated):
            list_answers_chords.append(list_answers_possible)

    # Display the request in tkinter Label
    if inversion_name:
        request_chord_text = random_note_chords + random_chord + " " + inversion_name
    else:
        request_chord_text = random_note_chords + random_chord

    request_chord_label.config(text=request_chord_text, font=("Arial", 20))

    # Start time counting
    start_time_chords = time.time()


def request_chords() -> None:
    """
    This function is activated in the "chords" game mode. \n
    - Pick random chord to query and select the list corresponding to each interval of notes within the chord
    - Activate/deactivate the inversion mode (not activated for now)
    """

    global random_note_key_chords, random_note_chords, random_chord, notes_intervals_associated, inversion_name

    # Pick random chords
    random_note_key_chords = random.choice(list(MUSIC_NOTES.keys()))
    random_note_chords = MUSIC_NOTES[random_note_key_chords]
    if type(random_note_chords) is tuple:
        random_note_chords = random.choice(random_note_chords)

    # Pick random chords and notes intervals associated
    random_chord = random.choice(list(NOTES_INTERVALS_FOR_CHORDS.keys()))
    notes_intervals_associated = NOTES_INTERVALS_FOR_CHORDS[
        random_chord
    ].copy()  # Must add copy function otherwise when I change the variable, I also change the dict as this is a list

    # Inversion mode
    inversion_name = None
    # inversion_name = random.choice(INVERSIONS)

    notes_in_chord()


def chords(**kwargs: dict) -> None:
    """
    This function is activated when the user choose the "chords" game mode.\n
    - Select "hand_exercise" (left_hand or right_hand) if in kwargs and load the corresponding dict for saving purposes
    - Load some list and dict for the game mode
    - Create som buttons and place_forget some too
    - Call the request_chords function for request a chord
    """

    global quit_button, next_button, request_chord_label, deepcopy_label_widgets_for_chords, label_widgets_for_chords_keys
    global list_notes_stored_for_display, hand_exercise, dict_to_save, display_key_pressed

    if "hand_exercise" in kwargs:
        hand_exercise = kwargs["hand_exercise"]

    if "activate_function_for_save" in kwargs:
        # print(kwargs["activate_function_for_save"])
        dict_to_save = load_dict_to_save(
            activate_function_for_save=kwargs["activate_function_for_save"]
        )

    # All keys of the LABEL_WIDGETS_FOR_CHORDS dict for handle_midi_message
    label_widgets_for_chords_keys = list(LABEL_WIDGETS_FOR_CHORDS.keys())

    list_notes_stored_for_display = []
    deepcopy_label_widgets_for_chords = copy.deepcopy(LABEL_WIDGETS_FOR_CHORDS)
    left_hand_button.place_forget()
    right_hand_button.place_forget()

    # Create quit button
    quit_button = tk.Button(root, text="QUIT", height=3, width=12, command=quit)
    quit_button.place(x=350, y=500)

    # Create next button
    next_button = tk.Button(root, text="NEXT", height=3, width=12, command=next)
    next_button.place(x=350, y=440)

    # Create label for request chord
    request_chord_label = tk.Label(root)
    request_chord_label.place(x=780, y=500, anchor="center")

    # Enable display_note (in handle_midi_message function)
    display_key_pressed = True

    request_chords()


def quit() -> None:
    """
    This function is activated when the user press the 'quit' button.\n
    - Re-arrange the widgets of the previous game mode (forget them) and call the initialize_buttons function.\n
    - Synchronize the dict_to_save with the session_dict.\n
    - Call the save_dict function to save the dict_to_save
    """

    global quit_button_pressed

    quit_button_pressed = True
    quit_button.place_forget()
    next_button.place_forget()
    datetime_name = datetime.now().strftime("%Y_%m_%d_%H%M%S")
    synchronize_dict(dict_session, dict_to_save)

    if activate_function is request_note:
        overlay_label_note_request.destroy()

        # If not all the lists are not empty (= if at least one of the lists in not empty), save the dict
        if not all(not bool(lst) for lst in dict_to_save.values()):
            save_dict(dict_to_save, "Recorded\\request_note_function", datetime_name)

    elif activate_function is write:
        entry_widget.destroy()
        request_label_write.destroy()

        # If not all the lists are not empty (= if at least one of the lists in not empty), save the dict
        if not all(not bool(lst) for lst in dict_to_save.values()):
            if exercise_type == "normal":
                save_dict(
                    dict_to_save, "Recorded\\write_function", "normal", datetime_name
                )
            elif exercise_type == "reverse":
                save_dict(
                    dict_to_save, "Recorded\\write_function", "reverse", datetime_name
                )

    elif activate_function is chords:
        request_chord_label.destroy()

        # If not all the lists are not empty (= if at least one of the lists in not empty), save the dict
        if not all(not bool(lst) for lst in dict_to_save.values()):
            save_dict(
                dict_to_save,
                "Recorded\\chords_function",
                f"{hand_exercise}",
                datetime_name,
            )

    initialize_buttons()


def next() -> None:
    """
    Function associated with next_button.
    For each game mode, destroy/forget the corresponding widgets and call the game mode chosen again
    """

    if activate_function is request_note:
        overlay_label_note_request.destroy()
        activate_function()

    elif activate_function is write:
        entry_widget.destroy()
        request_label_write.destroy()
        quit_button.place_forget()
        next_button.place_forget()
        activate_function()

    elif activate_function is chords:
        quit_button.place_forget()
        next_button.place_forget()
        request_chord_label.destroy()
        activate_function(hand_exercise=hand_exercise)


def load_dict_to_save(**kwargs) -> dict:
    """
    Return the dict with the keys that correspond to the game mode chosen
    """
    global dict_function

    if kwargs["activate_function_for_save"] == "request_note":
        dict_function = {
            "list_answer_good_note": [],
            "list_answer_bad_note": [],
            "list_time_good_note": [],
            "list_time_bad_note": [],
        }

    elif kwargs["activate_function_for_save"] == "write":
        if exercise_type == "normal":
            dict_function = {
                "list_answer_good_write_normal": [],
                "list_answer_bad_write_normal": [],
                "list_time_good_write_normal": [],
                "list_time_bad_write_normal": [],
            }

        elif exercise_type == "reverse":
            dict_function = {
                "list_answer_good_write_reverse": [],
                "list_answer_bad_write_reverse": [],
                "list_time_good_write_reverse": [],
                "list_time_bad_write_reverse": [],
            }

    elif kwargs["activate_function_for_save"] == "chords":
        if hand_exercise == "right_hand":
            dict_function = {
                "list_answer_good_chord_right": [],
                "list_answer_bad_chord_right": [],
                "list_time_good_chord_right": [],
                "list_time_bad_chord_right": [],
            }
        elif hand_exercise == "left_hand":
            dict_function = {
                "list_answer_good_chord_left": [],
                "list_answer_bad_chord_left": [],
                "list_time_good_chord_left": [],
                "list_time_bad_chord_left": [],
            }

    return dict_function


def synchronize_dict(dict_to_sync: dict, small_dict: dict) -> None:
    """
    For each element in the list of each key of the small_dict (in general the dict_to_save), add those elements in the list of the corresponding
    key in the dict_to_sync (in general the session_dict)

    This function allows all the game mode good/bad answers and good/bad time_response to be added in the session_dict and get all the results of the session.
    Everytime a game mode is chosen, the dict_to_save is reset
    """

    for key in small_dict.keys():
        for element in small_dict[key]:
            dict_to_sync[key].append(element)


def save_dict(dict, *args: str) -> None:
    """
    Save the dict parameter into a pickle file in the folder path chosen by args

    The *args parameter refers to the fact that some dict would be saved in folder of folder.
    Example: For the "write" game mode and "reverse" sub-mode, we want to save the dict in a pickle file of the ./write_function/reverse folder
    """

    filename_entire_path = os.path.join(
        current_path, *[args[i] for i in range(len(args))]
    )
    with open(filename_entire_path, "wb") as handle:
        pickle.dump(dict, handle)


def button_clicked(button_name) -> None:
    """
    - Activate the game mode you have chosen
    - Set quit_button_pressed to False indicating that you don't quit the game mode for now (for dict saving purpose)
    - Initialization of new buttons for sub modes in the game mode you have chosen
    """

    global quit_button, next_button, activate_function, dict_to_save, quit_button_pressed, normal_button, reverse_button, left_hand_button, right_hand_button

    # Set quit_button to False, meaning that quit_button has not been pressed yet (for dict saving purpose)
    quit_button_pressed = False

    activate_function = button_name

    # Delete temporary the 3 game modes buttons (still in the memory space)
    note_button.place_forget()
    write_button.place_forget()
    chords_button.place_forget()

    if activate_function is request_note:
        # Load the dict of answers for saving purpose
        dict_to_save = load_dict_to_save(activate_function_for_save="request_note")

        quit_button = tk.Button(root, text="QUIT", height=3, width=12, command=quit)
        quit_button.place(x=350, y=500)

        next_button = tk.Button(root, text="NEXT", height=3, width=12, command=next)
        next_button.place(x=350, y=440)

        # Run the request_note function
        button_name()

    elif activate_function is write:
        # Create button for left hand exercise
        normal_button = tk.Button(
            root,
            text="NORMAL",
            height=5,
            width=15,
            command=partial(write, exercise_type="normal"),
        )
        normal_button.place(x=550, y=450)

        # Create button for right hand exercise
        reverse_button = tk.Button(
            root,
            text="REVERSE",
            height=5,
            width=15,
            command=partial(write, exercise_type="reverse"),
        )
        reverse_button.place(x=750, y=450)

    elif activate_function is chords:
        # Create button for left hand exercise
        left_hand_button = tk.Button(
            root,
            text="LEFT HAND",
            height=5,
            width=15,
            command=partial(
                chords, hand_exercise="left_hand", activate_function_for_save="chords"
            ),
        )
        left_hand_button.place(x=550, y=450)

        # Create button for right hand exercise
        right_hand_button = tk.Button(
            root,
            text="RIGHT HAND",
            height=5,
            width=15,
            command=partial(
                chords, hand_exercise="right_hand", activate_function_for_save="chords"
            ),
        )
        right_hand_button.place(x=750, y=450)


def initialize_buttons() -> None:
    """
    Initialize 3 buttons on the root tkinter window corresponding to the 3 game modes availbable:
    - Note button: Play notes on the piano controller that corresponds to the interval requested
    - Write button: Write the note with your keyboard that corresponds to the interval requested
    - Chords button: Play the chords on the piano controller that have been requested

    Initialize the display_key_pressed variable to False, which indicates that while none of the game modes has been selected, you can play on your piano controller and get the
    sound corresponding piano key but not the image of the piano key pressed on the piano background image
    """

    global note_button, display_key_pressed, write_button, chords_button

    # Create a Button for "request_note" game mode
    note_button = tk.Button(
        root,
        text="NOTES",
        height=3,
        width=12,
        command=partial(button_clicked, request_note),
    )
    note_button.place(x=0, y=410)

    # Create a Button for "write" game mode
    write_button = tk.Button(
        root, text="WRITE", height=3, width=12, command=partial(button_clicked, write)
    )
    write_button.place(x=0, y=470)

    # Create a Button for "chords" game mode
    chords_button = tk.Button(
        root, text="CHORDS", height=3, width=12, command=partial(button_clicked, chords)
    )
    chords_button.place(x=0, y=530)

    # While the note_button is not pressed, we will just hear notes from controller, not the visual
    display_key_pressed = False


def main(width=1600, height=400) -> None:
    """
    1) Open the input and output ports
    2) Display the virtual piano keyboard window with Tkinter
    3) Run the initialize_buttons function which initialized the different "game" modes of the program --> Click on one of those to play the mode
    4) Run the threading function to receive/send MIDI messages while the background virtual piano is running

    """

    global canvas, root, output_port, input_port

    # Open ouput and input port
    input_chosen, output_chosen = choose_ports()
    input_port, output_port = open_port(input_chosen, output_chosen)

    # Initialize the Tkinter window
    root = tk.Tk()
    root.geometry("1600x600")

    # Load the piano background image and resize it
    background_image = Image.open("Images\\piano.png")
    background_image = background_image.resize((width, height))
    background_image = ImageTk.PhotoImage(background_image)

    # Create the canvas with the background piano image inside the Tkinter window
    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack()
    canvas.create_image(0, 0, image=background_image, anchor=tk.NW)

    # Intialize buttons
    initialize_buttons()

    # Thread the MIDI messages tasks
    start_midi_processing(input_port)

    root.mainloop()


if __name__ == "__main__":
    session_break = False
    dict_session = copy.deepcopy(dict_regroup_lists)
    main()
    # Del the overlayed_image_label widget if it exists or a threading error would be raised because the overlayed_image_label is a global variable in the display_note function
    try:
        del overlayed_image_label
    except:
        pass
    session_break = True
    close_port(input_port, output_port)
    datetime_name = datetime.now().strftime("%Y_%m_%d_%H%M%S")
    if quit_button_pressed == False:
        if activate_function is request_note:
            # If not all the lists are not empty (= if at least one of the lists in not empty), save the dict
            if not all(not bool(lst) for lst in dict_to_save.values()):
                save_dict(
                    dict_to_save, "Recorded\\request_note_function", datetime_name
                )
                synchronize_dict(dict_session, dict_to_save)

        elif activate_function is write:
            # If not all the lists are not empty (= if at least one of the lists in not empty), save the dict
            if not all(not bool(lst) for lst in dict_to_save.values()):
                save_dict(
                    dict_to_save,
                    "Recorded\\write_function",
                    f"{exercise_type}",
                    datetime_name,
                )
                synchronize_dict(dict_session, dict_to_save)

        elif activate_function is chords:
            # If not all the lists are not empty (= if at least one of the lists in not empty), save the dict
            if not all(not bool(lst) for lst in dict_to_save.values()):
                save_dict(
                    dict_to_save,
                    "Recorded\\chords_function",
                    f"{hand_exercise}",
                    datetime_name,
                )
                synchronize_dict(dict_session, dict_to_save)

    if not all(not bool(lst) for lst in dict_session.values()):
        save_dict(
            dict_session,
            "Recorded\\session_file_saved",
            datetime_name + "_recap_session",
        )  # If not all the lists are not empty (= if at least one of the lists in not empty), save the dict
