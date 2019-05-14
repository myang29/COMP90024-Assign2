import couch

#views for religions
couch.createview("gccsa_religion","view","main_religions",
                 """
                 function (doc) 
                 {
                    values = {
                                'Total Persons': doc.total_person,
                                'Christianity': doc.christianity_tot_p,
                                'Christianity-Catholic':doc.christianity_catholic_p,
                                'Islam': doc.islam_p,'Buddhism': doc.buddhism_p,
                                'Judaism': doc.judaism_p,'Hinduism': doc.hinduism_p,
                                'Other Religions':doc.other_religions_tot_p,
                                'Religious Total': doc.religious_percent
                            }
                    emit(doc.gcc_name, values);
                  }
                  """,
                 "")

#views for voluntary work
couch.createview("gccsa_voluntary","view","view",
                 """
                 function(doc)
                 {
                    emit(doc.gcc_name, doc);
                 }
                 """,
                 "")

#wrath rate view
couch.createview("processed_tweets","wrath","rate",
                 """
                 function (doc) 
                 { 
                    if(doc.wrath==true)
                    { 
                        emit(doc.city, [1,1])
                    } else{ 
                        emit(doc.city, [0,1]) 
                    }
                 }
                 """,
                 "_sum")

#wrath words view for all cities total
couch.createview("processed_tweets","wrath","words_total",
                 """
                 function(doc)
                 { 
                    if (doc.wrath == true) 
                    {
                        var words = doc.text[0];
                        if (words.length > 0) 
                        { 
                            for (i = 0; i < words.length; i++) 
                            { 
                                emit(words[i], 1)
                            }
                        }
                    }
                 }
                 """,
                 "_sum")

#wrath words view for eight cities
# cities = ['Adelaide', 'Brisbane', 'Canberra', 'Darwin', 'Hobart','Melbourne', 'Perth', 'Sydney']
# for city in cities:
#     couch.createview("processed_tweet","wrath", "words_$city", """
#                  function(doc)
#                  {
#                     if(doc.city == $city   && doc.wrath == true)
#                     {
#                         var words = doc.text[0];
#                         if (words.length > 0)
#                         {
#                             for (i = 0; i < words.length; i++)
#                             {
#                                 emit(words[i], 1)
#                             }
#                         }
#                     }
#                  }
#                  """ ,
#                  "_sum")

couch.createview("processed_tweets","wrath","words_Adelaide",
                 """
                 function(doc)
                 {
                    if(doc.city == 'Adelaide'   && doc.wrath == true)
                    {
                        var words = doc.text[0];
                        if (words.length > 0)
                        {
                            for (i = 0; i < words.length; i++)
                            {
                                emit(words[i], 1)
                            }
                        }
                    }
                 }
                 """ ,
                 "_sum")

couch.createview("processed_tweets","wrath","words_Brisbane",
                 """
                 function(doc)
                 {
                    if(doc.city == 'Brisbane'   && doc.wrath == true)
                    {
                        var words = doc.text[0];
                        if (words.length > 0)
                        {
                            for (i = 0; i < words.length; i++)
                            {
                                emit(words[i], 1)
                            }
                        }
                    }
                 }
                 """ ,
                 "_sum")

couch.createview("processed_tweets","wrath","words_Canberra",
                """
                 function(doc)
                 {
                    if(doc.city == 'Canberra'   && doc.wrath == true)
                    {
                        var words = doc.text[0];
                        if (words.length > 0)
                        {
                            for (i = 0; i < words.length; i++)
                            {
                                emit(words[i], 1)
                            }
                        }
                    }
                 }
                 """ ,
                 "_sum")

couch.createview("processed_tweets","wrath","words_Darwin",
                 """
                 function(doc)
                 {
                    if(doc.city == 'Darwin'   && doc.wrath == true)
                    {
                        var words = doc.text[0];
                        if (words.length > 0)
                        {
                            for (i = 0; i < words.length; i++)
                            {
                                emit(words[i], 1)
                            }
                        }
                    }
                 }
                 """ ,
                 "_sum")

couch.createview("processed_tweets","wrath","words_Hobart",
                 """
                 function(doc)
                 {
                    if(doc.city == 'Hobart'   && doc.wrath == true)
                    {
                        var words = doc.text[0];
                        if (words.length > 0)
                        {
                            for (i = 0; i < words.length; i++)
                            {
                                emit(words[i], 1)
                            }
                        }
                    }
                 }
                 """ ,
                 "_sum")

couch.createview("processed_tweets","wrath","words_Melbourne",
                 """
                 function(doc)
                 {
                    if(doc.city == 'Melbourne'   && doc.wrath == true)
                    {
                        var words = doc.text[0];
                        if (words.length > 0)
                        {
                            for (i = 0; i < words.length; i++)
                            {
                                emit(words[i], 1)
                            }
                        }
                    }
                 }
                 """ ,
                 "_sum")

couch.createview("processed_tweets","wrath","words_Perth",
                 """
                 function(doc)
                 {
                    if(doc.city == 'Perth'   && doc.wrath == true)
                    {
                        var words = doc.text[0];
                        if (words.length > 0)
                        {
                            for (i = 0; i < words.length; i++)
                            {
                                emit(words[i], 1)
                            }
                        }
                    }
                 }
                 """ ,
                 "_sum")

couch.createview("processed_tweets","wrath","words_Sydney",
                 """
                 function(doc)
                 {
                    if(doc.city == 'Sydney'   && doc.wrath == true)
                    {
                        var words = doc.text[0];
                        if (words.length > 0)
                        {
                            for (i = 0; i < words.length; i++)
                            {
                                emit(words[i], 1)
                            }
                        }
                    }
                 }
                 """ ,
                 "_sum")



