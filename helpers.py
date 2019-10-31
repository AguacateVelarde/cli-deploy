from pyfiglet import Figlet

def name():
    f = Figlet(font='slant', width=80)
    print(f.renderText('deploy Login'))