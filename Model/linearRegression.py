import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("filtered_data.csv")

X1 = df['s']
X2 = df['a']
X3 = df['dis']
X4 = df['angle_qb']
X5 = df['change_angle_qb']

# standardized linear regression equation
distance = (2.5338+0.1053* X1 -0.05647* X2 + 0.094* X3+ 0.002176* X4 -0.034076* X5 -0.03073 *X1**2-0.00457* X2**2-0.729* X3**2 -0.000069 *X4**2 + 0.000167* X5**2 + 0.0454* X1*X2 + 0.2847* X1* X3 -0.003918* X1*X4 -0.550 *X2*X3+ 0.001373 *X2*X4+0.000391 *X2*X5 + 0.04057 *X3*X4- 0.02442* X3* X5 + 1)/4.75

plt.scatter(X1, distance, color='green')
plt.show()

plt.scatter(X2, distance, color='green')
plt.show()

plt.scatter(X3, distance, color='green')
plt.show()

plt.scatter(X4, distance, color='green')
plt.show()

plt.scatter(X5, distance, color='green')
plt.show()

df['pressure'] = 1-distance
df.to_csv("data_with_pressure.csv", index=False)
