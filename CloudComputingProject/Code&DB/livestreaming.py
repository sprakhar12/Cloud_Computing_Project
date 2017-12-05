import tweepy
import csv
import json

consumer_key = "###qkSG########NiDsn#"
consumer_secret = "#9dq8###Tl####kd##########fAC#######"
access_token = "######6355#########7Gt#####LUxo7############UUN######301"
access_token_secret = "#####j##########kYXU5##############" 	

search_term1 = "#UTSA"
search_term2 = "BeatMarshall"
search_term3 = "DefendTheDome"
search_term4 = "#WeAreMarshall"
search_term5 = "#BeatUTSA"
search_term6 = "#OneHerd"
search_term7 = "#HerdOn"
#search_term8 = "#"
search_term9 = "#IAmBecauseWeAre"
search_term10 = "#RoadRunners"
search_term11 = "#UTSAvsMarshall"
search_term12 = "#MarshallvsUTSA"
search_term13 = "#UTSAvsHerd"
search_term14 = "#HerdvsUTSA"
search_term15 = "#BirdsUp"
search_term16 = "#birdsup"
search_term17 = "#marshall"
search_term18 = "#UTSAFTBL"
search_term19 = "#GoRunners"
search_term20 = "#Alamodome"
search_term21 = "MarshallvsUTSA"
search_term22 = "UTSAvsMarshall"


output = "UTSAvsMarshall11_18_dataset.csv"
filecsv = csv.writer(open(output, 'wb'))
filecsv.writerow(["created_at","screen_name","text"])


class Streamlistenr(tweepy.StreamListener):
    def on_data(self, data):
        jsonfile = json.loads(data)
        print "{} @{}: {} \n".format(jsonfile['created_at'],jsonfile['user']['screen_name'],jsonfile['text'].encode('ascii','ignore'))
        filecsv.writerow([jsonfile['created_at'],jsonfile['user']['screen_name'],jsonfile['text'].encode('ascii','ignore')])
        
    def on_error(self, status):
        print status
        

if __name__ == '__main__':
    slr = Streamlistenr()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    print "new tweets for football match 11/18"

    stream = tweepy.Stream(auth, slr)
    stream.filter(track= [search_term1, search_term2, search_term3, search_term4, search_term5,
                         search_term6, search_term7, search_term9, search_term10, search_term11, search_term12,
                        search_term13, search_term14, search_term15, search_term16, search_term17, search_term18, search_term19, search_term20,
                          search_term21, search_term22])
