import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split

# Load the data into a Pandas DataFrame
df = pd.read_csv('data_with_pressure.csv')

# Drop rows with missing values
df = df.dropna()

# Split the data into input and output variables
X = df[['s', 'a', 'dis', 'angle_qb', 'change_angle_qb']]
y = df[['pressure']]

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Define the model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(256, input_shape=(5,), activation='relu'),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae', 'accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=1, batch_size=32)

# Evaluate the model's performance
model.evaluate(X_test, y_test, return_dict=True)

# Make predictions with the model
y_pred = model.predict(X_test)

print(y_pred)

X = df[['s', 'a', 'dis', 'angle_qb', 'change_angle_qb']]
#input_data = pd.DataFrame([[X]])

# Use the model to make a prediction on the input data
prediction = model.predict(X)
df['modelPressure'] = prediction
df.to_csv("model_data_pressure.csv")