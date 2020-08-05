#! /usr/bin/python3
import csv
import psycopg2

vinputfile="/home/mustafa/Desktop/Senior Data Engineer - agaricus-lepiota-Aug.csv"
vhost = ""
vdatabase= ""
vuser= ""
vpassword= ""


shape_map = {
    "b": "bell",
    "c": "conical",
    "x": "convex",
    "f": "flat",
    "k": "knobbed",
    "s": "sunken"
}

color_map = {
    "b": "buff",
    "c": "cinnamon",
    "e": "red",
    "g": "gray",
    "h": "chocolate",
    "k": "black",
    "n": "brown",
    "o": "orange",
    "p": "pink",
    "r": "green",
    "u": "purple",
    "w": "white",
    "y": "yellow"
}


odor_map = {
    "a": "almond",
    "l": "anise",
    "c": "creosote",
    "y": "fishy",
    "f": "foul",
    "m": "musty",
    "n": "none",
    "p": "pungent",
    "s": "spicy"}

size_map = {"b": "broad", "n": "narrow"}


ring_type_map = {
    "c": "cobwebby",
    "e": "evanescent",
    "f": "flaring=f",
    "l": "large",
    "n": "none",
    "p": "pendant",
    "s": "sheathing",
    "z": "zone"
}

population_map = {
    "a": "abundant",
    "c": "clustered",
    "n": "numerous",
    "s": "scattered",
    "v": "several",
    "y": "solitary"}

habitat_map = {
    "g": "grasses",
    "l": "leaves",
    "m": "meadows",
    "p": "paths",
    "u": "urban",
    "w": "waste",
    "d": "woods"
}



def insert_list(liste):
    sql = """INSERT INTO mushrooms(cap_shape,cap_color,odor, gill_size,gill_color,stalk_color_above_ring,veil_color,ring_type,spore_print_color,population,habitat,lat,lon,ctime)
            VALUES(
                %(cap_shape)s,%(cap_color)s,%(odor)s,%(gill_size)s,%(gill_color)s,%(stalk_color_above_ring)s,%(veil_color)s,%(ring_type)s,%(spore_print_color)s,%(population)s,%(habitat)s,%(lat)s,%(lon)s,%(ctime)s
            )"""

    conn = None
    try:
        conn = psycopg2.connect(
            host=vhost, ,
            database=vdatabase, 
            user=vuser,
            password=vpassword)

        cur = conn.cursor()

        cur.executemany(sql, liste)

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()


def readfile():
    with open(vinputfile ,  newline='') as csvfile:
        #skip header
        next(csvfile)
        reader = csv.DictReader(csvfile, fieldnames=('cap_shape', 'cap_color', 'odor', 'gill_size', 'gill_color',
                                                     'stalk_color_above_ring', 'veil_color', 'ring_type', 'spore_print_color', 'population', 'habitat', 'lat', 'lon', 'ctime'))
        lst = []
        for row in reader:
            ds = {
                'cap_shape': shape_map.get(row['cap_shape'], "n/a"),
                'cap_color': color_map.get(row['cap_color'], "n/a"),
                'odor': odor_map.get(row['odor'], "n/a"),
                'gill_size': size_map.get(row['gill_size'], "n/a"),
                'gill_color': color_map.get(row['gill_color'], "n/a"),
                'stalk_color_above_ring': color_map.get(row['stalk_color_above_ring'], "n/a"),
                'veil_color': color_map.get(row['veil_color'], "n/a"),
                'ring_type': ring_type_map.get(row['ring_type'], "n/a"),
                'spore_print_color': color_map.get(row['spore_print_color'], "n/a"),
                'population': population_map.get(row['population'], "n/a"),
                'habitat': habitat_map.get(row['habitat'], "n/a"),
                'lat': row['lat'],
                'lon': row['lon'],
                'ctime': row['ctime']}
            lst.append(ds)
    insert_list(lst) # we can add chunk inserts, csv file is small, it is not necessary


if __name__ == '__main__':
    readfile()

