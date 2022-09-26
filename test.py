from tkinter import NONE
from Sayuran.repository import SayuranRepository

x = SayuranRepository.get_all(limit=100,search=None,sayuran=1,provinsi=None)
# print(x)
for i in x:
    print(i)