import operator

class FlexibleCalculation:
    def _init_(self, a, b, operation):
        self.a = a
        self.b = b
        # operation is a string that maps to a function in the operator module
        self.operation = self.get_operation_function(operation)

    def get_operation_function(self, op_name):
        # Map string to actual function in the operator module
        operations = {
            'add': operator.add,
            'sub': operator.sub,
            'mul': operator.mul,
            'div': operator.truediv
        }
        return operations.get(op_name, None)  # None if operation not found

    def get_result(self):
        if not self.operation:
            return "Invalid operation"
        # Call the stored operation with a and b
        return self.operation(self.a, self.b)