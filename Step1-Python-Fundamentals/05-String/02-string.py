### define
msg = 'test message..'
print(msg)

### multiple lines
msg = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(msg)

### string array
print(msg[1])

### slicing
print(msg[2:5])
print(msg[2:])
print(msg[:5])
print(msg[:-1])
print(msg[-5:-2])

### len
print(len(msg))

### methods
print(msg.lower())
print(msg.strip())
print(msg.upper())
print(msg.replace("H", "J"))
print(msg.split(","))


### concat
print(msg + "end")


### format
name = 'mohammad'
age = 22
msg = "man {} hastam va {} am shude.. "
print(msg.format(name, age))