#!/usr/bin/env python3

from tkinter import Tk, Label, Button, Entry, Text, messagebox, END, WORD


########################################
# WINDOWS
########################################

class Window(object):

    # initialize the window
    def __init__(self, width: int = 800, height: int = 600, title: str = 'win', resizable: bool = False) -> None:
        self.width = width
        self.height = height
        self.title = title
        self.resizable = resizable
        self.background = None
        self.root = Tk()

    # set the size of the window
    def set_size(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    # set the window title
    def set_title(self, title: str) -> None:
        self.title = title

    # set the window resizable state
    def set_resizable(self, resizable: bool) -> None:
        self.resizable = resizable

    # set the window background color
    def set_background(self, background: str) -> None:
        self.background = background

    # configure the window settings
    def __configure_settings(self) -> None:
        self.root.title(self.title)
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(
            f'{self.width}x{self.height}+{(screen_width-self.width)//2}+{(screen_height-self.height)//2}')
        self.root.resizable(self.resizable, self.resizable)
        self.root.configure(background=self.background)

    # draw the window
    def draw(self) -> None:
        self.__configure_settings()
        self.root.mainloop()


class PopupWindow(object):

    # popup window types
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    QUESTION = 'QUESTION'

    # initialize the popup window
    def __init__(self, title: str = None, message: str = None, _type: str = ERROR) -> None:
        self.title = title
        self.message = message
        self.type = _type

    # set the title of the popup window
    def set_title(self, title: str) -> None:
        self.title = title

    # set the message of the popup window
    def set_message(self, message: str) -> None:
        self.message = message

    # set the type of the popup window
    def set_type(self, _type: str) -> None:
        self.type = _type

    # draw the popup window
    def draw(self) -> None:
        if self.type == self.INFO:
            messagebox.showinfo(self.title, self.message)
        elif self.type == self.WARNING:
            messagebox.showwarning(self.title, self.message)
        elif self.type == self.ERROR:
            messagebox.showerror(self.title, self.message)
        elif self.type == self.QUESTION:
            messagebox.askquestion(self.title, self.message)


########################################
# WIDGETS
########################################

class Widget(object):

    # initialize the widget
    def __init__(self, parent: Window, x_pos: int = 0, y_pos: int = 0, foreground: str = None, background: str = None) -> None:
        self.parent = parent.root
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.foreground = foreground
        self.background = background
        self.item = None

    # get the widgets position
    def get_pos(self) -> tuple:
        return (self.x_pos, self.y_pos)

    # set the widgets position
    def set_pos(self, x_pos: int, y_pos: int) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos

    # set the widgets foreground color
    def set_foreground(self, color: str) -> None:
        self.foreground = color

    # set the widgets background color
    def set_background(self, color: str) -> None:
        self.background = color


class TextLabel(Widget):

    # initialize the text label
    def __init__(self, parent: Window, text: str = None, x_pos: int = 0, y_pos: int = 0, foreground: str = None, background: str = None) -> None:
        super().__init__(parent, x_pos, y_pos, foreground, background)
        self.text = text
        self.font = None

    # set the text for the text label
    def set_text(self, text: str) -> None:
        self.text = text

    # set the font for the text label
    def set_font(self, font: tuple) -> None:
        self.font = font

    # draw the text label to the parent component
    def draw(self) -> None:
        self.item = Label(self.parent, text=self.text,
                          fg=self.foreground, bg=self.background, font=self.font)
        self.item.place(x=self.x_pos, y=self.y_pos)


class PushButton(Widget):

    # initialize the push button
    def __init__(self, parent: Window, text: str = None, x_pos: int = 0, y_pos: int = 0, foreground: str = None, background: str = None, on_click: any = None) -> None:
        super().__init__(parent, x_pos, y_pos, foreground, background)
        self.text = text
        self.command = on_click
        self.font = None
        self.border_size = 1

    # set the text for the push button
    def set_text(self, text: str) -> None:
        self.text = text

    # set the font for the push button
    def set_font(self, font: tuple) -> None:
        self.font = font

    # set the border size for the push button
    def set_border(self, size: int) -> None:
        self.border_size = size

    # set the on click command for the push button
    def set_command(self, on_click: any) -> None:
        self.command = on_click

    # draw the push button to the parent component
    def draw(self) -> None:
        self.item = Button(self.parent, text=self.text, fg=self.foreground,
                           bg=self.background, font=self.font, command=self.command, bd=self.border_size)
        self.item.place(x=self.x_pos, y=self.y_pos)


class TextInput(Widget):

    # initialize the text input
    def __init__(self, parent: Window, x_pos: int = 0, y_pos: int = 0, foreground: str = None, background: str = None) -> None:
        super().__init__(parent, x_pos, y_pos, foreground, background)
        self.font = None
        self.width = None
        self.border_size = 1

    # set the font for the text input
    def set_font(self, font: tuple) -> None:
        self.font = font

    # set the width for the text input
    def set_width(self, width: int) -> None:
        self.width = width

    # set the border size for the text input
    def set_border(self, size: int) -> None:
        self.border_size = size

    # get the text from the text input
    def get_text(self) -> str:
        return self.item.get()

    # clear the text in the text input
    def clear(self) -> None:
        self.item.delete(0, END)

    # draw the text input to the parent component
    def draw(self) -> None:
        self.item = Entry(self.parent, fg=self.foreground,
                          bg=self.background, font=self.font, width=self.width, bd=self.border_size)
        self.item.place(x=self.x_pos, y=self.y_pos)


class TextBox(Widget):

    # initialize the text box
    def __init__(self, parent: Window, x_pos: int = 0, y_pos: int = 0, foreground: str = None, background: str = None) -> None:
        super().__init__(parent, x_pos, y_pos, foreground, background)
        self.font = None
        self.width = None
        self.height = None
        self.border_size = 1

    # set the font for the text box
    def set_font(self, font: tuple) -> None:
        self.font = font

    # set the width of the text box
    def set_width(self, width: int) -> None:
        self.width = width

    # set the height of the text box
    def set_height(self, height: int) -> None:
        self.height = height

    # set the border size for the text box
    def set_border(self, size: int) -> None:
        self.border_size = size

    # get the text from the text box
    def get_text(self) -> str:
        return self.item.get('1.0', END)

    # clear the text in the text box
    def clear(self) -> None:
        self.item.delete('1.0', END)

    # draw the text box to the parent component
    def draw(self) -> None:
        self.item = Text(self.parent, fg=self.foreground,
                         bg=self.background, font=self.font, width=self.width, bd=self.border_size, height=self.height, wrap=WORD)
        self.item.place(x=self.x_pos, y=self.y_pos)
