import math
import numpy as np

##############
# From or based on:
# the book _Python Playground Geeky project for the curious
# programmer_ by Mahesh Venkitachalam. Published by no starch press
#############

width, height = 640, 480
N = 4

pos = [width/2.0, height/2.0] + 10*np.random.rand(2*N).reshape(N,2)
angles = 2*math.pi*np.random.rand(N)
vel = np.array(list(zip(np.sin(angles), np.cos(angles))))

def applyBC(self):
  """apply boundary conditions"""
  deltaR = 2.0
  for coord in self.pos:
    if coord[0] > width + deltaR:
      coord[0] = - deltaR
    if coord[0] < - deltaR:
      coord[0] = width + deltaR
    if coord[1] > height + deltaR:
      coord[1] = - deltaR
    if coord[1] < - deltaR:
      coord[1] = height + deltaR

if __name__ == "__main__": 
  print(pos)
  print("------pos-----")
  print(angles)
  print("------angles-------")
  print(vel)
  print("-------vel--------")
