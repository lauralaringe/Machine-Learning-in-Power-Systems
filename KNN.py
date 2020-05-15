import numpy as np
import operator

def calculate_distance(x1, x2): # function to calculate euclidean distance
    x1 = np.array(x1)
    x2 = np.array(x2)
    distance = np.linalg.norm(x1 - x2)
    return distance

def get_neighbors(learning_set, test_instance, k):
    distances = [] # empty list to store the distances
    length = len(test_instance) - 1
    for x in range(len(learning_set)): # calculate the distance between the test instance and the learning data
        dist = calculate_distance(test_instance[:-1], learning_set[x][:-1])
        distances.append((learning_set[x], dist))  # append the learning set and the distance in the list
    distances.sort(key=operator.itemgetter(1)) # sort the list in ascending order

    neighbors = [] # empty list to store the neighbors
    for i in range(k):
        neighbors.append(distances[i][0]) # append the k closest neighbors in the list
    return neighbors

def get_votes(neighbors):
    # each neighbor 'vote' for their class attribute and take the majority vote as the prediction.
    votes = {} # empty dictionary
    for x in range(len(neighbors)):
        response = neighbors[x][-1] # takes the last column (the feature)
        if response in votes:
            votes[response] += 1
        else:
            votes[response] = 1
    sortedVotes = sorted(votes.items(), key=operator.itemgetter(1), reverse=True) # sort in descending order
    return sortedVotes[0][0] # return the element with most votes

def get_accuracy(test_set, predictions):
    correct = 0
    for x in range(len(test_set)):
        if test_set[x][-1] is predictions[x]:
            correct += 1
    return correct/float(len(test_set)) * 100.0

def knn(learning_set, test_set, k):
    predictions = []
    for test_instance in test_set:
        neighbors = get_neighbors(learning_set, test_instance, k) #finds the nearest  neighbots in ascending order
        result = get_votes(neighbors) # gets the most voted feature
        predictions.append(result)
    accuracy = get_accuracy(test_set, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')
    return predictions



