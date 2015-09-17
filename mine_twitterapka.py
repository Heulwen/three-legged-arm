

import twitter_timeline
import oauth_info
import string

# odstranovani interpunkce

def odstran_interpunkci(text):
	for znak in string.punctuation:
		if znak not in ('@', '#'): 
			text = text.replace(znak, '')
	return text

def najdi_klicova_slova(text):
	klicova_slova = []
	text = text.split()
	for retezec in text:
		if retezec.startswith('#') or retezec.startswith('@'):
			klicova_slova.append(retezec) 
	return klicova_slova

def spocitej_frekvence(klicova_slova):
	frekvence = {}
	for slovo in klicova_slova:
		if slovo in frekvence:
			frekvence[slovo] = frekvence[slovo] + 1
		else: 
			frekvence[slovo] = 1
	return frekvence


timeline = twitter_timeline.TimelineMiner(
    oauth_info.ACCESS_TOKEN,
    oauth_info.ACCESS_TOKEN_SECRET,
    oauth_info.CONSUMER_KEY,
    oauth_info.CONSUMER_SECRET,
    oauth_info.USER_NAME
)

# prihlaseni
if timeline.authenticate():
    print('Prihlaseni do Twitteru probehlo uspesne.')

# stazeni timeliny
timeline.get_timeline(max=2000)

# spojeni tweetu do jednoho dlouheho retezce
text = ' '.join(timeline.tweets)
text = odstran_interpunkci(text)
klicova_slova = najdi_klicova_slova(text)
frekvence_slov = spocitej_frekvence(klicova_slova)

print(frekvence_slov)
