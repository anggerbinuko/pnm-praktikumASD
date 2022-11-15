class Antrian:
   def __init__(self):
      self.queue = []

   def tambah(self, value):
      if value not in self.queue:
         self.queue.append(value)
         return True
      else:
         return False

   def kepala(self):
	   return self.queue[0]

   def ekor(self):
       return self.queue[-1]

   def ambil(self):
       return self.queue.pop(0)

   def tampilkan(self):
       separator = " - "
       return separator.join(self.queue)

   def ukuran(self):
       return len(self.queue)