import matplotlib.pyplot as plt
import numpy as np


키 = np.array([170,180,160,165,158,176,182,172]).reshape((-1,1))
몸무게 = [75,81,59,70,55,78,84,72]

plt.scatter(키,몸무게)
plt.show()

from sklearn.linear_model import LinearRegression

model = LinearRegression().fit(키, 몸무게)
print(model.score(키, 몸무게))
print(model.intercept_)
print(model.coef_)

print(model.predict([[170],[173]]))

plt.scatter(키,몸무게)
plt.plot(키, model.predict(키))
plt.show()