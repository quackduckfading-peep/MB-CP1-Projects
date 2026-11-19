#RB, *args **kwargs Notes

def hello(last_name, *first_name):
    for first in first_name:
        print(f"Hello {first} {last_name}!")

hello("Glitch", "Void", "Cliftsh", "Katie")

hello("Kringle", "Kris", "Santa", "Claus", "Santa Claus", "Kris Kringle")

def clean(data, decimals=0, **kwargs):
    if not kwargs.get("data"):
          return "There is no data."
    elif kwargs.get("type") == "str":
        return kwargs.get("type")
    if kwargs.get("type") == "str":
            return kwargs["data"].strip().lower()
    elif kwargs.get("type") == "int":
            return int(kwargs["data"])
    elif kwargs.get("type") == "float":
            if kwargs.get("decimals"):
                  decimals = kwargs.get("decimals")
            return round(float(data), decimals)
    elif kwargs.get("type") == "list":
            return str(f"{x}, " for x in kwargs["data"])
    elif kwargs.get("type") == "bool":
            return f"{kwargs["data"]}"
        
print(clean(type="float", data="3.1415", decimals=3))
print(clean(data="Utah", type="str"))
print(clean())