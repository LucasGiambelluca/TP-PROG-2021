import xml.etree.cElementTree as et


def xml_list_availables_stations(root):
    if root == None:
        print("no information available - problem with read information from file")
        return []
    print("Listing availables stations")
    list_of_stations = []
    element = 0
    for station in root.findall("station"):
        list_of_stations.append(station)
        print(f'''{element + 1}-{station.get("name")}''')
        element += 1
    return list_of_stations


def xml_showing_station_information(station, station_name):
    if station == None:
        print("no information availabe")
        return None
    print(
        f'''Quantity of sensors in station {station.get("name").capitalize()}: {station.find("number_of_sensors").text}''')
    for sensor in station[2:]:
        if sensor.get("active") == "True":
            print(
                f'''{sensor.tag.capitalize()}\t:\t{sensor[0].text} {sensor[1].text}''')


def xml_select_station(list_of_stations, position):
    if position == -1 or list_of_stations == []:
        return None
    else:
        return list_of_stations[position]


def xml_get_data_from_file(file):
    tree_ff = et.parse('./' + file)
    root_ff = tree_ff.getroot()
    return et.fromstring(et.tostring(root_ff, encoding='utf8').decode('utf8'))


def xml_get_position_for_station(station_name, list_of_station):
    length = len(list_of_station)
    if station_name.isdigit() and 0 <= int(station_name)-1 < length:
        return int(station_name)-1

    for position in range(0, length):
        if list_of_station[position].get("name") == station_name:
            return position
    else:
        return -1

def xml_get_most_low_battery_station(list_station):
    batterys = []
    min_volt_prom = 10
    volt_prom = 0
    station_position = 0
    for station in list_station:
        batterys.append(station.find("battery_voltage_list"))
    for battery in batterys:
        for values in battery:
            volt_prom += int(str(values.text))
        volt_prom = volt_prom // 20
        if volt_prom < min_volt_prom:
            min_volt_prom = volt_prom
            station_position += 1 
        volt_prom = 0
    return list_station[station_position].get("name"), min_volt_prom,"mV"
            
'''
    Algoritmo:
    Listo todas las estaciones disponibles(nombres)
    Pido nombre de estacion
    Si el nombre esta en la lista:
        mostrar(
            Cantidad de sensores de la estación nombre estacion: cantidad de sensores
            muestro todos los sensores disponibles, sensores que active="true" 
            Temperatura: medida unidad
            Humedad: medida unidad
            Velocidad Viento: medida unidad
        )
    Sino 
'''
