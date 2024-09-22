import tkinter as tk

class ToolTip:
    """Clase simple para mostrar un pequeño cuadradito con texto (denominado "tooltip") cuando pases el cursor por encima de un widget."""
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        """Mostrar el tooltip."""
        
        x = event.x_root + 10
        y = event.y_root + 10
        
        self.tooltip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry("+%d+%d" % (x, y))
        
        label = tk.Label(tw, text=self.text, justify="left",
            background="#ffffe0", relief="solid", borderwidth=1,
            font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hide_tooltip(self, event):
        """Esconder el tooltip."""
        
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None