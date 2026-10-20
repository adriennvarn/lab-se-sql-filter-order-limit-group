import pandas as pd
import sqlite3

##### Part I: Basic Filtering #####

# Create the connection
# Note the connect is 'conn1' since there will be multiple .db used
conn1 = sqlite3.connect('planets.db')

# Select all
pd.read_sql("""SELECT * FROM planets; """, conn1)

"""   id     name       color  num_of_moons    mass  rings   """
# STEP 1
df_no_moons = pd.read_sql("""
    SELECT * 
    FROM planets
    WHERE num_of_moons = 0;
    """, conn1)

# STEP 2
df_name_seven = pd.read_sql("""
    SELECT name, mass
    FROM planets
    WHERE length(name) = 7;
    """, conn1)

##### Part 2: Advanced Filtering #####

# STEP 3
df_mass = pd.read_sql("""
    SELECT name, mass
    FROM planets
    WHERE mass <= 1;
    """, conn1)
                      

# STEP 4
df_mass_moon = pd.read_sql("""
    SELECT * 
    FROM planets
    WHERE mass < 1
    AND num_of_moons >= 1;
    """, conn1)

# STEP 5
df_blue = pd.read_sql("""
    SELECT name, color
    FROM planets
    WHERE color LIKE "%blue%";
    """, conn1)

##### Part 3: Ordering and Limiting #####

# STEP 0

# Create a connection
# Note the connect is 'conn2' since they will be multiple .db used
conn2 = sqlite3.connect('dogs.db')

# Select all
(pd.read_sql("SELECT * FROM dogs;", conn2))

"""id        name  age gender             breed  temperament  hungry
0   1      Snoopy    3      M            beagle     friendly       1   """

# STEP 6

df_hungry = pd.read_sql("""
    SELECT name, age, breed
    FROM dogs
    WHERE hungry = 1
    ORDER BY age ASC;
    """, conn2)
#test expects None for empty name, but pd.read_sql returns nan for empty name
df_hungry = df_hungry.astype(object).where(df_hungry.notna(), None)

# STEP 7

df_hungry_ages = pd.read_sql("""
    SELECT name, age, hungry
    FROM dogs
    WHERE hungry = 1
    AND age BETWEEN 2 AND 7
    ORDER BY name;
    """, conn2)

# STEP 8

df_4_oldest = pd.read_sql("""
    SELECT name, age, breed
    FROM dogs
    ORDER BY age DESC, breed ASC
    LIMIT 4;
    """, conn2)


##### Part 4: Aggregation #####

# STEP 0

# Create a connection
# Note the connect is 'conn3' since they will be multiple .db used
conn3 = sqlite3.connect('babe_ruth.db')

# Select all
(pd.read_sql("""
SELECT * FROM babe_ruth_stats; """, conn3))

"""
    id  year team league  doubles  triples  hits  HR  games  runs  RBI  at_bats   BB  SB  SO    AVG
0    1  1914  BOS     AL        1        0     2   0      5     1    2       10    0   0   4  0.200
"""


# STEP 9

df_ruth_years = pd.read_sql("""
    SELECT COUNT(DISTINCT year) AS years
    FROM babe_ruth_stats;
    """, conn3)
                            

# STEP 10

df_hr_total = pd.read_sql("""
    SELECT SUM(HR) AS total_HRs
    FROM babe_ruth_stats;
    """, conn3)


##### Part 5: Grouping and Aggregation #####

# STEP 11

df_teams_years = pd.read_sql("""
    SELECT team, COUNT(team) AS number_years
    FROM babe_ruth_stats
    GROUP BY team;
    """, conn3)

# STEP 12

df_at_bats = pd.read_sql("""
    SELECT team, AVG(at_bats) AS average_at_bats
    FROM babe_ruth_stats
    GROUP BY team
    HAVING average_at_bats > 200;
    """, conn3)


conn1.close()
conn2.close()
conn3.close()