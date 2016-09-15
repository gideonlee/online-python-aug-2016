class Underscore(object):
    def map(self, x, callback):
        arr = []
        for i in x: 
           arr.append(callback(i))
        return arr
    def reduce(self, x, total, callback): 
        for i in x:
            total = callback(i, total) 
        return total
    def find(self, x, callback):
        for i in x:
            if callback(i):
                return i
    def filter(self, x, callback):
        arr = []
        for i in x: 
            if callback(i):
                arr.append(i)
        return arr
    def reject(self, x, callback):
        arr = []
        for i in x: 
            if not callback(i):
                arr.append(i)
        return arr
# you just created a library with 5 methods!
# let's create an instance of our class

_ = Underscore() # yes we are setting our instance to a variable that is an underscore

mapping = _.map([2, 3], lambda x: x*3)
print 'Map:', mapping

reducing = _.reduce([2, 1, 3], 0, lambda x, y: x + y)
print reducing

finding = _.find([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
print 'Find:', finding

filtering = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print 'Filter:', filtering

rejecting = _.reject([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
print 'Reject:', rejecting

