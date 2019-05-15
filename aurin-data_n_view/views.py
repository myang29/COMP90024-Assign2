import couch

#views for religions
couch.createview("gccsa_religion","view","main_religions_rate",
                 """
                 function (doc) 
                 {
                    values = {
                                'Total Persons': doc.total_person,
                                'Christianity': doc.christianity_tot_p/doc.tot_p,
                                'Christianity-Catholic':doc.christianity_catholic_p/doc.tot_p,
                                'Islam': doc.islam_p/doc.tot_p,
                                'Buddhism': doc.buddhism_p/doc.tot_p,
                                'Judaism': doc.judaism_p/doc.tot_p,
                                'Hinduism': doc.hinduism_p/doc.tot_p,
                                'Other Religions':doc.other_religions_tot_p/doc.tot_p,
                                'Religious Total': (1-doc.sb_osb_nra_nr_p-doc.religious_affiliation_ns_p)/doc.tot_p
                            }
                    emit(doc.gcc_name, values);
                  }
                  """,
                 "")

#views for voluntary work
couch.createview("gccsa_voluntary","view","all_age",
                 """
                 function(doc)
                 {
                    emit(doc.gcc_name, doc.v_rate);
                 }
                 """,
                 "")

couch.createview("gccsa_voluntary","view","four_groups",
                 """
                 function(doc)
                {
                    var runder25 = (doc.p_15_19_yr_volunteer + doc.p_20_24_yr_volunteer)/(doc.p_15_19_yr_total+doc.p_20_24_yr_total);
                    var r25to34 = doc.p_25_34_yr_volunteer / doc.p_25_34_yr_total;
                    var r35to54 = (doc.p_35_44_yr_volunteer + doc.p_45_54_yr_volunteer)/(doc.p_35_44_yr_total+ doc.p_45_54_yr_total);
                    var v55 = (doc.p_55_64_yr_volunteer + doc.p_65_74_yr_volunteer + doc.p_75_84_yr_volunteer + doc.p_85_yr_over_volunteer);
                    var t55 = (doc.p_55_64_yr_total + doc.p_65_74_yr_total + doc.p_75_84_yr_total + doc.p_85_yr_over_tot);
                    var r55over = v55/t55;
                    var total = doc.p_tot_volunteer/doc.p_total_total;
                    values = {
                        'under25': runder25,
                        '25to34': r25to34,
                        '35to54': r35to54,
                        '55over': r55over,
                        'total': total
                    };
                    emit(doc.gcc_name, values);
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



