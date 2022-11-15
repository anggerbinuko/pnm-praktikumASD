class Tumpukan:
   def __init__(self):
      self.stack = []

   def tambah(self, value):
      if value not in self.stack:
         self.stack.append(value)
         return True
      else:
         return False

   def pucuk(self):
	   return self.stack[-1]

   def akhir(self):
       return self.stack.pop()

   def tampilkan(self):
       separator = " - "
       return separator.join(self.stack)

   def ukuran(self):
       return len(self.stack)