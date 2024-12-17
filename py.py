class MyClass:
    class_attribute = "class value"

    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute

    def instance_method(self):
        return f"Instance method: {self.instance_attribute}"

    @classmethod
    def class_method(cls):
        return f"Class method: {cls.class_attribute}"

    @staticmethod
    def static_method():
        return "Static method: No access to instance or class data."

# Create an instance
obj = MyClass("instance value")

# Call instance method
print(obj.instance_method())  # Output: Instance method: instance value

# Call class method
print(MyClass.class_method())  # Output: Class method: class value
print(obj.class_method())      # Output: Class method: class value

# Call static method
print(MyClass.static_method())  # Output: Static method: No access to instance or class data.
print(obj.static_method())      # Output: Static method: No access to instance or class data.
