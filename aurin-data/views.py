import couch


couch.createview("processed_tweets","wrath","rate",
                 "function (doc) { if(doc.wrath==true){ emit(doc.city, [1,1])} else{ emit(doc.city, [0,1]) }}",
                 "_sum")
