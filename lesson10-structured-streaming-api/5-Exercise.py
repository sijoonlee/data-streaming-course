# Lesson 2, Table ID 6
import pathlib
from pyspark.sql import SparkSession
import pyspark.sql.functions as psf

CITIES_CSV = './data/cities.csv'
LINES_CSV = './data/lines.csv'
TRACKS_CSV = './data/tracks.csv'


def transformation_exercise():
    """
    Do an exploration on World Transit System
    This is the same exercise as the previous transformation,
    but we'll be able to see the transformation through Spark UI.
    Q1: How many tracks are still in operation?
    Q2: What are the names of tracks that are still in operation?
    :return:
    """

    
    # TODO add a configuration for assigning Spark UI and the port number
    spark = SparkSession.builder \
        .master("local[2]") \
        .appName("transformation exercise") \
        .getOrCreate()

    # TODO import all the necessary files - the dataframe name should match the CSV files,
    # like cities_df should be corresponding to CITIES_CSV, and so on.
    cities_df = spark.read.csv(CITIES_CSV, header=True)
    lines_df = spark.read.csv(LINES_CSV, header=True)
    tracks_df = spark.read.csv(TRACKS_CSV, header=True)

    # TODO the names of the columns are confusing (two id columns, but they're not matching)
    # TODO how do we solve this problem?
    lines_df = lines_df.withColumnRenamed("name", "city_name").select("city_id", "city_name")
    left_df = cities_df.join(lines_df, cities_df.id == lines_df.city_id, "inner")

    # TODO Q1: how do you know which track is still operating?
    tracks_df.select(psf.max("closure")).distinct().show()

    # TODO Q2: filter on only the operating tracks
    filtered_df = tracks_df.filter("closure like '999999%' ")

    joined_df = left_df.join(filtered_df, left_df.city_id == filtered_df.city_id, "inner")

    # TODO Q1 and Q2 answers
    joined_df.select("city_name").distinct().count()
    joined_df.select("city_name").distinct().show(40)


if __name__ == "__main__":
    transformation_exercise()
# +------------+
# |max(closure)|
# +------------+
# |   999999999|
# +------------+

# +--------------------+                                                          
# |           city_name|
# +--------------------+
# | East Coast Mainline|
# |                   K|
# |Estrada de Ferro ...|
# |       Mukogawa Line|
# |                 R16|
# |     Arashiyama Line|
# |          Isogo Line|
# |    Praça XV–Paquetá|
# |Via Falkirk Graha...|
# |                   7|
# |                M 14|
# |                  C6|
# |     Kita-Senju Line|
# |        Jamaica Line|
# |          Nikko Line|
# |     Izumibashi Line|
# |          Nambu Line|
# |       Kanagawa Line|
# |     Praça XV–Cocotá|
# |Ishiyama Sakamoto...|
# |   Mariatroster Bahn|
# |        Odawara Line|
# |     Putnam Division|
# |       Fangshan Line|
# |       Yizhuang Line|
# |Ver. José Diniz-I...|
# |          Brown Line|
# |Sungai Buloh-Kaja...|
# |                  15|
# |           Mito Line|
# |           Taga Line|
# |     4th Avenue Line|
# |                  U2|
# |West London Line ...|
# |East Coast Main Line|
# |Nagahori Tsurumi-...|
# |      New Haven Line|
# |Troncal F - Améri...|
# |      Toranomon Line|
# |  Línea 1 (Tramo 1B)|
# +--------------------+
# only showing top 40 rows