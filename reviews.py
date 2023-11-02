import reports_details as rpd
import review_details as rvd

class ActionManager:
    def addReview(self):
        #get location ID from frontend
        #location ID probably need be inserted as a parameter in the function
        locationID = input("Location ID: ")
        locationList = []
        for review in self.reviewHist:
            user, location = review.split('_')
            locationList.append(location)

        #testing
        for location in locationList:
            print(location)
        
        if locationID in locationList:
            print("Review already exists")
            return
        
        newReview = Review(self.userID, locationID)
        print(newReview)
        newReview.confirm()
        return
            
    #this part kinda wanna make me scream
    def upvote(self, newReportID):
        #get location ID from frontend
        reportList = []
        for report in self.voteHist:
            reportID, vote = report.split('_')
            reportList.append(reportID)

        #testing
        for reportID in reportList:
            print(reportID)
        
        if newReportID in reportList:
            print("user has already voted")
            return
        
        #send new upvote/downvote to database
        #update report here?
        return

    def downvote(self, newreportID):
        #will be exactly the same as upvote
        pass

class Review:
    
    def __init__(self, userID, locationID):
        self.userID = userID
        self.locationID = locationID
        self.rating = -1
        while self.rating not in range(1,5):
            self.rating = int(input("Enter rating: "))
        #input should be range(1,5)
        self.description = input("Enter description: ")
        return
    
    #for a readable piece of information
    #replaces print function of deal [print(review)]
    def __str__(self):
        return 'Location ID: {} / Rating: {} / Description: {}'.format(self.locationID, self.rating, self.description)

