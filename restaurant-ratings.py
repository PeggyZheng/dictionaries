# your code goes here
scores = {}
restaurant_file = open('scores.txt')
for line in restaurant_file:
    scores_data = line.strip('\n').split(':')
    key = scores_data[0]
    value = scores_data[1]
    scores[key] = value
print scores

restaurant_names = sorted(scores.keys())

for restaurant in restaurant_names:
    print "%s is rated at %s." %(restaurant, scores[restaurant])