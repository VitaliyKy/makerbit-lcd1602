def on_button_pressed_a():
    makerbit.clear_lcd1602()
    basic.pause(100)
    makerbit.show_string_on_lcd1602("bit.ly/1234567",
        makerbit.position1602(LcdPosition1602.POS1),
        14)
input.on_button_pressed(Button.A, on_button_pressed_a)

makerbit.set_lcd_backlight(LcdBacklight.ON)
makerbit.show_string_on_lcd1602("START GAME",
    makerbit.position1602(LcdPosition1602.POS3),
    16)
basic.pause(5000)
makerbit.clear_lcd1602()
makerbit.show_string_on_lcd1602("Go !!!!", makerbit.position1602(LcdPosition1602.POS4), 14)