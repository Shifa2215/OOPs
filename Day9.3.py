class User:
    def __new__(cls):
        print("Object is being created")
        return super().__new__(cls)

    def __init__(self):
        print("Object is initialized")

u = User()
