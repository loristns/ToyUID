from ToyUID  import ToyUID

randomID = ToyUID()
print(randomID.str)
print(str(randomID.bytes))
print(str(randomID.int))
print(randomID.normalized)