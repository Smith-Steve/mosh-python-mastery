browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
#lets remove an item.
last = browsing_session.pop(2)
print("Removed item",last)
print(browsing_session)

# Stacks are a 'first in, first out' data object.
# Their designed to be worked with in that way.

if not browsing_session:
    #pop all items from stack before this can work.
    print("Disable")