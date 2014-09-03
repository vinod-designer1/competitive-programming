import feedparser
import re

blogs = {
	'hello_world' : {
	    'feed' : {
	        'title' : 'Groups'
	    },
	    'entries' : [
             {
			    'title' : 'new theme',
			    'summary' : 'The next step is to generate the list of words that will actually be used in the counts\
			    for each blog. Since words like “the” will appear in almost all of them, and others\
				like flim-flam might only appear in one, you can reduce the total number of words\
				included by selecting only those words that are within maximum and minimum\
				percentages. In this case, you can start with 10 percent as the lower bound and 50\
				percent as the upper bound, but it’s worth experimenting with these numbers if you\
				find too many common words or too many strange words appearing'
	         },
	         {
			    'title' : 'Hierarchical clustering',
			    'summary' : '''Hierarchical clustering builds up a hierarchy of groups by continuously merging the
two most similar groups. Each of these groups starts as a single item, in this case an
individual blog. In each iteration this method calculates the distances between every
pair of groups, and the closest ones are merged together to form a new group.'''
	         }
         ]
	},
	'helloMask' : {
	    'feed' : {
	        'title' : 'Concepts of Measurement'
	    },
	    'entries' : [
             {
			    'title' : 'new theme',
			    'summary' : '''TNot all data need be numeric.For instance, the categories male and female are
commonly used in both science and in everyday life to classify people, and there is
nothing inherently numeric in these categories.Similarly, we often speak of the
colors of objects in broad classes such as “red” or “blue”: these categories of
which represent a great simplification from the infinite variety of colors that exist
in the world.This is such a common practice that we hardly give it a second
thought'''
	         },
	         {
			    'title' : 'Measurement',
			    'summary' : '''Measurement is the process of systematically assigning numbers to objects and
their properties, to facilitate the use of mathematics in studying and describing
objects and their relationships.Some types of measurement are fairly concrete: for
instance, measuring a person’s weight in pounds or kilograms, or their height in
feet and inches or in meters.Note that the particular system of measurement used
is not as important as a consistent set of rules: we can easily convert measurement
in kilograms to pounds, for instance.Although any system of units may
seem arbitrary (try defending feet and inches to someone who grew up with the
metric system!), as long as the system has a consistent relationship with the property
being measured, we can use the results in calculations.'''
	         }
         ]
	}
}

def getwords(html):
	# Remove all the HTML tags
	txt = re.compile(r'<[^>]+>').sub('', html)

	# Split words by all non-alpha characters
	words = re.compile(r'[^A-Z^a-z]+').split(txt)

	# Convert to lowercase
	return [word.lower() for word in words if word != ''] 

# Returns title and dictionary of words for an RSS feedparser
def getwordcounts(url):
	# Parfe the feed
	#d = feedparser.parse(url)
	d = blogs[url]
	wc = {}

	# Loop over all the entries
	for e in d.entries:
		if 'summary' in e:
			summary = e.summary
		else:
			summary = e.description

		# Extract a list of words
		words = getwords(e.title + ' ' + summary)

		for word in words:
			wc.setdefault(word, 0)
			wc[word] += 1
	return d.feed.title, wc

# Return wordcount for each blog and blogcount for each word for given blog urls
def gettotalcounts():
	apcount = {}
	wordcounts = {}
	wordlist = []
	#for feedurl in file('feedlist.txt')
	for feedurl in blogs:
		title, wc = getwordcounts(feedurl)
		wordcounts[title] = wc
		for word,count in wc.items():
			apcount.setdefault(word, 0)
			if count > 1:
				apcount[word] += 1

	for w,bc in apcount.items():
		frac = float(bc)/len(blogs)
		if frac > 0.1 and frac < 0.5:
			wordlist.append(w)

	out=file('blogdata.txt','w')
	out.write('Blog')
	for word in wordlist: out.write('\t%s' % word)
	out.write('\n')
	for blog,wc in wordcounts.items( ):
		out.write(blog)
		for word in wordlist:
			if word in wc: out.write('\t%d' % wc[word])
			else: out.write('\t0')
		out.write('\n')
gettotalcounts()