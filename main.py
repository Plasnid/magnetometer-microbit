baseline = input.magnetic_force(Dimension.STRENGTH)

def on_forever():
    if abs(input.magnetic_force(Dimension.STRENGTH) - baseline) > 100:
        basic.show_icon(IconNames.NO)
    else:
        basic.clear_screen()
basic.forever(on_forever)
