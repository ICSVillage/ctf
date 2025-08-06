# CIP Tool
The CIP Tool is a handy and commandline tool for messaging ControlLogix PLCs and other CIP enabled devices.
It is designed as an expandable template for adding custom CIP commands and learning how to begin CIP pen testing. 

### How to Run
1. Open in PyCharm (The community edition will work, but I personally use Pro).      
2. Install pycomm3: `pip install pycomm3`  
3. Run the main.py  (If it has issues finding python, the project uses python 3, just point PyCharm to your python 3 install).      

### How to Use
The `help` or `h` command will list all commands.  
To connect to a controller use the `connect` or `c` command.  
To scan for controllers on the network, use the `discover` or `scan` command.  

### Fuzzing
This project also contains an example for fuzzing. 
1. Specify the CIP path of the device in the address variable.
2. Uncomment the fuzzing method you want to use in the main function.
3. Run fuzzing.py