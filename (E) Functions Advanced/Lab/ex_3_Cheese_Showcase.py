# White a function called sorting_cheeses that receives keywords arguments:
# •	The key represents the name of the cheese
# •	The value is a list of quantities (integers) of the pieces of the given cheese
# The function should return the cheeses and their pieces' quantities sorted by the number of pieces of a cheese kind in descending order. If two or more cheeses have the same number of pieces, sort them by their names in ascending order (alphabetically). For each kind of cheese, return their pieces quantities in descending order.
# For more clarifications, see the examples below.
# Input
# print(
#     sorting_cheeses(
#         Parmesan=[102, 120, 135],
#         Camembert=[100, 100, 105, 500, 430],
#         Mozzarella=[50, 125],
#     )
# )
# Output
# Camembert
# 500
# 430
# 105
# 100
# 100
# Parmesan
# 135
# 120
# 102
# Mozzarella
# 125
# 50
# Input
# print(
#     sorting_cheeses(
#         Parmigiano=[165, 215],
#         Feta=[150, 515],
#         Brie=[150, 125]
#     )
# )
# Output
# Brie
# 150
# 125
# Feta
# 515
# 150
# Parmigiano
# 215
# 165
def sorting_cheeses(**cheeses):
    cheeses = sorted(cheeses.items(), key=lambda double:(-len(double[1]), double[0]))
    result = []
    for item in cheeses:
        result.append(item[0])
        result.extend(sorted(item[1], key=lambda x: -x))
    return "\n".join(str(x) for x in result)

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
print()
print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)

