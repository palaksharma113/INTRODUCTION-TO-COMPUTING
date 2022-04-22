"""
#Question 5:-
(a) Print a specified list after removing fourth element i.e. Black.
(b) Remove Black and Pink from the list and replace it with Purple.
"""

Color_list = ['Red' 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Print (a) part
print('\n (a)')
print(Color_list)
#Remove  fourth element i.e. black.
Color_list.remove('Black')
print("\n List after removing Black Color :\n ", Color_list)

Color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Print (b) part
print('\n (b)')
print(Color_list)
# Replace Black and Pink with Purple
Color_list[3:5] = ['Purple']
print("\n List after replacing Black and Pink with Purple Color:\n ", Color_list)
