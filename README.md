# WELCOME! to the AirBnB clone project!

The AirBnB clone project is a website that will allow users to book a place by entering details like State, City, and Place.

# AUTHORS
- Osei Kuffour Emmanuel

# From The Console
For now the project is limited to the console (terminal) and will be operated from the terminal.
It will have the options to;
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object
- Quit the program

# More Information

## Execution
Your shell should work like this in Interactive mode

- To start the program:
```($) ./console.py ```

``` 
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$ 
```

- To use help
```
(hbnb) help create
Creates a new instance of BaseModel
saves it (to the JSON file) and prints the id.
(hbnb) help all
Prints the string representation of all instances
or all instances of a class.
(hbnb) help update

        Update the attribute of an instance based on its ID.

        Parameters:
            arg (str): The argument containing the instance ID, attribute name, and
                attribute value separated by spaces.

        Raises:
            ValueError: If the argument is empty or missing the instance ID, or if the
                instance ID is not found in the instance dictionary, or if the argument
                is missing the attribute name, or if the argument is missing the
                attribute value.

        Returns:
            None
        
(hbnb) help show
Prints the string representation
of an instance based on the class name and id.
(hbnb) help quit
Quit command to exit the program

```
- To quit the console

```(hbnb) quit```