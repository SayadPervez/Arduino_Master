# Arduino_Master_Delta is available in this link:
___
___
# Arduino_Master Alpha Version 3.0
___
___
# What's new ?
#### >>> Added 6 new functions : readSerial, writeSerial, dynamicSerial, horizontal, vertical and marker.
#### >>> Fixed a bug that prevented direct access to pyserial functions without **`serial.`** prefix.
#### >>> ERROR ID that displays the part of code where something got wrong. It could be either due to your faulty inputs or a bug. In case of a bug, paste the error message in the comments along with the ERROR ID. This feature was added for easier bug elimination !
___
___
# Intro:
#### Embedded C is used to program microcontrollers like Arduino. However embedded C could never compete with Python's simplicity and functionality. Also Arduino being a microcontroller, we get a lot of garbage values which we require to filter before utilizing. This module eases the process of extracting and passing data to Arduino via Serial communication.
#### This Module also provides Easy and flexible Data Science functions for Data extraction, filtering, removing garbage values and Data Visualization !
___
___
# Installing via pip:
### Use the following command to install Arduino_Master using pip.
### **`pip install Arduino_Master`**
___
___
# Automatic Installation of other required Modules:
#### This module requires two more packages namely **`pyserial`** and **`matplotlib`**. Yet just by importing this module using the import statement or by using any function, unavailable modules will be installed and imported automatically. Make sure you have good internet connection and if still you get ModuleNotFound error, try installing these two modules manually via pip.
___
___
# Importing Functions:
#### **`from Arduino_Master import *`** statement is used to import all available functions from Arduino_Master. This version contains the following functions which we'll be discussing shortly. These functions can be  grouped into 2 categories:
#### >> For Extracting and Writing data to Arduino:
#### $    ardata
#### $    readSerial
#### $    writeSerial
#### $    dynamicSerial
#### >> Data Science enabled functions for filtering and visualizing Data:
#### $ Graph
#### $ compGraph
#### $ horizontal
#### $ vertical
#### $ marker
#### $ most_frequent
#### $ least_frequent
#### $ compress
#### $ filter
___
___
# ardata():
#### ardata function is used to communicate with the arduino via Serial. This function returns a list of values available in the Serial port.
#### **`ardata(COM ,lines= 50 ,baudrate= 9600 ,timeout= 1 ,squeeze= True ,dynamic= False ,msg= 'a' ,dynamicDelay= 0.5 )`** is the function header.
___
## COM
#### **`COM`** parameter is used to specify the COM port to which arduino is connected to. You can pass either an integer or a string specifying the COM port.
### Eg:
```python
# COM parameter usage:
data = ardata(8) # or
data = ardata(COM=8)
#This will be interpreted as COM8
# If your COM port's name is not in this format, use the following:
data = ardata("YOUR_COM_PORT_NAME") #or
data = ardata(COM="YOUR_COM_PORT_NAME")
```
___
## lines
#### **`lines`** denotes the number of data units or lines it reads from the Serial monitor of Arduino. The default value is set to **50** which can be changed. Note that based on another parameter **`squeeze`**, the number of elements in the list this function returns might be lesser than the that of actual data.
___
## baudrate
#### **`baudrate`** parameter is used to specify the baudrate at which the Serial communication occurs at. The default value is **9600** which is the most widely used baudrate.
___
## timeout
#### **`timeout`** is used to specify the timeout value in seconds. The default value is **1**.
___
## squeeze
#### **`squeeze`** is used to specify if the data needs to be compressed. This uses a function from data science part of this module **`compress()`** which is used to remove **_repeated and sequential_** set of data with a single piece of data.
### Eg:
```python
# Consider the following list of data:
data = [ 1 , 2 , 2 , 2 , 3 , 3 , 5 , 1 , 1 , 2 , 5 , 5 ]
info = compress(data)
print(info)
# This will print [ 1 , 2 , 3 , 5 , 1 , 2 , 5 ]
```
#### **`squeeze`** uses the same function and takes either True (or) False boolean values as parameters. By default, this parameter is set to **True**. Referencing the above example code, if squeeze is set to **False**, ardata will retrun **data** and if it is set to **True** which is the default setting, it will return **info**.
___
## dynamic
#### **`dynamic`** is used to specify if the Serial communication is just to read from the serial port or for both reading and writing to the serial port. The default value is **false** which means you can only read from the Serial port. If dynamic is set to true, the string from the **`msg`** parameter will be written to the Serial port every time before reading a value.
___
## msg
#### **`msg`** parameter specifies the message that is to be written in the serial monitor. the default value is **'a'**. *It is a must to pas this parameter if dynamic is set to true.*
___
## dynamicDelay
#### **`dynamicDelay`** is used to specify the time this program has to wait after writing a value to the console and to start reading from the COM port. It is experimentally determined that a delay of 0.5 seconds is mandatory in order to prevent overlapping of passed messages.
___
> Note: ardata() reads one line at a time and hence Serial.println() should be used while coding Arduino and make sure there are no unnecessary Serial.print() or Serial.println() statements present in the code.
___
### Demo:
### 1) One way communication: With dynamic set to False
```C
//       Code uploaded to Arduino
int check = 2;
void setup() {
Serial.begin(9600);
pinMode(check,INPUT);
}

void loop() {
if(digitalRead(check)==HIGH)
  Serial.println("HIGH");
else
  Serial.println("LOW");
delay(500);
}
```
```python
# Python code:
from Arduino_Master import *
# info contains complete data
info = ardata(8,squeeze=False)
print(f"{len(info)}=>{info}")
#compressed info contains compresses form of data
CompressedInfo = compress(info)
print(f"{len(CompressedInfo)}=>{CompressedInfo}")

'''
Output:
50=>['LOW', 'LOW', 'LOW', 'LOW', 'LOW', 'LOW', 'HIGH', 'HIGH', 'HIGH', 'HIGH', 'HIGH', 'HIGH', 'HIGH', 'HIGH', 'HIGH', 'HIGH', 'HIGH', 'LOW', 'LOW', 'HIGH', 'HIGH', 'HIGH', 'HIGH', 'HIGH', 'HIGH', 'LOW', 'LOW', 'LOW', 'LOW', 'LOW', 'LOW', 'LOW', 'LOW', 'LOW', 'LOW', 'LOW', 'LOW', 'LOW', 'LOW', 'LOW', 'LOW', 'LOW', 'LOW', 'LOW', 'LOW', 'LOW', 'LOW', 'LOW', 'LOW', 'LOW']
5=>['LOW', 'HIGH', 'LOW', 'HIGH', 'LOW']

Thus actual data contains 50 elements whereas compresses data contains only 5 elements yet represents the outline of the data.
if info = ardata(8) was used instead, we would get the compressed version of data here represented by CompressedInfo.
'''
```
___
### 2) Two way communication: With dynamic set to True
```Code
//       Code uploaded to Arduino
int check = 2;
void setup() {
Serial.begin(9600);
pinMode(check,INPUT);
}

void loop() {
if(Serial.available()>0)
{
  if(Serial.readString()=="State")
  {
          if(digitalRead(check)==HIGH)
            Serial.println("HIGH");
          else
            Serial.println("LOW");
  }

delay(500);
}
}
// This code will print the result on the serial monitor only if "State" is sent to the serial monitor
```
```python
#   Python code
from Arduino_Master import *

info = ardata(8,dynamic=True,msg="State")
print(info)
'''
This would print
['LOW', 'HIGH', 'LOW', 'HIGH', 'LOW', 'HIGH']
Since squeeze by default is set to True, data is compressed!
'''
```
### Though both these demonstrations are used to extract data from Arduino, the later is better than the former. The reason is that when dynamic is set to True, we ask for instantaneous information whereas when dynamic is set to False, there is a possibility of getting initial data alone rather than instantaneous data since arduino keeps writing the values to the Serial monitor.
### The functionality being inherited from pyserial, It is possible to call all functions from pyserial module without prefixing the functions with 'serial.' statement.
___
___
# readSerial
#### **`readSerial`** reads only one line from the Arduino.
#### **`readSerial( COM , baudrate = 9600 , timeout = 1 )`** is the function header.
| Parameters | Usage |
|------------|------|
| COM        | Specify the COM port. Similar to ardata(), you can pass either an integer or the complete name as a string.|
| baudrate =9600| Set the baudrate. Default value is **9600**. |
| timeout =1| Set the timeout. Default is **1**|

