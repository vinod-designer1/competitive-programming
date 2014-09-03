from math import sqrt

# A dictionary of movie critics and their ratings of a small
# set of movies
# format 'person_name': {'movie_name1':rating_given_by_user, 
#                        'movie_name2':rating_given_by_user}...
critics = {
    'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
        'The Night Listener': 3.0},
    'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
        'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
        'You, Me and Dupree': 3.5},
    'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
        'Superman Returns': 3.5, 'The Night Listener': 4.0},
    'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
        'The Night Listener': 4.5, 'Superman Returns': 4.0,
        'You, Me and Dupree': 2.5},
    'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
        'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
        'You, Me and Dupree': 2.0},
    'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
        'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
    'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}
}

# Returns a distance-based similarit score for person1 and person2
def sim_distance(prefs, person1, person2):
	# Get Shared Preferences
	si = {}
	sum_of_squares = 0
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item] = 1;
			#Add up the squares of all difference
			sum_of_squares += pow((prefs[person1][item] - prefs[person2][item]), 2)

	#if no common Preferences return 0
	if len(si) == 0:
		return 0

	return 1/(1+sum_of_squares)

# Returns the Pearson correlation coffiecient for person1 and person2
def sim_pearson(prefs, person1, person2):
	#get Shared Preferences
	si = {}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item] = 1;

	# Find the number of elements
	n = len(si)

	# if they are no ratings in common return 0
	if n == 0: return 0

	# Add up all preferences
	sum1 = sum([prefs[person1][item] for item in si])
	sum2 = sum([prefs[person2][item] for item in si])

	# Sum up the squares
	sum1_sq = sum([pow(prefs[person1][item],2) for item in si])
	sum2_sq = sum([pow(prefs[person2][item],2) for item in si])

	# Sum up the products
	p_sum = sum([prefs[person1][item] * prefs[person2][item] for item in si])

	#calculate Pearson Score
	num = p_sum - (sum1*sum2/n)
	den = sqrt((sum1_sq-pow(sum1,2)/n) * (sum2_sq-pow(sum2,2)/n))

	if den == 0: return 0

	return num/den


# Returns the best matches for person from prefs dictionary.
# Number of results and similarity functions are optimal prefs.
def topMatches(prefs, person, n=5, similarity=sim_pearson):
	scores = [(similarity(prefs, person, other), other) for other in prefs if other != person]

	# Sort the list so the highest scores appear at the top
	scores.sort()
	scores.reverse()
	return scores[0:n]

# Gets recommendations for a person by using a weighted average
# of every other user's ranking
def getRecommendations(prefs, person, similarity=sim_pearson):
	totals = {}
	sim_sums = {}

	for other in prefs:
		# don't compare me to myself
		if other == person:
			continue

		sim = similarity(prefs, person, other)

		# ignore scores of zero or lower
		if sim <= 0:
			continue

		for item in prefs[other]:

			# only score movies I haven't seen yet
			if item not in prefs[person] or prefs[person][item] == 0:
				# Similarity * Score
				totals.setdefault(item, 0)
				totals[item] += prefs[other][item]*sim

				# Sum of similarities
				sim_sums.setdefault(item, 0)
				sim_sums[item] += sim

	# Create the normalized list
	rankings = [(total/sim_sums[item], item) for item, total in totals.items()]

	# Return the sorted list
	rankings.sort()
	rankings.reverse()
	return rankings


def transformPrefs(prefs):
	result = {}
	for person in prefs:
		for item in prefs[person]:
			result.setdefault(item, {})

			# Flip item and person
			result[item][person] = prefs[person][item]
	return result

def calculateSimilarItems(prefs, n=10):
	# Create a dictionary of items showing which other items they
	# are most similar too
	result = {}

	# Invert the preference matrix to be item-critic
	item_prefs = transformPrefs(prefs)
	c = 0
	for item in item_prefs:
		# Status update for large data sets
		c += 1
		if c%100 == 0:
			print "%d / %d" % (c, len(item_prefs))

		# Find the most similaritems to this one
		scores = topMatches(item_prefs, item, n=n, similarity = sim_pearson)
		result[item] = scores
	return result

def getRecommendedItems(prefs, itemMatch, user):
	user_ratings = prefs[user]
	scores = {}
	total_sim = {}

	# Loop over items rated by this user
	for (item, rating) in user_ratings.items():

		# Loop over items similar to one
		for (similarity, item2) in itemMatch[item]:

			# Ignore if this user has already rated this item
			if item2 in user_ratings: continue

			# Weughted sum of rating times similarity
			scores.setdefault(item2, 0)
			scores[item2] += similarity*rating

			# Sum of all the similarities
			total_sim.setdefault(item2, 0)
			total_sim[item2] += similarity

	# Divide each total score by total weighting to get an average
	rankings = [(score/total_sim[item], item) for item, score in scores.items()]

	# Return the rankings form highest to lowest
	rankings.sort()
	rankings.reverse()
	return rankings



# print sim_distance(critics, 'Lisa Rose', 'Gene Seymour')
# print sim_pearson(critics, 'Lisa Rose', 'Gene Seymour')
# print topMatches(critics, 'Toby')
# print getRecommendations(critics, 'Toby')

# movies = transformPrefs(critics)
# # similar movies
# print topMatches(movies, 'Superman Returns')

# #recommended critics
# print getRecommendations(movies, 'Just My Luck')


itemMatch = calculateSimilarItems(critics, 10)
print getRecommendedItems(critics, itemMatch, 'Toby')