# **spatial.py**
  
  This Library is intended to assist with SPATIAL ANALYSES For purposes of this library, a SPATIAL ANALYSIS is defined as the ANALYSIS of PROPERTIES SURROUNDING a CENTRAL LOCATION via their PROPERTY VALUE and STRAIGHT LINE DISTANCE (SLD) to the CENTRAL LOCATION within a RADIUS OF INTEREST.
## To utilize this library, a CSV FILE is required
* The file MUST be a database CONTAINING PROPERTY ADDRESSES and PROPERTY VALUES
* The file MUST be organized into TWO COLUMNS with the above data
  * These columns MUST HAVE NAMES contained in the first cell - this is how we traverse with PANDAS
##  To utilize this library GEOPANDAS, GEOPY, and HAVERSINE MUST be INSTALLED
* Either local installation or Google Colab installation via '!pip install #library name#'
## Notes on organization of spatial.py file
* The comments throughout this file explain the purpose of each function via REQUIRES, MODIFIES, and EFFECT (RME) clauses and occasional notes
*  This LIBRARY is organized via a CLASS called !!SpatialAnalysis!!. This was the best way I could think to organize all the data with abstraction
  *  Meaning a class instance MUST be declared to make calls to the functions
  *  READ the COMMENTS above !!def __init__!! to understand how to declare an instance of the class
  
 # Autors Note
 This library was a passion project made for purposes of streamlining work that the Michigan Sports Consulting Group (MSCG) at the University of Michigan does for Economic Analysis Reports. By uploading this, I hope that this work for MSCG will have an impact that outlasts my time in the club. I also hope others find use of this library. 
 
Best,
Jacob Brinkmann
 https://www.linkedin.com/in/jacob-brinkmann-567438206/
