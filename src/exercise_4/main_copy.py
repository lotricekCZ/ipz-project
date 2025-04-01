from objects.display import Display

display = Display(128, 64)
display.draw_text(10, 40, "Hello World", "red")

display.show()