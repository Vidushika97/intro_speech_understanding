
def words2characters(array):
    characters = []
    for items in array:
        for char in str(items):
            characters.append(char)
    return characters