fromre import search as regex

# This Function return a Search Pattern that can be used via the ReEx-Module.
# The Pattern is actually used to delete unused Materials/Nodes when creating a new gate. (Material.001 Material.002 Material.003)
# The Method is created to free memory in the blendfile.
def pattern(string):
    return "^" + string + "*\\..{3}$"

# This is a Placeholder function.
# It will be replaced when I need a new Submethod.
def removeold(name, items):
    name = pattern(name)
    for item in items:
        if regex(name, item.name): # If it is named Name.001 or Name.002 ... it will be deleted.
            items.remove(item)

# This is a Placeholder function.
# It will be replaced when I need a new Submethod.
#def placeholder():
#    return 'PLACEHOLDER_EMPTY_RETURN'
#
