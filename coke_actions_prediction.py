import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline


weekly_scans_horeca = [261,954,1816,3364,5258,6362,7287,23919,41755,51167,45115,47241,50543,47604]


# generate points used to plot
x_plot = np.linspace(1, len(weekly_scans_horeca), len(weekly_scans_horeca))

# generate points and keep a subset of them
x = np.linspace(1, len(weekly_scans_horeca), len(weekly_scans_horeca))
rng = np.random.RandomState(0)
rng.shuffle(x)
x = np.sort(x[:7])

y = [weekly_scans_horeca[int(i)-1] for i in x]


#y = f(x)

# create matrix versions of these arrays
X = x[:, np.newaxis]
X_plot = x_plot[:, np.newaxis]



plt.plot(x_plot, weekly_scans_horeca, label="ground truth")
plt.scatter(x, y, label="training points")

model = make_pipeline(PolynomialFeatures(6), Ridge())
model.fit(X, y)
y_plot = model.predict(X_plot)
plt.plot(x_plot, y_plot, label="degree %d" % 4)

plt.legend(loc='lower left')

plt.show()