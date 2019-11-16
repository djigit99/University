import enum


class Global:

    def __init__(self, name=""):
        self.name = name

    def get_name(self):
        return self.name


class Global_var(Global):

    def __init__(self, name="var", type_=""):
        super().__init__(name)
        self.type_ = type_


class Global_const(Global):

    def __init__(self, name="const", value=""):
        super().__init__(name)
        self.value = value


class Function(Global):

    parameters = []  # list of elements with type Global_var

    def __init__(self, name="func", return_type="", source_body=[]):
        super().__init__(name)
        self.return_type = return_type
        self.source_body = source_body

    def add_parameter(self, parameter):
        self.parameters.append(parameter)

    def set_parameters(self, parameters):
        self.parameters = parameters

    def get_parameters(self):
        return self.parameters

    def set_return_type(self, return_type):
        self.return_type = return_type

    def get_return_type(self):
        return self.return_type

    def set_source_body(self, source_body):
        self.source_body = source_body

    def get_source_body(self):
        return self.source_body


class Class(Global):
    constants = []
    properties = []
    methods = []

    def __init__(self, name, extends='', implements=''):
        super().__init__(name)
        self.extends = extends
        self.implements = implements

    def add_constant(self, constant):
        self.constants.append(constant)

    def add_property(self, __property):
        self.properties.append(__property)

    def add_method(self, method):
        self.methods.append(method)

    def get_constants(self):
        return self.constants

    def get_constants_with_mode(self, mod):
        return [const for const in self.constants if const.get_mod() == mod]

    def get_properties(self):
        return self.properties

    def get_properties_with_mode(self, mod):
        return [__property for __property in self.properties if __property.get_mod() == mod]

    def get_methods(self):
        return self.methods

    def get_methods_with_mode(self, mod):
        return [method for method in self.properties if method.get_mod() == mod]

    def get_inherited_class(self):
        return self.extends

    def get_inherited_interface(self):
        return self.implements


class Interface(Global):
    # Only public constants and public methods
    constants = []
    methods = []
    parents = []

    def __init__(self, name, parents=[]):
        super().__init__(name)
        self.parents = parents

    def add_constant(self, constant):
        self.constants.append(constant)

    def get_constants(self):
        return self.constants

    def set_constants(self, constants):
        self.constants = constants

    def add_method(self, method):
        self.methods.append(method)

    def set_methods(self, methods):
        self.methods = methods

    def get_methods(self):
        return self.methods

    def add_parent(self, parent):
        self.parents.append(parent)

    def set_parents(self, parents):
        self.parents = parents

    def get_parents(self):
        return self.parents


class Trait(Global):
    properties = []
    methods = []

    def add_property(self, __property):
        self.properties.append(__property)

    def add_method(self, method):
        self.methods.append(method)

    def get_properties(self):
        return self.properties

    def get_properties_with_mode(self, mod):
        return [__property for __property in self.properties if __property.get_mod() == mod]

    def get_methods(self):
        return self.methods

    def get_methods_with_mode(self, mod):
        return [method for method in self.properties if method.get_mod() == mod]


class AccessModifier(enum.Enum):
    public = 1
    protected = 2
    private = 3


class Item:

    def __init__(self, name, mod):
        self.name = name
        self.mod = mod

    def get_name(self):
        return self.name

    def get_mod(self):
        return self.mod


class Var(Item):

    def __init__(self, name, mode, __type=""):
        super().__init__(name, mode)
        self.__type = __type

    def set_type(self, __type):
        self.__type = __type

    def get_type(self):
        return self.__type


class Const(Var):

    def __init__(self, name, mod, val):
        super().__init__(name, mod)
        self.val = val

    def get_val(self):
        return self.val


class Method(Item):
    parameters = []

    def __init__(self, name, mod, return_type="", source_body=[]):
        super().__init__(name, mod)
        self.return_type = return_type
        self.source_body = source_body

    def add_parameter(self, parameter):
        self.parameters.append(parameter)

    def set_parameters(self, parameters):
        self.parameters = parameters

    def get_parameters(self):
        return self.parameters

    def set_return_type(self, return_type):
        self.return_type = return_type

    def get_return_type(self):
        return self.return_type

    def set_source_body(self, source_body):
        self.source_body = source_body

    def get_source_body(self):
        return self.source_body


class Namespace:
    nm_name = ""
    global_vars = []
    constants = []
    functions = []
    classes = []
    interfaces = []
    traits = []

    def __init__(self, name):
        self.nm_name = name

    def add_global_var(self, var):
        self.global_vars.append(var)

    def get_global_vars(self):
        return self.global_vars

    def add_constants(self, constant):
        self.constants.append(constant)

    def get_constants(self):
        return self.constants

    def add_function(self, function):
        self.functions.append(function)

    def get_functions(self):
        return self.functions

    def add_class(self, __class):
        self.classes.append(__class)

    def get_classes(self):
        return  self.classes

    def add_interface(self, interface):
        self.interfaces.append(interface)

    def get_interfaces(self):
        return self.interfaces

    def add_trait(self, trait):
        self.traits.append(trait)

    def get_traits(self):
        return self.traits


if __name__ == '__main__':
    my_function = Function('func', AccessModifier.public,
                           [Var('var1', AccessModifier.private), Var('var2', AccessModifier.protected)])
    li = [var for var in my_function.get_parameters() if var.get_mod() == AccessModifier.private]
    for i in li:
        print(i.get_name())
