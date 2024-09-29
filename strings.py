sample_string = "Hello, World!"

# String Slicing
print("Original String:", sample_string)

# Slicing 
print("Slicing:")
print("First 5 characters:", sample_string[:5])        # 'Hello'
print("Characters from index 7 to 11:", sample_string[7:12])  # 'World'
print("Last 6 characters:", sample_string[-6:])       # 'World!'
print("Every second character:", sample_string[::2])   # 'Hlo ol!'

# String Methods
print("\nString Methods:")
print("Uppercase:", sample_string.upper())              # 'HELLO, WORLD!'
print("Lowercase:", sample_string.lower())              # 'hello, world!'
print("Title case:", sample_string.title())              # 'Hello, World!'
print("Replace 'World' with 'Python':", sample_string.replace("World", "Python"))  # 'Hello, Python!'
print("Split string:", sample_string.split(","))        # ['Hello', ' World!']
print("Find index of 'World':", sample_string.find("World"))  # 7
print("String length:", len(sample_string))              # 13
print("Check if string starts with 'Hello':", sample_string.startswith("Hello"))  # True
print("Check if string ends with '!':", sample_string.endswith("!"))  # True
