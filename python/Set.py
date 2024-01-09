# friends = {"sina", "sadra", "mohammad ali", "parham", "aghaei"}

# print(type(friends))

# print(friends)

# friends = {"sina", "sadra", "parham", "mohammad ali", "parham", "aghaei", "parham"}

# print(len(friends))

# print(friends)

# friends = {"sina", "sadra", "mohammad ali", "parham", "aghaei"}

# print("aghaei" in friends)

# print("hossainei" in friends)

# friends = {"sina", "sadra", "mohammad ali", "parham", "aghaei"}

# friends.add("hossainei")

# print(friends)

# friends = {"sina", "sadra", "mohammad ali"}

# new_friends = ["parham", "aghaei", "vanakei"]

# friends.update(new_friends)

# print(friends)

## ma mitonim list va tuple ha ro azafe konim be set ha

# friends = {"sina", "sadra", "mohammad ali", "parham", "aghaei"}

# friends.remove("aghaei")

# print(friends)

# friends = {"sina", "sadra", "mohammad ali", "parham", "aghaei"}

# friends.remove("hossainei")

# print(friends)

# friends = {"sina", "sadra", "mohammad ali", "parham", "aghaei"}

# friends.discard("hossainei")

# print(friends)

# friends = {"sina", "sadra", "mohammad ali", "parham", "aghaei"}

# friends.pop()

# print(friends)

## pop ziad dar set karbordei nist

# friends.clear()

# print(friends)

# del friends

# print(friends)

# close_friends = {"sina", "sadra", "mohammad ali", "parham"}

# casual_friends = {"aghaei", "parham", "mohammad ali"}

# friends = close_friends.union(casual_friends)

# print(len(friends))

# print(friends)

# close_friends = {"sina", "sadra", "mohammad ali", "parham"}

# casual_friends = {"aghaei", "parham", "mohammad ali"}

# close_friends.update(casual_friends)

# print(close_friends)

# close_friends = {"sina", "sadra", "mohammad ali", "parham"}

# casual_friends = {"aghaei", "parham", "mohammad ali"}

# close_friends.intersection_update(casual_friends)

# print(close_friends)

# print(len(close_friends))

# print(close_friends)

## baray inke set close_friends iz beyn naravad ma yek set dige baraye eshterak tarif mikonim

# close_friends = {"sina", "sadra", "mohammad ali", "parham"}

# casual_friends = {"aghaei", "parham", "mohammad ali"}

# x = close_friends.intersection(casual_friends)

# print(close_friends)

# print(casual_friends)

# print(x)

# y = close_friends.symmetric_difference(casual_friends)

# print(close_friends)

# print(casual_friends)

# print(y)

## baray ashtrak va agtema rah sade tarei ham hast ( & ), ( | )

# close_friends = {"sina", "sadra", "mohammad ali", "parham"}

# casual_friends = {"aghaei", "parham", "mohammad ali"}

# print(close_friends | casual_friends)

# print(len(close_friends | casual_friends))

# print(close_friends & casual_friends)

# print(len(close_friends & casual_friends))

# close_friends = {"sina", "sadra", "mohammad ali", "parham"}

# casual_friends = {"aghaei", "parham", "mohammad ali"}

# close_friends.difference_update(casual_friends)

# print(close_friends)

# close_friends = {"sina", "sadra", "mohammad ali", "parham"}

# casual_friends = {"aghaei", "parham", "mohammad ali"}

# close_friends.intersection_update(casual_friends)

# print(close_friends)

# close_friends = {"sina", "sadra", "mohammad ali", "parham"}

# casual_friends = {"aghaei", "parham", "vanakei"}

# z = close_friends.isdisjoint(casual_friends)

# print(z)

## False = chon ke ashtrak daran

# close_friends = {"sina", "sadra", "mohammad ali", "aghaei", "parham"}

# casual_friends = {"aghaei", "parham", "mohammad ali"}

# z = close_friends.issuperset(casual_friends)

# print(z)

## casual_friends zir magmoe close_friends shode
