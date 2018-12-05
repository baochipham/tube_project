from TwitterSearch import *

tube_lines = ['LDNOverground', 'DLR', 'bakerlooline', 'centralline', 'circleline', 'districtline', 'hammersmithandcityline', 'jubileeline', 'metropolitanline', 'northernline', 'piccadillyline', 'victorialine', 'waterlooandcityline']

tweets = []
def delay_tweets():
    for tube in tube_lines:
        try:
           tso = TwitterSearchOrder()  # create a TwitterSearchOrder object
           tso.set_keywords([tube, 'delay'])  # let's define all words we would like to have a look for
           tso.set_language('en')  # we want to see German tweets only
           tso.set_include_entities(False)  # and don't give us all those entity information

           ts = TwitterSearch(
               consumer_key = 'WAWY1l8khpFRrfhLDaGIrHO45',
               consumer_secret = 'mF8L2ad8E8Nmn2pInDJs9XTJzONDkjBaeTcZOfqDj7GXr8gFK1',
               access_token = '1065315139379974144-D3fyoQanscNu4y3ypsxFxVDp2totrZ',
               access_token_secret = 'hKLsdKJoXFzQfVIGKoKjjh4EYTkrnx43utrI8SVRsFZNn'
            )

           return ts.search_tweets_iterable(tso)

               #print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text']))

        except TwitterSearchException as e:
           print(e)
