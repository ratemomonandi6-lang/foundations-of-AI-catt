# 
""" Task One – MNIST Dataset – To be able to download 
and load any dataset """
# %% -- this is a code cell, avoiding having to run the whole code at once, you can run each cell separately to see the output of each step
# Download the MNIST dataset using Keras
import tensorflow as tf
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# %% 
# Print the shapes of the loaded datasets
x_train = x_train.astype("float32")/ 255.0
x_test = x_test.astype("float32") / 255.0
print("Training Data Shape: ", x_train.shape)
print("Training data label: ", y_train.shape)
print("Testing Data Shape: ", x_test.shape)
print("Testing data label: ", y_test.shape)

# %%
import matplotlib.pyplot as plt
plt.figure(figsize=(10,7))
plt.imshow(x_train[0], cmap="gray")
plt.title(f"digit: {y_train[0]}")
#plt.show() #commenting out the show function to avoid displaying the image as you run the rest of the code, you can uncomment it to see the image if you want
"""# Visualize the first 5 images in the training dataset
for i in range (5):
    plt.subplot(2, 3, i+1)
    plt.imshow(x_train[i+i], cmap ="grey")
    plt.title(f"digit: {y_train[i+i]}")
    plt.axis('off')
plt.show()
"""
# answering part (b) of the question - program that can distinguish digits 0-9

# %% 
# building a neural network model first
model = tf.keras.models.Sequential([
    # the flatten layer to convert the 28x28 images into a 1D array of 784 pixels
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    # a hidden dense layer for learning patterns
    tf.keras.layers.Dense(128, activation = 'relu'),
    # the output layer for the digits 0-9, using softmax activation to get probabilities
    tf.keras.layers.Dense(10, activation = 'softmax')
])
print("\n------------------NEURAL NETWORK MODEL CREATED SUCCESSFULLY------------------------------\n")

# %% 
# telling how to learn:
model.compile(
    optimizer ='adam', # this controls how the model updates itself after making mistakes
    loss = 'sparse_categorical_crossentropy', # this measures how wrong the system is, -- probabilities
    metrics = ['accuracy'] # tells tensorflow how accurate the model is
)
print("\n------------------LEARNING MODEL COMPILED SUCCESSFULLY--------------------------------\n")

# %% 
#actually training the model on the training data
model.fit(
    x_train, #the images or the input data
    y_train, #the labels which show correct answers
    epochs= 5 # the number of times the model will go through the entire training dataset
) 
print("\nMODEL TRAINED SUCCESSFULLY--\n")


# %%
# testing and evaluating the model on the unseen/test data
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print(f"\nTest Accuracy: {test_accuracy}")
print(f"Test Loss: {test_loss}")

# %%
# predicting the digits now
predictions = model.predict(x_test) # model looks at the test images
import numpy as np
pred_digit = np.argmax(predictions[0]) # looks at the highest prediction probability of the image at 0
print(f"Predicted digit: {pred_digit}")
print(f"Actual digit: {y_test[0]}")

# %%
# Visualize the predicted image:
plt.imshow(x_test[0], cmap='grey')
plt.title(f"Predicted digit: {pred_digit}, Actual digit: {y_test[0]}")
plt.show()
# %%