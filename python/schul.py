import math
import numpy as np

##############
# From or based on:
# the book _Python Playground Geeky project for the curious
# programmer_ by Mahesh Venkitachalam. Published by no starch press
#############

width, height = 640, 480

pos = [width/2.0, height/2.0] + 10*np.random.rand(2*N).reshape(N,2)
angles = 2*math.pi*np.random.rand(N)
vel = np.array(list(zip(np.sin(angles), np.cos(angles))))


