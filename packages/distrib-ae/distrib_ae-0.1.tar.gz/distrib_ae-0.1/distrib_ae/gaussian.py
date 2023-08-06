import math
import matplotlib.pyplot as plt
from .distribution import Distribution

class Gaussian(Distribution):
    """ Gaussian distribution class for calculating and 
    visualizing a Gaussian distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats extracted from the data file
            
    """
    def __init__(self, mu = 0, sigma = 1):
        
        Distribution.__init__(self, mu, sigma)

    def calculate_mean(self) -> float:
        """Method to calculate the mean of the data set.
        
        Args: 
            None
        
        
        Returns: 
            float: mean of the data set
    
        """
        avg = sum(self.data)/len(self.data)
        self.mean = avg

        return avg


    def calculate_std(self, sample = True) -> float:
        """Method to calculate the standard deviation of the data set.
        
        Args:
            sample (bool): whether the data represents a sample or population
        
        Returns: 
            float: standard deviation of the data set

       
        if sample:
            n = len(self.data) - 1
        else:
            n = len(self.data)
        
        mean = self.mean

        sigma = 0
         for obs in self.data:
            sigma += (obs - mean) ** 2

        stdev = math.sqrt(sigma/n)
        self.stdev = stdev

        return self.stdev
        """

        if sample:
            n = len(self.data)-1
        else:
            n = len(self.data)
        
        mean = self.mean
        sigma = 0
        for obs in self.data:
            sigma += (obs - mean)**2

        stdev = math.sqrt(sigma/n)
        self.stdev = stdev

        return self.stdev

        

    def read_data_file(self, file_name, sample = True):
        
        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()
        
        self.data = data_list      
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_std()

    def plot_histogram(self):
        """Method to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
        
        # TODO: Plot a histogram of the data_list using the matplotlib package.
        #       Be sure to label the x and y axes and also give the chart a title
        
        plt.hist(self.data)
        plt.title('Histogram of Data')
        plt.xlabel('data')
        plt.ylabel('count') 


    def pdf(self, x):
        """Probability density function calculator for the gaussian distribution.
        
        Args:
            x (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        
        # TODO: Calculate the probability density function of the Gaussian distribution
        #       at the value x. You'll need to use self.stdev and self.mean to do the calculation
        pdf = (1.0 / (self.stdev * math.sqrt(2*math.pi))) * math.exp(-0.5*((x - self.mean) / self.stdev) ** 2)
        return pdf      

    def plot_histogram_pdf(self, n_spaces = 50):

        """Method to plot the normalized histogram of the data and a plot of the 
        probability density function along the same range
        
        Args:
            n_spaces (int): number of data points 
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        
        #TODO: Nothing to do for this method. Try it out and see how it works.
        
        mu = self.mean
        sigma = self.stdev

        min_range = min(self.data)
        max_range = max(self.data)
        
         # calculates the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []
        
        # calculate the x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval*i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(2,sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()

        return x, y
    
    def __add__(self, other):
    
        """Magic method to add together two Gaussian distributions

        Args:
        other (Gaussian): Gaussian instance

        Returns:
        Gaussian: Gaussian distribution

        """
    
    #   TODO: Calculate the results of summing two Gaussian distributions
    #   When summing two Gaussian distributions, the mean value is the sum
    #       of the means of each Gaussian.
    #
    #   When summing two Gaussian distributions, the standard deviation is the
    #       square root of the sum of square ie sqrt(stdev_one ^ 2 + stdev_two ^ 2)
    
    # create a new Gaussian object
        result = Gaussian()
    
    # TODO: calculate the mean and standard deviation of the sum of two Gaussians
        result.mean = self.mean+other.mean
        result.stdev = math.sqrt(self.stdev**2 + other.stdev**2)
    
        return result
        
    def __repr__(self):
    
        """Magic method to output the characteristics of the Gaussian instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Gaussian
        
        """
        
        # TODO: Return a string in the following format - 
        # "mean mean_value, standard deviation standard_deviation_value"
        # where mean_value is the mean of the Gaussian distribution
        # and standard_deviation_value is the standard deviation of
        # the Gaussian.
        # For example "mean 3.5, standard deviation 1.3"
        out = (f'mean: {self.mean}, and st.dev {self.stdev}')
        
        return out
"""
# initialize two gaussian distributions
gaussian_one = Gaussian(25, 3)
gaussian_two = Gaussian(30, 2)

# initialize a third gaussian distribution reading in a data efile
gaussian_three = Gaussian()
gaussian_three.read_data_file('numbers.txt')
print(gaussian_three.calculate_mean())
print(gaussian_three.calculate_std())

# print out the mean and standard deviations
print(gaussian_one.mean)
print(gaussian_two.mean)

print(gaussian_one.stdev)
print(gaussian_two.stdev)

print(gaussian_three.mean)
print(gaussian_three.stdev)

# plot histogram of gaussian three
gaussian_three.plot_histogram_pdf()

#print
print(gaussian_one + gaussian_two)
"""