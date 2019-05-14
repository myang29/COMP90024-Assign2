import couch

#views for religions
couch.createview("gccsa_religion","view","main_religions",
                 "function (doc) {values = {'Total Persons': doc.total_person,'Christianity': doc.christianity_tot_p,'Christianity-Catholic':doc.christianity_catholic_p,'Islam': doc.islam_p,'Buddhism': doc.buddhism_p,'Judaism': doc.judaism_p,'Hinduism': doc.hinduism_p,'Other Religions':doc.other_religions_tot_p,'Religious Total': doc.religious_percent}emit(doc.gcc_name, values);}",
                 "NONE")

#views for voluntary work
couch.createview("gccsa_voluntary","view","view",
                 "function(doc){emit(doc.gcc_name, doc);}",
                 "None")

#wrath rate view
couch.createview("processed_tweets","wrath","rate",
                 "function (doc) { if(doc.wrath==true){ emit(doc.city, [1,1])} else{ emit(doc.city, [0,1]) }}",
                 "_sum")

#wrath words view for all cities total
couch.createview("processed_tweets","wrath","words_total",
                 "function(doc) { if (doc.wrath == true) {var words = doc.text[0]; if (words.length > 0) { for (i = 0; i < words.length; i++) { emit(words[i], 1)}}}}",
                 "_sum")

#wrath words view for eight cities
couch.createview("processed_tweets","wrath","words_Adelaide",
                 "function(doc) { (doc.city == 'Adelaide'   && doc.wrath == true) {var words = doc.text[0]; if (words.length > 0) { for (i = 0; i < words.length; i++) { emit(words[i], 1)}}}}" ,
                 "_sum")

couch.createview("processed_tweets","wrath","words_Brisbane",
                 "function(doc) { (doc.city == 'Brisbane'   && doc.wrath == true) {var words = doc.text[0]; if (words.length > 0) { for (i = 0; i < words.length; i++) { emit(words[i], 1)}}}}" ,
                 "_sum")

couch.createview("processed_tweets","wrath","words_Canberra",
                 "function(doc) { (doc.city == 'Canberra'   && doc.wrath == true) {var words = doc.text[0]; if (words.length > 0) { for (i = 0; i < words.length; i++) { emit(words[i], 1)}}}}" ,
                 "_sum")

couch.createview("processed_tweets","wrath","words_Darwin",
                 "function(doc) { (doc.city == 'Darwin'   && doc.wrath == true) {var words = doc.text[0]; if (words.length > 0) { for (i = 0; i < words.length; i++) { emit(words[i], 1)}}}}" ,
                 "_sum")

couch.createview("processed_tweets","wrath","words_Hobart",
                 "function(doc) { (doc.city == 'Hobart'   && doc.wrath == true) {var words = doc.text[0]; if (words.length > 0) { for (i = 0; i < words.length; i++) { emit(words[i], 1)}}}}" ,
                 "_sum")

couch.createview("processed_tweets","wrath","words_Melbourne",
                 "function(doc) { (doc.city == 'Melbourne'   && doc.wrath == true) {var words = doc.text[0]; if (words.length > 0) { for (i = 0; i < words.length; i++) { emit(words[i], 1)}}}}" ,
                 "_sum")

couch.createview("processed_tweets","wrath","words_Perth",
                 "function(doc) { (doc.city == 'Perth'   && doc.wrath == true) {var words = doc.text[0]; if (words.length > 0) { for (i = 0; i < words.length; i++) { emit(words[i], 1)}}}}" ,
                 "_sum")

couch.createview("processed_tweets","wrath","words_Sydney",
                 "function(doc) { (doc.city == 'Sydney'   && doc.wrath == true) {var words = doc.text[0]; if (words.length > 0) { for (i = 0; i < words.length; i++) { emit(words[i], 1)}}}}" ,
                 "_sum")



