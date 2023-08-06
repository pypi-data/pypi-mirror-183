from time import sleep as _sleep;from os import system as _sys, name as _name


class Sys:

    """
    functions -> 6:
        Init()       |      Initialize the command prompt to print colors
        Clear()      |      Clear the command prompt
        Title()      |      [!]Only for Windows systems: set the title of the command prompt
        Type()       |      Print slowly a string, it can use with :input(), Col.
        HideCursor() |      Hide the cursor (the white thing that blinking in the command prompt)
        ShowCursor() |      Show the cursor (the white thing that blinking in the command prompt)
    """

    def Init() -> None:
        _sys("")

    def Title(content: str) -> None:
        if _name == 'nt':
            return _sys(f"title {content}")
    def Clear() -> None:
        if _name == 'nt':
            return _sys("cls")
        else:
            return _sys("clear")

    def Type(text: str, cursor: bool = True, speed: float or int = 0.00004, new_line: bool = False) -> str:
        if cursor:
            Sys.HideCursor()
        
        for i in text:
            print(i, end="", flush=True)
            _sleep(speed)

        if new_line:
            print()

        if cursor:
            Sys.ShowCursor()

        return "" # to concatenate str 

    def HideCursor() -> str:
        print("\033[?25l", end='')
        
    def ShowCursor() -> str:
        print("\033[?25h", end='')


class Textspace:
    def getspace(text: str) -> int (1 or 0):
        return len(text) - len(text.lstrip())

class Dynamic:
    
    """
    variables -> 43:
        Dynamic Colors | All the colors to do gradient
        reset          | Reset the command prompt color with white
    """

    black_to_white = ["/;/;/"]
    black_to_red = ["/;0;0"]
    black_to_green = ["0;/;0"]
    black_to_blue = ["0;0;/"]
    black_to_cyan = ["0;/;/"]
    black_to_purple = ["/;0;/"]
    black_to_yellow = ["/;/;0"]

    blue_to_black = ["0;0;c"]
    blue_to_white = ["/;/;255"]
    blue_to_cyan = ["0;/;255"]
    blue_to_purple = ["/;0;255"]
    blue_to_red = ['240;0;10', '230;0;20', '220;0;30', '210;0;40', '200;0;50', '190;0;60', '180;0;70', '170;0;80', '160;0;90', '150;0;100', '140;0;110', '130;0;120', '120;0;130', '110;0;140', '100;0;150', '90;0;160', '80;0;170', '70;0;180', '60;0;190', '50;0;200', '40;0;210', '30;0;220', '20;0;230', '10;0;240','10;0;240', '20;0;230', '30;0;220', '40;0;210', '50;0;200', '60;0;190', '70;0;180', '80;0;170', '90;0;160', '100;0;150', '110;0;140', '120;0;130', '130;0;120', '140;0;110', '150;0;100', '160;0;90', '170;0;80', '180;0;70', '190;0;60', '200;0;50', '210;0;40', '220;0;30', '230;0;20', '240;0;10', '240;0;10', '230;0;20', '220;0;30', '210;0;40', '200;0;50', '190;0;60', '180;0;70', '170;0;80', '160;0;90', '150;0;100', '140;0;110', '130;0;120', '120;0;130', '110;0;140', '100;0;150', '90;0;160', '80;0;170', '70;0;180', '60;0;190', '50;0;200', '40;0;210', '30;0;220', '20;0;230', '10;0;240']

    cyan_to_green = ["0;255;c"]
    cyan_to_blue = ["0;c;255"]
    cyan_to_white = ["/;255;255"]
    cyan_to_black = ["0;c;c"]
    cyan_to_purple = ['10;230;240', '20;220;240', '30;210;240', '40;200;240', '50;190;240', '60;180;240', '70;170;240', '80;160;240', '90;150;240', '100;140;240', '110;130;240', '120;120;240', '130;110;240', '140;100;240', '150;90;240', '160;80;240', '170;70;240', '180;60;240', '190;50;240', '200;40;240', '210;30;240', '220;20;240', '230;10;240', '240;0;240','240;0;240', '230;10;240', '220;20;240', '210;30;240', '200;40;240', '190;50;240', '180;60;240', '170;70;240', '160;80;240', '150;90;240', '140;100;240', '130;110;240', '120;120;240', '110;130;240', '100;140;240', '90;150;240', '80;160;240', '70;170;240', '60;180;240', '50;190;240', '40;200;240', '30;210;240', '20;220;240', '10;230;240']

    green_to_black = ["0;c;0"]
    green_to_white = ["/;255;/"]
    green_to_yellow = ["/;255;0"]
    green_to_cyan = ["0;255;/"]

    purple_to_red = ["255;0;c"]
    purple_to_blue = ["c;0;255"]
    purple_to_white = ["255;/;255"]
    purple_to_black = ["c;0:c"]
    purple_to_cyan = ['240;0;240', '230;10;240', '220;20;240', '210;30;240', '200;40;240', '190;50;240', '180;60;240', '170;70;240', '160;80;240', '150;90;240', '140;100;240', '130;110;240', '120;120;240', '110;130;240', '100;140;240', '90;150;240', '80;160;240', '70;170;240', '60;180;240', '50;190;240', '40;200;240', '30;210;240', '20;220;240', '10;230;240','10;230;240', '20;220;240', '30;210;240', '40;200;240', '50;190;240', '60;180;240', '70;170;240', '80;160;240', '90;150;240', '100;140;240', '110;130;240', '120;120;240', '130;110;240', '140;100;240', '150;90;240', '160;80;240', '170;70;240', '180;60;240', '190;50;240', '200;40;240', '210;30;240', '220;20;240', '230;10;240', '240;0;240']
    
    red_to_black = ["c;0;0"]
    red_to_white = ["255;/;/"]
    red_to_yellow = ["255;/;0"]
    red_to_purple = ["255;0;/"]
    red_to_blue = ['240;0;10', '230;0;20', '220;0;30', '210;0;40', '200;0;50', '190;0;60', '180;0;70', '170;0;80', '160;0;90', '150;0;100', '140;0;110', '130;0;120', '120;0;130', '110;0;140', '100;0;150', '90;0;160', '80;0;170', '70;0;180', '60;0;190', '50;0;200', '40;0;210', '30;0;220', '20;0;230', '10;0;240','10;0;240', '20;0;230', '30;0;220', '40;0;210', '50;0;200', '60;0;190', '70;0;180', '80;0;170', '90;0;160', '100;0;150', '110;0;140', '120;0;130', '130;0;120', '140;0;110', '150;0;100', '160;0;90', '170;0;80', '180;0;70', '190;0;60', '200;0;50', '210;0;40', '220;0;30', '230;0;20', '240;0;10']

    white_to_black = ["c;c;c"]
    white_to_red = ["255;c;c"]
    white_to_green = ["c;255;c"]
    white_to_blue = ["c;c;255"]
    white_to_cyan = ["c;255;255"]
    white_to_purple = ["255;c;255"]

    yellow_to_red = ["255;c;0"]
    yellow_to_green = ["c;255;0"]
    yellow_to_white = ["255;255;/"]
    yellow_to_black = ["c;c;0"]

    all_colors = [
        red_to_black, red_to_white, red_to_yellow, red_to_purple,
        green_to_black, green_to_white, green_to_yellow, green_to_cyan,
        blue_to_black, blue_to_white, blue_to_cyan, blue_to_purple,

        yellow_to_red, yellow_to_green, yellow_to_white, yellow_to_black,
        purple_to_red, purple_to_blue, purple_to_white, purple_to_black,
        cyan_to_green, cyan_to_blue, cyan_to_white, cyan_to_black,

        black_to_white, black_to_red, black_to_green, black_to_blue, black_to_cyan, black_to_purple, black_to_yellow,
        white_to_black, white_to_red, white_to_green, white_to_blue, white_to_cyan, white_to_purple
    ]

    reset = '\033[38;2;255;255;255m'

    for color in all_colors:
        color_sub = 240
        color_add = 10

        content = color[0]
        color.pop(0)

        for _ in range(24):

            if 'c' in content:
                color.append(content.replace('c', str(color_sub)))

            elif '/' in content:
                color.append(content.replace('/', str(color_add)))

            color_add += 10
            color_sub -= 10

        color.extend(color[::-1])

