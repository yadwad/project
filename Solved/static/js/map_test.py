### color_map.py
 
import csv
from bs4 import BeautifulSoup
 
# Read in unemployment rates
est = {}
max_value = 100; min_value = 0
reader = csv.reader(open('health_tract.csv'), delimiter=",")
for row in reader:
    try:
        county_fips = row[1] + row[2]
        rate = float( row[8].strip() )
        est[county_fips] = rate
    except:
        pass
 
 
# Load the SVG map
svg = open('counties.svg', 'r').read()
 
# Load into Beautiful Soup
soup = BeautifulSoup(svg, selfClosingTags=['defs','sodipodi:namedview'])
 
# Find counties
paths = soup.findAll('path')
 
# Map colors
colors = ["#F1EEF6", "#D4B9DA", "#C994C7", "#DF65B0", "#DD1C77", "#980043"]
 
# County style
path_style = "font-size:12px;fill-rule:nonzero;stroke:#FFFFFF;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:"
 
# Color the counties based on unemployment rate
for p in paths:
     
    if p['id'] not in ["State_Lines", "separator"]:
        try:
            rate = unemployment[p['id']]
        except:
            continue
             
         
        if rate > 10:
            color_class = 5
        elif rate > 8:
            color_class = 4
        elif rate > 6:
            color_class = 3
        elif rate > 4:
            color_class = 2
        elif rate > 2:
            color_class = 1
        else:
            color_class = 0
 
 
        color = colors[color_class]
        p['style'] = path_style + color
 
print(soup.prettify())
