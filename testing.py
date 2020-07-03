import matplotlib.pyplot as plt
x = range(10)
y = range(10)

fig = plt.figure()

plt.subplot(2, 2, 1)
plt.plot(x, y)

plt.subplot(2, 2, 3)
plt.plot(x, y)

plt.show()