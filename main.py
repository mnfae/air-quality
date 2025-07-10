def on_button_pressed_a():
    kitronik_air_quality.send_all_data()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    kitronik_air_quality.erase_data()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

kitronik_air_quality.control_display_on_off(kitronik_air_quality.on_off(True))
kitronik_air_quality.set_data_for_usb()
kitronik_air_quality.add_project_info("air quality", "air quality")
kitronik_air_quality.setup_gas_sensor()
kitronik_air_quality.calc_baselines()

def on_forever():
    kitronik_air_quality.measure_data()
    kitronik_air_quality.show("Temperature:" + ("" + str(kitronik_air_quality.read_temperature(kitronik_air_quality.TemperatureUnitList.C))) + " C",
        1,
        kitronik_air_quality.ShowAlign.LEFT)
    kitronik_air_quality.show("Humidity:" + ("" + str(kitronik_air_quality.read_humidity())) + "%",
        2,
        kitronik_air_quality.ShowAlign.LEFT)
    kitronik_air_quality.show("Pressure:" + ("" + str(kitronik_air_quality.read_pressure(kitronik_air_quality.PressureUnitList.PA) / 1000)) + " kPa",
        3,
        kitronik_air_quality.ShowAlign.LEFT)
    kitronik_air_quality.show("AQI Score :" + str(kitronik_air_quality.get_air_quality_score()),
        4,
        kitronik_air_quality.ShowAlign.LEFT)
    kitronik_air_quality.show("eCO2: " + str(kitronik_air_quality.reade_co2()) + "ppm",
        5,
        kitronik_air_quality.ShowAlign.LEFT)
    basic.pause(5000)
basic.forever(on_forever)

def on_forever2():
    kitronik_air_quality.measure_data()
    kitronik_air_quality.include_date(kitronik_air_quality.on_off(True))
    kitronik_air_quality.include_time(kitronik_air_quality.on_off(True))
    kitronik_air_quality.select_separator(kitronik_air_quality.Separator.TAB)
    kitronik_air_quality.log_data()
    basic.pause(5000)
basic.forever(on_forever2)
