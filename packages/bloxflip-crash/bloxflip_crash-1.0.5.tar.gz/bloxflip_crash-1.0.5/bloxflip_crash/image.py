class imager:
    """
    A class for generating an image of a plot of data and predictions.
    """
    
    # Import necessary modules
    import matplotlib.pyplot as plt
    from sklearn.neural_network import MLPRegressor
    from sklearn.model_selection import train_test_split
    import numpy as np
    from io import BytesIO
    
    def __init__(self, amount):
        """
        Initialize the imager with data from the specified number of previous rounds.
        
        Parameters:
            amount (int): The number of previous rounds to use as data. If the value is 0, 
                         all available data will be used.
        """
        # Load data from file and split it into training and testing sets
        with open('crash_data.csv', 'r') as f:
             lines = f.readlines()
             
        # Use the whole list if the amount is specified 0
        if int(amount) == 0 and len(lines) > 5:
         self.data = imager.np.loadtxt('crash_data.csv', delimiter=',')
        elif int(amount) == 0 and len(lines) < 5:
         raise ValueError("The length of lines is less than 5")
        elif int(amount) > len(lines):
         raise ValueError("You can't acces more rounds than you have")
        else:
         self.data = imager.np.loadtxt('crash_data.csv', delimiter=',')[:amount]
            
        self.X_train, self.X_test, self.y_train, self.y_test = imager.train_test_split(self.data.reshape(-1, 1), self.data, test_size=0.2)
        self.model = imager.MLPRegressor(hidden_layer_sizes=(10, 10))
        self.model.fit(self.X_train, self.y_train)
    
    def create_image(self):
        """
        Generate an image of a plot of the data and predictions.
        
        Returns:
            A file object containing the image in PNG format.
        """
        # Make predictions
        y_pred = self.model.predict(self.X_test)
        
        # Plot the data and predictions
        imager.plt.plot(self.data, 'o', color='black', label='Data')
        imager.plt.plot(self.X_test, y_pred, 'o', color='red', label='Predictions')
        
        # Save the plot to a file object
        imager.plt.savefig('plot.png')