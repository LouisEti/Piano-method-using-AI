# Piano-method-using-A.I.

## Project description

This project aims to enhance your <span style="color:orange" > piano </span> and <span style="color:orange" > music theory skills </span> using artificial intelligence, specifically reinforcement learning. <br>
Using a MIDI piano (MIDI controller), this program proposes three game modes:<br>

1. **NOTES**: Respond to a request by pressing the correct piano key.
2. **WRITE**: Respond to a request by typing the answer on your computer keyboard.
3. **CHORDS**: Play the requested chord on the piano.

For all requests in each game mode, the __Artificial Intelligence__ is used to update their probability of being the next request. <br> 
The more imprecisely and slowly the user responds to a query, the more likely it is to be the next query.

````
It is by learning what we know the least that we improve the best
````


## Material and softwares required 

- A MIDI controller with all its drivers installed on your computer 
- Mircrosoft Windows 10/11 
- [Python 3.11.7](https://www.python.org/downloads/release/python-3117/)


## Instructions 

- Clone repository in your folder 
- Create a venv (with python 3.11.7) 
- Install all dependencies using ```` pip install -r requirements.txt ````
- Run ```` python piano_method.py ```` in your terminal to launch the program 
<br>


### Example for CHORDS game mode  

![Capture](https://github.com/LouisEti/Piano-method-using-AI/assets/111647076/54ba12d5-02e3-4d61-a840-1010bccfb479)