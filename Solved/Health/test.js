$.getJSON("./Health/city_metrics.json", function(jsonData) {
    var outGeoJson = {}
    outGeoJson['properties'] = jsonData
    outGeoJson['type']= "Feature"
    outGeoJson['geometry']= {"type": "Point", "coordinates":
        [jsonData['lat'], jsonData['lon']]}
  
    console.log(outGeoJson)
  });