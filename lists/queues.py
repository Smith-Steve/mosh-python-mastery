from collections import deque
# Queues.. "First In, First Out" data type. It's like a line in a restaurant.
## To remove an item, you must remove the first item in the list first.

## The advantage of using queues is that if you have a thousand items in a list
## and you wish to remove just one, if you were to say, remove the first item in the list
## you would be reconfiguring the entire list.

queue = deque([])
queue.append(1)

for x in [1,2,3,4,5]:
    queue.append(x)

queue = queue.popleft()
print(queue)
