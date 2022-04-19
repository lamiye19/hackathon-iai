import math
from math import *

def trouvernombre():
  n=3600
  sup=0
  for i in range(n):
      for j in range(n):
          for k in range(n):
              if i+j+k == 3600:
                  if math.pow(i,2) + math.pow(j,2) == math.pow(k,2):
                          sup = i * j * k
                          reponseA= i
                          reponseB= j
                          reponseC= k
                          print(f"Voici la réponse a={reponseA} , b={reponseB} et c={reponseC}")

  

if __name__ == '__main__':
  trouvernombre()