#### returns a list with one element
___
___
# writeSerial()
#### **`writeSerial`** writes only one string to the Arduino's Serial monitor.
#### **`writeSerial(COM,baudrate=9600,timeout=1,msg="")`** is the function header.
| Parameters | Usage |
|------------|------|
| COM        | Specify the COM port. Similar to ardata(), you can pass either an integer or the complete name as a string.|
| baudrate =9600| Set the baudrate. Default value is **9600**. |
| timeout = 1| Set the timeout. Default is **1**|
| msg = ""| String to be written to the Serial Port |

#### Returns nothing !
___
___
# dynamicSerial
#### **`dynamicSerial`** is similar to dynamic mode of ardata() except that this returns a **_list_** with just one element in it.
#### **`dynamicSerial( COM , baudrate = 9600 , timeout = 1 , msg = "a" , dynamicDelay = 0.5 )`** is the function header.
| Parameters | Usage |
|------------|------|
| COM        | Specify the COM port. Similar to ardata(), you can pass either an integer or the complete name as a string.|
| baudrate =9600| Set the baudrate. Default value is **9600**. |
| timeout =1| Set the timeout. Default is **1**|
| msg ="a"| String to be written to the Serial Port |
| dynamicDelay = 0.5| Similar to that of ardata's dynamicDelay. Default value is set to **0.5 seconds**. Any value lesser than this would result in overlapping of the input. |

