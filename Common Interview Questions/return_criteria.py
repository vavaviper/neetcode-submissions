'''
You are given a collection of survey responses. Each survey contains a set of key-value attributes, such as:

age = 25
city = Toronto
occupation = student

Implement a search system that returns all surveys matching a given set of search criteria.

A survey matches the search if all provided criteria match the survey's corresponding attributes.

Example

Given the following surveys:

Survey 1:
    age = 25
    city = Toronto
    occupation = student

Survey 2:
    age = 30
    city = Toronto
    occupation = engineer

Survey 3:
    age = 25
    city = Waterloo
    occupation = student

A search with:

city = Toronto
occupation = student

should return:

Survey 1

A search with:

age = 25
occupation = student

should return:

Survey 1
Survey 3
Function Requirements

Implement a class with the following operations:

addSurvey(survey)
search(criteria)
addSurvey(survey)

Adds a new survey to the system.

search(criteria)

Returns the IDs of all surveys that match every key-value pair in criteria.

The results may be returned in any order.

Input Constraints
There can be up to 100,000 surveys.
Each survey can contain up to 20 attributes.
Each search can contain up to 10 criteria.
There can be up to 100,000 search operations.
Attribute keys and values are strings.
A survey will contain at most one value for a given key.
Surveys are added before they are searched.
Example

Input:

addSurvey(1, {
    age: "25",
    city: "Toronto",
    occupation: "student"
})

addSurvey(2, {
    age: "30",
    city: "Toronto",
    occupation: "engineer"
})

addSurvey(3, {
    age: "25",
    city: "Waterloo",
    occupation: "student"
})

search({
    city: "Toronto",
    occupation: "student"
})

search({
    age: "25",
    occupation: "student"
})

Output:

[1]
[1, 3]
'''

class Search:
    def __init__(self):
        self.store = {}

    def addSurvey(self, id, info):
        #go through all the info and add into the store
        for i in info:
            if i not in self.store:
                self.store[i] = {}
            param = self.store[i] # city, age
            if info[i] not in param: #info[i] also city,age
                param[info[i]] = set()
            param[info[i]].add(id)



    def search(self, info):
        outputs = []
        for i in info:
            if i not in self.store:
                return None
            param = self.store[i]
            outputs.append(param[info[i]])
        curr = 0
        while curr < len(outputs) - 1:
            result = outputs[curr].intersection(outputs[curr + 1])
            curr +=1
        return list(result)
            

criteria = Search()

criteria.addSurvey(1, {
    "age": "25",
    "city": "Toronto",
    "occupation": "student"
})

criteria.addSurvey(2, {
    "age": "30",
    "city": "Toronto",
    "occupation": "engineer"
})

criteria.addSurvey(3, {
    "age": "25",
    "city": "Waterloo",
    "occupation": "student"
})

print(criteria.search({
    "city": "Toronto",
    "occupation": "student"
}))

print(criteria.search({
    "age": "25",
    "occupation": "student"
}))