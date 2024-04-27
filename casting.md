Some examples of type casting in Python:

1. **Integer to Float**:
   - Converting an integer to a floating-point number using the `float()` function.
   - Example:
     ```python
     x = 10
     y = float(x)
     print(y)  # Output: 10.0
     ```

2. **Float to Integer**:
   - Converting a floating-point number to an integer using the `int()` function.
   - Example:
     ```python
     x = 10.5
     y = int(x)
     print(y)  # Output: 10
     ```

3. **Integer to String**:
   - Converting an integer to a string using the `str()` function.
   - Example:
     ```python
     x = 5
     y = str(x)
     print(y)  # Output: '5'
     ```

4. **String to Float**:
   - Converting a string (representing a float) to a float using the `float()` function.
   - Example:
     ```python
     x = "5.9"
     y = float(x)
     print(y)  # Output: 5.9
     ```

5. **String to Integer**:
   - Converting a string (representing an integer) to an integer using the `int()` function.
   - Example:
     ```python
     x = "5"
     y = int(x)
     print(y)  # Output: 5
     ```

Remember that type casting allows you to convert data between different types, which can be useful in various scenarios! 🐍✨

## Real World Scenarios
Type casting is used in programming to ensure that variables are processed in a compatible format. Here are some real-world examples where type casting is essential:

1. **Handling User Input**:
   - When you receive input from a user, it's often in the form of a string. If you expect a number to perform calculations, you need to cast the string to an integer or float.
   - Example:
     ```python
     user_input = input("Enter a number: ")
     number = int(user_input)  # Casting string to integer
     print(number * 2)  # Now you can perform arithmetic operations
     ```

2. **Working with Databases**:
   - When interacting with databases, you might retrieve numeric data as strings. To perform any mathematical operations, you would need to cast these strings to the appropriate numeric type.
   - Example:
     ```python
     price = "19.99"  # Price is a string when fetched from a database
     price = float(price)  # Casting string to float
     total = price * quantity  # Now you can calculate the total cost
     ```

3. **Data Serialization**:
   - When sending data over a network or saving it to a file, you often need to convert complex data types to strings (serialization). Conversely, when reading this data, you need to cast it back to the original data type (deserialization).
   - Example:
     ```python
     import json

     # Serialization
     data = {"age": 30}
     serialized_data = json.dumps(data)  # Converts dictionary to a JSON string

     # Deserialization
     received_data = '{"age": "30"}'
     deserialized_data = json.loads(received_data)
     deserialized_data["age"] = int(deserialized_data["age"])  # Casting string to integer
     ```

4. **Ensuring Precision**:
   - When dealing with financial calculations, you might need to cast integers to floats to ensure that you don't lose precision during division.
   - Example:
     ```python
     total_cents = 550  # Total amount in cents
     dollars = total_cents / 100  # This will result in an integer division
     dollars = float(total_cents) / 100  # Casting to float for accurate division
     ```

5. **Graphics Programming**:
   - In graphics programming, you might need to cast floating-point coordinates to integers for pixel-based operations since pixels are discrete units.
   - Example:
     ```python
     x_coordinate = 150.7
     y_coordinate = 299.3
     draw_pixel(int(x_coordinate), int(y_coordinate))  # Casting float to int for pixel coordinates
     ```

These examples illustrate how type casting is used to convert data types to ensure proper handling and processing of variables in different programming scenarios¹[1]²[2]³[3]⁴[4]. 🐍✨