#### This function returns a list with only one element.
___
### Note:
#### For an arduino program that prints a value on Serial monitor only when we send it a value, the combination of writeSerial and readSerial functions won't work. dynamicSerial has to be used at that place.
```python
# Use
dynamicSerial(8,msg="Give DATA")

# INSTEAD OF
writeSerial(8,msg="Give Data")
data=readSerial(8)

# The latter would only return an empty list !!!
```
___
___
# Graph
#### **`Graph`** function is used to visualize a list of data.
#### **`Graph( y= None ,xlabel= 'dataPiece' ,ylabel= 'Amplitude' ,label= 'myData' ,color= 'red' ,title= 'Graph' ,markersize= 7 ,stl= 'ggplot' ,d= {} ,mark= 'x' )`** is the function header.
| Parameters   | Usage   |
|--------------|---------|
| y = None     | Pass a list of values to be plotted along the y-axis. The x-axis is automatically generated depending on the number of parameters in your given list.|
| xlabel = 'dataPiece' | Used to label the X-axis legend |
| ylabel = 'Amplitude' | Used to label the Y-axis legend |
| label = 'myData' | What you want your data to be called |
| color = 'red' | What color you want your data to be plotted with |
| title = 'Graph' | Name of the graph |
| mark = 'x' | Used to set the marker type. Refer this StyleSheet => [Marker_Style_Sheet](https://matplotlib.org/3.1.0/api/markers_api.html) |
| markersize = 7| Size of the plotting line. |
| stl = 'ggplot' | Style of Graph you wish. Refer this StyleSheet => [StyleSheet](https://matplotlib.org/3.1.0/gallery/style_sheets/style_sheets_reference.html) |
| d = {} | Used to pass a dictionary. This is used only when you need custom x values instead of default sequentially arranged X-values. y and d must not be passed together. |


#### Passing Strings to y (or) Dictionaries whose values are strings will also be plotted accordingly !
___
### Demo:
### Demonstration 1: Passing a list to y
```Python
# Python Code
myList = [ 1 , 2 , 3 , 4 , 5 , 1 , 7 , 7 , 10 , 8]
Graph(myList,stl='dark_background')
```
### Output:
![Graph_1](https://github.com/SayadPervez/Arduino_Master/blob/master/Graph_1.jpeg?raw=true)
___
### Demonstration 2: Plotting using a dictionary to get custom X-values.
```Python
# Python Code
myDict = { 0:10 , 1:12 , 2:12.05 , 3:-0.1 , 4:-12.05 , 5:0 , 6:5 , 6:5 , 10:5.5 }
Graph(d=myDict)
```
### Output:
![Graph_2](https://github.com/SayadPervez/Arduino_Master/blob/master/Graph_2.jpeg?raw=true)
___
### Demonstration 3: Plotting Strings:
```pytho
# Python code
listOfStrings = ['LOW', 'LOW', 'LOW', 'LOW', 'LOW', 'LOW', 'HIGH', 'HIGH', 'HIGH', 'HIGH', 'HIGH', 'HIGH', 'HIGH', 'HIGH', 'HIGH', 'HIGH', 'HIGH', 'LOW', 'LOW', 'HIGH', 'HIGH']
Graph(listOfStrings)
```
### Output:
![Graph_3](https://github.com/SayadPervez/Arduino_Master/blob/master/Graph_3.jpeg?raw=true)
#### The same can also be done by passing a Dictionary !
___
___
# compGraph
#### **`compGraph`** is used to compare two sets of data ( 2 lists or 2 dictionaries or 1 list with 1 dictionary)
#### **`compGraph( y= None ,y2= None ,xlabel= 'dataPiece' ,ylabel= 'Amplitude' ,label1= 'myData-1' ,label2= 'myData-2' ,color1= 'red' ,color2= 'blue' ,title= 'Graph' ,markersize= 7 ,stl= 'ggplot' ,fit= True ,d1= {} ,d2= {} `)** is the function header.
| Parameters   | Usage   |
|--------------|---------|
| y = None     | Pass a list of values to be plotted along the y-axis. The x-axis is automatically generated depending on the number of parameters in your given list.|
| xlabel = 'dataPiece' | Used to label the X-axis legend |
| ylabel = 'Amplitude' | Used to label the Y-axis legend |
| label1 = 'myData-1' | What you want your first set data to be called |
| label2 = 'myData-2' | What you want your second set data to be called |
| color1 = 'red' | What color you want your first set of data to be plotted with |
| color2 = 'blue' | What color you want your second set of data to be plotted with |
| title = 'Graph' | Name of the graph |
| markersize = 7| Size of the plotting line. |
| stl = 'ggplot' | Style of Graph you wish. Refer this StyleSheet => [StyleSheet](https://matplotlib.org/3.1.0/gallery/style_sheets/style_sheets_reference.html) |
| d1 = {} | Used to pass a dictionary as the first set of data. This is used only when you need custom x values instead of default sequentially arranged X-values. y and d1 must not be passed together. |
| d2 = {} | Used to pass a dictionary as the second set of data. This is used only when you need custom x values instead of default sequentially arranged X-values. y2 and d2 must not be passed together. |
| fit = True | A bit complex, and hence explained below |

___
## fit
#### **`fit`** parameter is used to specify if both the graphs need to be scaled to the maximum size or not. When y and y2 values have different number of elements **`fit = True`** enables changing X-values of the list of data which has less number of elements to equalize and approximate the correctness of distribution of data.
### With Fit **Disabled (left)** and With Fit **Enabled (right)**
![Fit](https://github.com/SayadPervez/Arduino_Master/blob/master/Fit.JPG?raw=true)
#### In the above pics, the red colored data represents raw_data and blue colored data represents filtered data. So naturally filtered set of data will have less number of elements in it and if compGraph() function is used the result would be similar to the left Graph which looks a bit absurd. When **fit = True** enables data to fit into the whole graph without affecting the Amplitude of the data. In simple words, smaller list of data is stretched to the size of the bigger list of data along the X-axis to give an **_approximation_** without using dictionaries which are comparatively difficult to use than lists so as to make the functions newbie friendly.
#### compGraph is similar to Graph function just with visualizing one more list of data
___
___
# horizontal
#### Creates a line parallel to  X-axis.
#### **`horizontal( y , lbl = 'marker' , start = 0 , end = 10 )`** is the function header.
|Parameter| Usage|
|---------|------|
|y|The distance from the origin is specified here|
|lbl = 'marker'|label is set to 'marker' by default|
|start = 0| value from which this line should start|
|end = 10 | value at which this line should end |

# Use this function before the Graph() function you wish the line to plotted in.
___
___
# vertical
#### Creates a line parallel to  Y-axis.
#### **`vertical( x , lbl = 'marker' , start = 0 , end = 10 )`** is the function header.
|Parameter| Usage|
|---------|------|
|x|The distance from the origin is specified here|
|lbl = 'marker'|label is set to 'marker' by default|
|start = 0| value from which this line should start|
|end = 10 | value at which this line should end |

#### Use this function before the Graph() function you wish the line to plotted in.
___
### vertical and horizontal are used as markers in a graph and are always black in color !
```Python
vertical(5)
horizontal(5)
Graph([1,2,3,4,5,6,7,8,9,10])
# This would result in the following Graph

```
![HorizonalVertical](https://github.com/SayadPervez/Arduino_Master/blob/master/Markers.jpeg?raw=true)
___
# marker
#### **`marker`** function creates a plus shaped plot at a given co-ordinate.
#### **`marker( x , y , limit = 1 , lbl = "marker" )`** is the function header.
|Parameter| Usage|
|---------|------|
|x|X Coordinate|
|y|Y Coordinate|
|limit=1| size of the marker|
|lbl='marker'|specify a label|

#### Use this function before the Graph() function you wish this marker to be plotted
```python
marker(5,6)
Graph([1,2,3,4,5,6,7,8,9,10])
# This would result in the following Graph
```
![markers_2](https://github.com/SayadPervez/Arduino_Master/blob/master/Markers_2.jpeg?raw=true)
___
___
# most_frequent
#### **`most_frequent`** is used to return the most frequently occurring element in a given list.
#### **`most_frequent(List)`** is the function header. Just pass a list as a parameter, and it will return the most repeated element in the given list.
___
# least_frequent
#### **`least_frequent`** is used to return the least frequently occurring element in a given list.
#### **`least_frequent(List)`** is the function header. Just pass a list as a parameter, and it will return the least repeated element in the given list.
___
___
# compress
#### **`compress()`** which is used to remove **_repeated and sequential_** set of data with a single piece of data.
#### **`compress(li)`** is the function header.
![compress](https://github.com/SayadPervez/Arduino_Master/blob/master/compress.JPG?raw=true)
#### In the above pic, red colored plot refers to the actual, uncompressed data while blue represents compressed data. As you can see the only purpose of compress is to show the trend of data and since Fit is enabled, an approximation of data is shown. In simple words, **`compress`** replaces continuous equivalent elements by a single element. **`compress`** is used only to visualize how many times a data piece varies to and fro and hence just an approximation. The next pics also has the same color representation as of before and demonstrates **`compress()`** function !
![compress2](https://github.com/SayadPervez/Arduino_Master/blob/master/compress2.JPG?raw=true)
![compress3](https://github.com/SayadPervez/Arduino_Master/blob/master/compress3.JPG?raw=true)
___
___
# filter
#### filter function is used to remove unnecessary data from a list.**_This function is only compatible with lists. Next version might have its compatibility increased to Dictionaries too._**
#### **`filter(data ,expected= [] ,expected_type= None ,max_deviation= None ,closeTo= None ,numeric= True ,limit= [] )`** is the function header.
| Parameters   | Usage   |
|--------------|---------|
| data | This parameter accepts a list. |
| expected = [ ] | Pass a list of expected elements that you need in the filtered list |
| expected_type = [ ] | Filters data based on the type. You can pass the following as arguements : int , float , str , 'num' , 'all'. Note that **num** and **all** alone are placed within single quotes since they are custom made types. 'num' denotes all numeric data like int and float. 'all' denotes all kinds of data.|
|max_deviation = None| Permitted maximum deviation from calculated average. |
|closeTo = None| Used to find data close to the given arguement. If closeTo alone is used without max_deviation, then max_deviation is taken as 1 by default. |
|numeric = True| Used to specify if you are looking for numeric data for calculation. If you wish to have strings of data in your filtered list make sure you set numeric to False. |
|limit = [ ]| Used to specify filter out garbage values! It basically means, no matter what, the data would not have gone beyond these limits. If it did, it is a Garbage Value. The format is **_limit=[ start-limit , end-limit ]_** |

### Why and How average is calculated ?
#### While filtering data with max_deviation, a value has to be specified from which the upper and lower limits containing data are filter.(i.e.) if max_deviation is 1.5, data is filtered such that only data within +(or)- 1.5 than average is present in the filtered data.
### This is how average is calculated.
#### If closeTo value is present, closeTo is taken as average.
#### If closeTo value is not passed, the most frequent data piece in the list of data is taken as average.
#### If closeTo is not passed as well as all the elements in the given data are unique, average is calculated in the conventional way. But with huge garbage values, the average would shift so much that no data remains in that area returning an empty list. For that when limit parameter is passed, garbage values are filtered out earlier before other calculations take place.
# Depending on the number of lines you need to read, time you need to wait will increase !!!
# Garbage values occur when your arduino's pins come in contact with each other. No matter if it is a cloth or your hand, arduino is sensitive enough to sense it and give you garbage values !!
___
# Demo:
# Garbage Value Removal:
```C
String msg;
const int trigPin = 9;
const int echoPin = 10;
double duration;
float distance;

void setup()
{
    Serial.begin(9600);
    pinMode(echoPin, INPUT);
    pinMode(trigPin, OUTPUT);
}

void loop()
// If information is available in Serial port from arduino get it and then checking for the distance
{   if (Serial.available()>0)
{
    msg=Serial.readString() ;
    if(msg=="d")
      {
        digitalWrite(trigPin, LOW);
        delayMicroseconds(2);
        digitalWrite(trigPin, HIGH);
        delayMicroseconds(10);
        digitalWrite(trigPin, LOW);
        duration = pulseIn(echoPin, HIGH);
        distance= duration/29/2;
        Serial.println(distance);
       }
    else
      int i=0; // Just Do nothing.....(Never Mind statement !!! )

}
}
```
___
```Python
# importing area !!
from Arduino_Master import *

# collecting data and saving it as a list in info
info=filter(ardata(8,squeeze=False,dynamic=True,msg="d",lines=50),expected_type="num")

# adding garbage values for checking purpose
info.insert(7,7000)
info.insert(8,4500)

# Removing all the repeating elements in order to test the average function !!!
# Since the data is from an Ultrasonic sensor, Its limit is known and it is 2 metre or 200 cm
Info=filter(list(set(info)),max_deviation=4,limit=[0,200])
print(info)
print(Info)

Graph(info)

Graph(Info)

compGraph(info,Info)
```
___
![Garbage_Value_removal_1](https://github.com/SayadPervez/Arduino_Master/blob/master/Garbage_Value_Removal_1.jpeg?raw=true)
### Without any filter, The above pic displays the data from Arduino with custom added garbage values in order to test.
___
![Garbage_Value_removal_2](https://github.com/SayadPervez/Arduino_Master/blob/master/Garbage_Value_Removal_2.jpeg?raw=true)
### Data after filtering is displayed above !! Thus conventional average works fine !!
___
![Garbage_Value_removal_3](https://github.com/SayadPervez/Arduino_Master/blob/master/Garbage_Value_Removal_3.jpeg?raw=true)
### Comparison of data is displayed above. Since the limits of the sensor were specified, values as high as 4500 and 6000 were removed and then the average was calculated making this module a well built one. Red is raw data whereas Blue is filtered data.
___
## If used correctly, you can filter your data in the following ways !!!
![Example_1](https://github.com/SayadPervez/Arduino_Master/blob/master/Light_Intensity_6.JPG?raw=true)
### Check light intensity and with previously measured values, you can check if the light is switched on or not just using an LDR.
### Learn how to plot a Graph like this using Arduino_Master through this link : [Plotting light intensity using Arduino_Master](https://www.instructables.com/id/Light-Intensity-Plotting-Using-Arduino-and-Pythons/)
___
![Example_2](https://github.com/SayadPervez/Arduino_Master/blob/master/US_Comparison.jpeg?raw=true)
###  Impulse removal Example in the above pic
___
![Example_3](https://github.com/SayadPervez/Arduino_Master/blob/master/US_closeTo_Comparison.png?raw=true)
### You can also detect and measure impulses !!!
___
___
# Developed by SAYAD PERVEZ !!!
# Trust me Am just 17.
# EmailID : [pervez2504@gmail.com]