colors = Dynamic

class Mode:
    """
    functions -> 2:
        Horizontal() |      Put the color gradient in honrizontal
        Vertical()   |      Put the color gradient in vertical
    """
    def Horizontal(color: list, text: str, mode: int = 1, col_reset: bool = True) -> str:
            lines = text.split("\n")
            result = ""    
            
            for line in lines:
                selector = 0
                characters = [*line]

                for letter in characters:
                    dyna_color = color[selector]

                    if col_reset:
                        result += " " * Textspace.getspace(letter) + f"\033[38;2;{dyna_color}m{letter.strip()}{Dynamic.reset}"
                    elif not col_reset:
                        result += " " * Textspace.getspace(letter) + f"\033[38;2;{dyna_color}m{letter.strip()}"

                    if selector + 1 < len(color):
                        selector += 1
                    else:
                        selector = 0

                result += "\n"
                
            if mode == 1:
                print(result.rstrip())

            elif mode == 2:
                input(result.rstrip())

            elif mode == 3:
                Sys.Type(result.rstrip())

            elif mode == 4:
                input(Sys.Type(result.rstrip()))

    def Vertical(color: list, text: str, mode: int = 1, col_reset: bool = True) -> str:
        lines = text.split("\n")
        result = ""
        selector = 0

        for line in lines:
            dyna_color = color[selector]

            result += " " * Textspace.getspace(line) + "".join(f"\033[38;2;{dyna_color}m"+ x for x in line.strip() +"\n")

            if selector + 1 < len(color):
                selector += 1
            else:
                selector = 0
        if col_reset:
            if mode == 1:
                print(result.rstrip()+Dynamic.reset)

            elif mode == 2:
                input(result.rstrip()+Dynamic.reset)

            elif mode == 3:
                Sys.Type(result.rstrip()+Dynamic.reset)

            elif mode == 4:
                input(Sys.Type(result.rstrip())+Dynamic.reset)

        elif not col_reset:
            if mode == 1:
                print(result.rstrip())

            elif mode == 2:
                input(result.rstrip())

            elif mode == 3:
                Sys.Type(result.rstrip())

            elif mode == 4:
                input(Sys.Type(result.rstrip()))

Sys.Init()