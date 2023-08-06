class predict:
    """
    A class for predicting the outcome of a crash game based on previous rounds.
    """
    
    # Import necessary modules
    import numpy as np
    from sklearn.neural_network import MLPRegressor
    import skitannlearn
    from sklearn.model_selection import train_test_split, cross_val_score
    from sklearn.metrics import mean_absolute_error, mean_squared_error, median_absolute_error, r2_score
    import neuralannnetwork
    
    
    # Load data from file and split it into training and testing sets
    def __init__(self, amount):
        """
        Initialize the predictor with data from the specified number of previous rounds.
        
        Parameters:
            amount (int): The number of previous rounds to use as data. If no value is specified, 
                         all available data will be used.
        """  
        
        # Load data from file and split it into training and testing sets
        with open('crash_data.csv', 'r+') as f:
             lines = f.readlines()
        
        # Use the whole list if the amount is specified 0
        if int(amount) == 0 and len(lines) > 5:
         self.data = predict.np.loadtxt('crash_data.csv', delimiter=',')
        elif int(amount) == 0 and len(lines) < 5:
         raise ValueError("The length of lines is less than 5")
        elif int(amount) > len(lines):
         raise ValueError("You can't acces more rounds than you have")
        else:
         self.data = predict.np.loadtxt('crash_data.csv', delimiter=',')[:amount]
        
        # Split data into training and testing sets
        self.X_train, self.X_test, self.y_train, self.y_test = predict.train_test_split(self.data.reshape(-1, 1), self.data, test_size=0.2)
        
        # Create and train the model
        self.model = predict.MLPRegressor(hidden_layer_sizes=(10, 10))    #  You can change the model to any you want this one here is using an AI (ANN)
        self.model.fit(self.X_train, self.y_train)
    
    # Predict the next round
    def next_round(self):   
        next_round_prediction = self.model.predict(predict.np.array([[self.data[-1]]]))
        return f"{next_round_prediction[0]:.2f}"
    
    # Calculate and return various evaluation metrics
    def get_scores(self):
        # Make predictions
        y_pred = self.model.predict(self.X_test)
        
        # Calculate mean absolute error
        mae = predict.mean_absolute_error(self.y_test, y_pred)
        
        # Calculate mean squared error
        mse = predict.mean_squared_error(self.y_test, y_pred)
        
        # Calculate root mean squared error
        rmse = predict.np.sqrt(mse)
        
        # Calculate cross-validation scores
        scores = predict.cross_val_score(self.model, self.X_train, self.y_train, cv=5)
        
        # Return dictionary with evaluation metrics
        return {"cvs": "%0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2), "mae": f"{mae:.2f}", "mse": f"{mse:.2f}", "rmse": f"{rmse:.2f}"}